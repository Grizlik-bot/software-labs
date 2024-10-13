from renderer import Renderer

class JSONRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> None:
        print(f'{{"title": "{title}", "content": "{content}"}}')

    def render_product_page(self, product) -> None:
        print(f'{{"name": "{product.name}", "description": "{product.description}", "image": "{product.img_url}", "id": {product.id}}}')
