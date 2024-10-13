from page import Page

class SimplePage(Page):
    def __init__(self, renderer, title: str, content: str) -> None:
        super().__init__(renderer)
        self.title = title
        self.content = content

    def view(self) -> None:
        self.renderer.render_simple_page(self.title, self.content)
