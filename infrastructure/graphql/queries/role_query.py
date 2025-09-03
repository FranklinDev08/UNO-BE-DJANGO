import graphene
from infrastructure.models.role_model import RoleModel
from infrastructure.graphql.types.role_type import RoleType

# TODO: Definir las consultas (queries) relacionadas con los roles.
# Esta clase permite obtener roles desde GraphQL.
class RoleQuery(graphene.ObjectType):
    # TODO: Consulta para obtener todos los roles registrados
    all_roles = graphene.List(RoleType)
    
    # TODO: Consulta para obtener un rol específico por su ID
    role_by_id = graphene.Field(RoleType, id=graphene.ID(required=True))

    # TODO: Resolver de la consulta all_roles
    # Retorna todos los registros de roles
    def resolve_all_roles(root, info):
        return RoleModel.objects.all()

    # TODO: Resolver de la consulta role_by_id
    # Retorna el registro de rol que coincide con el ID proporcionado
    # Si no existe, retorna None
    def resolve_role_by_id(root, info, id):
        try:
            return RoleModel.objects.get(id=id)
        except RoleModel.DoesNotExist:
            return None
