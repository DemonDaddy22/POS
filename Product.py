class Product:
    def __init__(self,name,qty):
        self.name = name
        self.quantity = qty

    @property
    def getName(self):
        return self.name

    """@property
    def getPrice(self):
        return self.price"""

    @property
    def getQty(self):
        return self.quantity

    