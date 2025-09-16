import graphene
from infrastructure.graphql.types.user_type import UserType
from infrastructure.models.user_model import UserModel

class UserQuery(graphene.ObjectType):
    allUsers = graphene.List(UserType)
    userById = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_allUsers(root, info):
        return UserModel.objects.all()

    def resolve_userById(root, info, id):
        try:
            return UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return None
