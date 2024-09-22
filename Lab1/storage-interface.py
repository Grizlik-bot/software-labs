from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def upload_file(self, file_path: str) -> None:
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> None:
        pass
