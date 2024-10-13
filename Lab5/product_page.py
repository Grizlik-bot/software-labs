from page import Page

class ProductPage(Page):
    def __init__(self, renderer, product) -> None:
        super().__init__(renderer)
        self.product = product

    def view(self) -> None:
        self.renderer.render_product_page(self.product)
