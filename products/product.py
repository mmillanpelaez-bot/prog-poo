class Product:
    def __init__(self, name: str, price: float, stock: int):
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    def __str__(self) -> str:
        return f"{self._name} - Price: ${self._price}, Stock: {self._stock}"
