from core.entities.role_entity import RoleEntity
from infrastructure.orm.role_repository_impl import RoleRepositoryImpl
from application.use_cases.auditoria.audit_service import AuditService

class RoleService:
    repo = RoleRepositoryImpl()

    @staticmethod
    def create_role(info, nombre, descripcion=None):
        role_entity = RoleEntity(nombre, descripcion)
        created_role = RoleService.repo.create(role_entity)
        AuditService.log(
            info.context.user_id,
            "CREATE",
            "Roles",
            created_role.id,
            detalles={"nombre": created_role.nombre, "descripcion": created_role.descripcion}
        )
        return created_role

    @staticmethod
    def update_role(info, role_id, nombre=None, descripcion=None):
        role_entity = RoleService.repo.get_by_id(role_id)
        old_data = {"nombre": role_entity.nombre, "descripcion": role_entity.descripcion}
        if nombre: role_entity.nombre = nombre
        if descripcion: role_entity.descripcion = descripcion
        updated_role = RoleService.repo.update(role_entity)
        AuditService.log(
            info.context.user_id,
            "UPDATE",
            "Roles",
            updated_role.id,
            detalles={"antes": old_data, "despues": {"nombre": updated_role.nombre, "descripcion": updated_role.descripcion}}
        )
        return updated_role

    @staticmethod
    def delete_role(info, role_id):
        role_entity = RoleService.repo.get_by_id(role_id)
        old_data = {"nombre": role_entity.nombre, "descripcion": role_entity.descripcion}
        RoleService.repo.delete(role_id)
        AuditService.log(
            info.context.user_id,
            "DELETE",
            "Roles",
            role_id,
            detalles=old_data
        )

    @staticmethod
    def list_roles():
        return RoleService.repo.list()
