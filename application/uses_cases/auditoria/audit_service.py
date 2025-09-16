from infrastructure.models.auditoria_model import Auditoria
import json

# TODO: Servicio para registrar acciones en la tabla de auditoría
class AuditService:
    @staticmethod
    def log(usuario_id, accion, tabla, registro_id=None, detalles=None):

        # TODO: convertir dict de detalles a JSON antes de guardarlo
        if isinstance(detalles, dict):
            detalles = json.dumps(detalles)

        # TODO: crear registro en la tabla Auditoria
        Auditoria.objects.create(
            usuario_id=usuario_id,
            accion=accion,
            tabla=tabla,
            registro_id=registro_id,
            detalles=detalles
        )
