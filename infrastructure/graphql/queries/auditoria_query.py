import graphene
from infrastructure.models.auditoria_model import AuditoriaModel
from infrastructure.graphql.types.auditoria_type import AuditoriaType

# TODO: Definir las consultas (queries) relacionadas con la auditoría.
# Esta clase permite obtener registros de auditoría desde GraphQL.
class AuditoriaQuery(graphene.ObjectType):
    # TODO: Consulta para obtener todas las auditorías registradas
    allAuditorias = graphene.List(AuditoriaType)

    # TODO: Resolver de la consulta allAuditorias
    # Retorna todos los registros de auditoría ordenados por fecha descendente
    def resolve_allAuditorias(root, info):
        return AuditoriaModel.objects.all().order_by('-fecha')
