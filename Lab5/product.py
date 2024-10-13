class Product:
    def __init__(self, name: str, description: str, img_url: str, product_id: int) -> None:
        self.name = name
        self.description = description
        self.img_url = img_url
        self.id = product_id
