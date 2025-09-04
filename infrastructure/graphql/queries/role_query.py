import graphene
from infrastructure.models.role_model import RoleModel
from infrastructure.graphql.types.role_type import RoleType

class RoleQuery(graphene.ObjectType):
    all_roles = graphene.List(RoleType)
    role_by_id = graphene.Field(RoleType, id=graphene.ID(required=True))

    def resolve_all_roles(root, info):
        return RoleModel.objects.all()

    def resolve_role_by_id(root, info, id):
        try:
            return RoleModel.objects.get(id=id)
        except RoleModel.DoesNotExist:
            return None
