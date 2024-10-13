from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_simple_page(self, title: str, content: str) -> None:
        pass

    @abstractmethod
    def render_product_page(self, product) -> None:
        pass
