from typing import Dict
from storage import Storage
from storage_factory import StorageFactory

class StorageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls)
            cls._instance.storage_map: Dict[str, Storage] = {}
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_user_storage(self, user_id: str, storage_type: str) -> None:
        storage = StorageFactory.get_storage(storage_type)
        self.storage_map[user_id] = storage

    def get_user_storage(self, user_id: str) -> Storage:
        return self.storage_map.get(user_id)
