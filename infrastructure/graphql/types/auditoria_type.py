import graphene

# TODO: Definir el tipo GraphQL para exponer datos de auditoría
class AuditoriaType(graphene.ObjectType):
    id = graphene.ID()
    usuario_id = graphene.Int()
    accion = graphene.String()
    tabla = graphene.String()
    registro_id = graphene.Int()
    detalles = graphene.String()
    fecha = graphene.String()
