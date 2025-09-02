import graphene
from infrastructure.models.auditoria_model import AuditoriaModel
from infrastructure.graphql.types.auditoria_type import AuditoriaType

# TODO: Definir mutaciones relacionadas con la auditoría.
# Esta clase permite crear registros de auditoría desde GraphQL.
class AuditoriaMutations(graphene.ObjectType):
    # TODO: Mutación para crear un registro de auditoría
    # 🔧 Mejora sugerida: validar que los valores cumplan políticas de seguridad
    createAuditoria = graphene.Field(
        AuditoriaType,
        usuario_id=graphene.Int(required=True),   # ID del usuario que realizó la acción
        accion=graphene.String(required=True),    # Acción realizada (INSERT, UPDATE, DELETE)
        tabla=graphene.String(required=True),     # Nombre de la tabla afectada
        registro_id=graphene.Int(),               # ID del registro afectado
        detalles=graphene.String()                # Detalles adicionales
    )

    # TODO: Resolver de la mutación createAuditoria
    # Encargado de registrar la acción en la base de datos
    def resolve_createAuditoria(root, info, usuario_id, accion, tabla, registro_id=None, detalles=None):
        # TODO: Crear instancia del modelo Auditoria con los datos proporcionados
        auditoria = AuditoriaModel(
            usuario_id=usuario_id,
            accion=accion,
            tabla=tabla,
            registro_id=registro_id,
            detalles=detalles
        )
        # TODO: Guardar el registro en la base de datos
        auditoria.save()

        # TODO: Retornar el objeto creado como respuesta de la mutación
        return auditoria
