from renderer import Renderer

class HTMLRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> None:
        print(f"Render simple HTML page: title='{title}', content='{content}'")

    def render_product_page(self, product) -> None:
        print(f"Render product HTML page: name='{product.name}', description='{product.description}', image='{product.img_url}', id={product.id}")
