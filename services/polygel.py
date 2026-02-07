from .service import Service

class PolygelTips(Service):
    def __init__(self):
        super().__init__("Polygel Tips", 95)

    def get_details(self):
        return f"{self.name} - Lightweight hybrid extensions (${self.price})"
