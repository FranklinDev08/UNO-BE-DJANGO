from abc import ABC, abstractmethod

class RoleRepositoryInterface(ABC):
    @abstractmethod
    def create(self, role_entity):
        pass

    @abstractmethod
    def update(self, role_entity):
        pass

    @abstractmethod
    def delete(self, role_id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def get_by_id(self, role_id):
        pass
