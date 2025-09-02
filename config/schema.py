import graphene

from infrastructure.graphql.queries.auditoria_query import AuditoriaQuery
from infrastructure.graphql.mutations.auditoria_mutation import AuditoriaMutations

# TODO: Definir el conjunto de queries disponibles en el esquema GraphQL
# Se hereda de AuditoriaQuery y graphene.ObjectType
class Query(
    AuditoriaQuery,
    graphene.ObjectType
):
    # TODO: Query de prueba para verificar que la API está en funcionamiento
    hello = graphene.String(default_value="API GraphQL funcionando correctamente")

# TODO: Definir el conjunto de mutaciones disponibles en el esquema GraphQL
# Se hereda de AuditoriaMutations y graphene.ObjectType
class Mutation(
    AuditoriaMutations,
    graphene.ObjectType
):
    pass

# TODO: Crear el esquema principal que combina queries y mutaciones
schema = graphene.Schema(query=Query, mutation=Mutation)
