import graphene

# TODO: Definir el tipo GraphQL para exponer datos de auditoría
class RoleType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    descripcion = graphene.String()
