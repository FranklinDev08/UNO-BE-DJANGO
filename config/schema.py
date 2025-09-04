import graphene

from infrastructure.graphql.queries.auditoria_query import AuditoriaQuery
from infrastructure.graphql.queries.role_query import RoleQuery
from infrastructure.graphql.queries.user_query import UserQuery

from infrastructure.graphql.mutations.auditoria_mutation import AuditoriaMutations
from infrastructure.graphql.mutations.role_mutation import RoleMutations
from infrastructure.graphql.mutations.user_mutation import UserMutations
from infrastructure.graphql.mutations.login_mutation import LoginMutations

# TODO: Definir el conjunto de queries disponibles en el esquema GraphQL
# Se hereda de AuditoriaQuery y graphene.ObjectType
class Query(
    AuditoriaQuery,
    RoleQuery,
    UserQuery,
    graphene.ObjectType
):
    # TODO: Query de prueba para verificar que la API está en funcionamiento
    hello = graphene.String(default_value="API GraphQL funcionando correctamente")

# TODO: Definir el conjunto de mutaciones disponibles en el esquema GraphQL
# Se hereda de AuditoriaMutations y graphene.ObjectType
class Mutation(
    AuditoriaMutations,
    RoleMutations,
    UserMutations,
    LoginMutations,
    graphene.ObjectType
):
    pass

# TODO: Crear el esquema principal que combina queries y mutaciones
schema = graphene.Schema(query=Query, mutation=Mutation)
