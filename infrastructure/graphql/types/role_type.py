import graphene

class RoleType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    descripcion = graphene.String()
