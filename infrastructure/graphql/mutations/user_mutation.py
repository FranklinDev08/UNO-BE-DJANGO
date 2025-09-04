import graphene
from infrastructure.models.user_model import UserModel
from infrastructure.graphql.types.user_type import UserType
import hashlib

# Función para registrar auditoría (opcional)
from infrastructure.models.auditoria_model import AuditoriaModel
def registrar_auditoria(usuario, accion, tabla, registro_id=None, detalles=None):
    AuditoriaModel.objects.create(
        usuario_id=getattr(usuario, 'id', None),
        accion=accion,
        tabla=tabla,
        registro_id=registro_id,
        detalles=detalles
    )

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        rol_id = graphene.Int(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, username, email, password, rol_id):
        usuario = info.context.user  # viene del token en headers
        if not usuario or not getattr(usuario, 'id', None):
            return CreateUser(success=False, message="Debes iniciar sesión", user=None)
        if getattr(usuario, 'rol_id', None) != 1:  # solo admin
            return CreateUser(success=False, message="No tienes permisos para crear usuarios", user=None)

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = UserModel.objects.create(
            username=username,
            email=email,
            password=password_hash,
            rol_id=rol_id,
            activo=True
        )
        registrar_auditoria(usuario, "CREATE", "usuarios", user.id, f"Creado usuario: {username}")
        return CreateUser(user=user, success=True, message="Usuario creado")

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        rol_id = graphene.Int()
        activo = graphene.Boolean()

    user = graphene.Field(UserType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, id, username=None, email=None, password=None, rol_id=None, activo=None):
        usuario = info.context.user
        if not usuario or not getattr(usuario, 'id', None):
            return UpdateUser(success=False, message="Debes iniciar sesión", user=None)
        if getattr(usuario, 'rol_id', None) != 1:
            return UpdateUser(success=False, message="No tienes permisos para actualizar usuarios", user=None)

        try:
            user = UserModel.objects.get(pk=id)
            cambios = []
            if username: 
                cambios.append(f"username: {user.username} -> {username}")
                user.username = username
            if email: 
                cambios.append(f"email: {user.email} -> {email}")
                user.email = email
            if password: 
                user.password = hashlib.sha256(password.encode()).hexdigest()
            if rol_id: 
                cambios.append(f"rol_id: {user.rol_id} -> {rol_id}")
                user.rol_id = rol_id
            if activo is not None: 
                cambios.append(f"activo: {user.activo} -> {activo}")
                user.activo = activo
            user.save()
            registrar_auditoria(usuario, "UPDATE", "usuarios", user.id, "; ".join(cambios))
            return UpdateUser(user=user, success=True, message="Usuario actualizado")
        except UserModel.DoesNotExist:
            return UpdateUser(user=None, success=False, message="Usuario no encontrado")

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, id):
        usuario = info.context.user
        if not usuario or not getattr(usuario, 'id', None):
            return DeleteUser(success=False, message="Debes iniciar sesión")
        if getattr(usuario, 'rol_id', None) != 1:
            return DeleteUser(success=False, message="No tienes permisos para eliminar usuarios")

        try:
            user = UserModel.objects.get(pk=id)
            user.delete()
            registrar_auditoria(usuario, "DELETE", "usuarios", id, "Usuario eliminado")
            return DeleteUser(success=True, message="Usuario eliminado")
        except UserModel.DoesNotExist:
            return DeleteUser(success=False, message="Usuario no encontrado")

class UserMutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = UpdateUser.Field()
    deleteUser = DeleteUser.Field()
