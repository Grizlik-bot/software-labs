from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self, renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def view(self) -> None:
        pass
