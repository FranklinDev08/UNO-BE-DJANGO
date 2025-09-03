import graphene

# ========================
# QUERIES
# ========================
from infrastructure.graphql.queries.role_query import RoleQuery

from infrastructure.graphql.queries.auditoria_query import AuditoriaQuery

# ========================
# MUTATIONS
# ========================


from infrastructure.graphql.mutations.role_mutation import RoleMutations
from infrastructure.graphql.mutations.auditoria_mutation import AuditoriaMutations


# ========================
# QUERIES COMBINADAS
# ========================
class Query(
    RoleQuery,
    AuditoriaQuery,
    graphene.ObjectType
    
):
    hello = graphene.String(default_value="API GraphQL funcionando 🚀")


# ========================
# MUTATIONS COMBINADAS
# ========================
class Mutation(
    RoleMutations,
    AuditoriaMutations,
    graphene.ObjectType
):
    pass


# ========================
# SCHEMA FINAL
# ========================
schema = graphene.Schema(query=Query, mutation=Mutation)
