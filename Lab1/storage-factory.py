from storage import Storage
from local_disk_storage import LocalDiskStorage
from amazon_s3_storage import AmazonS3Storage

class StorageFactory:
    @staticmethod
    def get_storage(storage_type: str) -> Storage:
        if storage_type.lower() == "local":
            return LocalDiskStorage()
        elif storage_type.lower() == "s3":
            return AmazonS3Storage()
        else:
            raise ValueError("Invalid storage type")
