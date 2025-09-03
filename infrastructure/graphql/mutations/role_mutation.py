import graphene
from infrastructure.models.role_model import RoleModel
from infrastructure.models.auditoria_model import AuditoriaModel
from infrastructure.graphql.types.role_type import RoleType
import jwt
from django.conf import settings

# TODO: Función para registrar auditoría en la base de datos
def registrar_auditoria(usuario, accion, tabla, registro_id=None, detalles=None):
    AuditoriaModel.objects.create(
        usuario_id=usuario.id if usuario else None,
        accion=accion,
        tabla=tabla,
        registro_id=registro_id,
        detalles=detalles
    )

# TODO: Función para validar token JWT y devolver el usuario autenticado
def get_usuario_desde_token(info):
    auth = info.context.META.get('HTTP_AUTHORIZATION', '')
    if not auth.startswith('Bearer '):
        return None
    token = auth.split(' ')[1]
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        from infrastructure.models.user_model import UserModel
        return UserModel.objects.get(id=payload['user_id'])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, UserModel.DoesNotExist):
        return None

# TODO: Mutation para crear un nuevo rol
class CreateRole(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        descripcion = graphene.String()

    # TODO: Campos de salida de la mutation
    role = graphene.Field(RoleType)
    success = graphene.Boolean()
    message = graphene.String()

    # TODO: Lógica de creación del rol
    def mutate(root, info, nombre, descripcion=None):
        usuario = get_usuario_desde_token(info)
        if not usuario:
            return CreateRole(success=False, message="Debes iniciar sesión", role=None)
        if usuario.rol_id != 1:
            return CreateRole(success=False, message="No tienes permisos para crear roles", role=None)

        role = RoleModel.objects.create(nombre=nombre, descripcion=descripcion)
        registrar_auditoria(usuario, "CREATE", "roles", role.id, f"Creado rol: {nombre}")
        return CreateRole(role=role, success=True, message="Rol creado correctamente")

# TODO: Mutation para actualizar un rol existente
class UpdateRole(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        descripcion = graphene.String()

    # TODO: Campos de salida de la mutation
    role = graphene.Field(RoleType)
    success = graphene.Boolean()
    message = graphene.String()

    # TODO: Lógica de actualización del rol
    def mutate(root, info, id, nombre=None, descripcion=None):
        usuario = get_usuario_desde_token(info)
        if not usuario:
            return UpdateRole(success=False, message="Debes iniciar sesión", role=None)
        if usuario.rol_id != 1:
            return UpdateRole(success=False, message="No tienes permisos para actualizar roles", role=None)

        try:
            role = RoleModel.objects.get(id=id)
            cambios = []
            if nombre:
                cambios.append(f"nombre: {role.nombre} -> {nombre}")
                role.nombre = nombre
            if descripcion:
                cambios.append(f"descripcion: {role.descripcion} -> {descripcion}")
                role.descripcion = descripcion
            role.save()
            registrar_auditoria(usuario, "UPDATE", "roles", role.id, "; ".join(cambios))
            return UpdateRole(role=role, success=True, message="Rol actualizado correctamente")
        except RoleModel.DoesNotExist:
            return UpdateRole(role=None, success=False, message="Rol no encontrado")

# TODO: Mutation para eliminar un rol
class DeleteRole(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    # TODO: Campos de salida de la mutation
    success = graphene.Boolean()
    message = graphene.String()

    # TODO: Lógica de eliminación del rol
    def mutate(root, info, id):
        usuario = get_usuario_desde_token(info)
        if not usuario:
            return DeleteRole(success=False, message="Debes iniciar sesión")
        if usuario.rol_id != 1:
            return DeleteRole(success=False, message="No tienes permisos para eliminar roles")

        try:
            role = RoleModel.objects.get(id=id)
            role.delete()
            registrar_auditoria(usuario, "DELETE", "roles", id, "Rol eliminado")
            return DeleteRole(success=True, message="Rol eliminado correctamente")
        except RoleModel.DoesNotExist:
            return DeleteRole(success=False, message="Rol no encontrado")

# TODO: Agrupar todas las mutations de roles para GraphQL
class RoleMutations(graphene.ObjectType):
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
