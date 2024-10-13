from renderer import Renderer

class XMLRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> None:
        print(f"<page><title>{title}</title><content>{content}</content></page>")

    def render_product_page(self, product) -> None:
        print(f"<product><name>{product.name}</name><description>{product.description}</description><image>{product.img_url}</image><id>{product.id}</id></product>")
