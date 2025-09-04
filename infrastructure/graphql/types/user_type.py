import graphene

class UserType(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    rol_id = graphene.Int()
    activo = graphene.Boolean()
