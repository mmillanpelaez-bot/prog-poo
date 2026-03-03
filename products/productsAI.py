from dataclasses import dataclass
from typing import Dict, List, Optional


# ==========================================
# 1. DOMAIN MODELS (El objeto que vamos a gestionar)
# ==========================================

@dataclass
class Product:
    """
    Represents a product in the warehouse.
    Using @dataclass automatically generates the __init__, __repr__, and __eq__ methods!
    """
    sku: str  # Stock Keeping Unit (Unique ID, like 'LAP-001')
    name: str
    price: float
    quantity: int = 0  # Default value is 0 if not provided

    @property
    def total_value(self) -> float:
        """Calculates the total monetary value of this product in stock."""
        return self.price * self.quantity

    def add_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount to add must be greater than zero.")
        self.quantity += amount

    def remove_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount to remove must be greater than zero.")
        if amount > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. Current: {self.quantity}, Requested: {amount}")
        self.quantity -= amount


# ==========================================
# 2. BUSINESS LOGIC (El gestor del almacén)
# ==========================================

class Warehouse:
    """Manages the inventory, keeping track of all products."""

    def __init__(self, name: str):
        self.name: str = name
        # Usamos un diccionario con el SKU como clave para búsquedas instantáneas O(1)
        self._inventory: Dict[str, Product] = {}

    def add_new_product(self, product: Product) -> None:
        if product.sku in self._inventory:
            raise ValueError(f"Product with SKU '{product.sku}' already exists.")
        self._inventory[product.sku] = product

    def get_product(self, sku: str) -> Optional[Product]:
        return self._inventory.get(sku)

    def get_all_products(self) -> List[Product]:
        return list(self._inventory.values())

    def get_total_warehouse_value(self) -> float:
        """Returns the total monetary value of all items in the warehouse."""
        return sum(product.total_value for product in self.get_all_products())

    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:
        """Returns a list of products that have a stock level at or below the threshold."""
        # Clean Code: Usar 'List Comprehensions' es la forma más "Pythonic" de filtrar listas
        return [p for p in self.get_all_products() if p.quantity <= threshold]


# ==========================================
# 3. USER INTERFACE (Interacción con el usuario)
# ==========================================

class WarehouseCLI:
    """Command Line Interface for the Warehouse."""

    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse

    def print_menu(self):
        print(f"\n📦 --- {self.warehouse.name.upper()} MANAGEMENT SYSTEM ---")
        print("1. Add a new product catalog entry")
        print("2. Receive stock (Incoming)")
        print("3. Dispatch stock (Outgoing)")
        print("4. View full inventory")
        print("5. View low stock alerts")
        print("6. Exit")
        print("-" * 40)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Select an operation (1-6): ").strip()

            try:
                match choice:
                    case "1":
                        sku = input("Enter SKU (e.g., ITM-001): ").strip().upper()
                        name = input("Enter product name: ").strip()
                        price = float(input("Enter unit price: "))

                        new_product = Product(sku, name, price)
                        self.warehouse.add_new_product(new_product)
                        print(f"✅ Product '{name}' added to catalog.")

                    case "2":
                        sku = input("Enter SKU to receive stock: ").strip().upper()
                        product = self.warehouse.get_product(sku)
                        if product:
                            amount = int(input(f"Enter amount to add to '{product.name}': "))
                            product.add_stock(amount)
                            print(f"✅ Stock updated. New quantity: {product.quantity}")
                        else:
                            print(f"❌ SKU '{sku}' not found.")

                    case "3":
                        sku = input("Enter SKU to dispatch: ").strip().upper()
                        product = self.warehouse.get_product(sku)
                        if product:
                            amount = int(input(f"Enter amount to dispatch for '{product.name}': "))
                            product.remove_stock(amount)
                            print(f"✅ Stock dispatched. Remaining quantity: {product.quantity}")
                        else:
                            print(f"❌ SKU '{sku}' not found.")

                    case "4":
                        print("\n📋 CURRENT INVENTORY:")
                        products = self.warehouse.get_all_products()
                        if not products:
                            print("The warehouse is currently empty.")
                        else:
                            print(f"{'SKU':<10} | {'NAME':<15} | {'PRICE':<8} | {'QTY':<5} | {'TOTAL VAL'}")
                            print("-" * 55)
                            for p in products:
                                print(
                                    f"{p.sku:<10} | {p.name:<15} | ${p.price:<7.2f} | {p.quantity:<5} | ${p.total_value:.2f}")
                            print("-" * 55)
                            print(f"TOTAL WAREHOUSE VALUE: ${self.warehouse.get_total_warehouse_value():.2f}")

                    case "5":
                        limit = int(input("Enter low stock threshold (default is 5): ") or 5)
                        low_stock = self.warehouse.get_low_stock_products(limit)
                        print(f"\n⚠️ LOW STOCK ALERTS (<= {limit} units):")
                        if not low_stock:
                            print("All products are well stocked.")
                        else:
                            for p in low_stock:
                                print(f"- {p.name} (SKU: {p.sku}): Only {p.quantity} left!")

                    case "6":
                        print("Exiting Warehouse Management System. Goodbye! 👋")
                        break

                    case _:
                        print("❌ Invalid option. Please choose a number between 1 and 6.")

            except ValueError as e:
                # Captura errores de conversión (ej. meter letras en el precio) y de nuestra lógica
                print(f"⚠️ Input/Logic Error: {e}")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")


# ==========================================
# 4. MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Inicializamos el sistema
    my_warehouse = Warehouse("Vigo Central Logistics")

    # Añadimos unos datos de prueba para que no empiece vacío
    my_warehouse.add_new_product(Product("LAP-01", "Laptop Pro", 999.99, 10))
    my_warehouse.add_new_product(Product("MOU-05", "Wireless Mouse", 25.50, 4))
    my_warehouse.add_new_product(Product("KEY-02", "Mechanical Keyboard", 85.00, 15))

    # Lanzamos la interfaz
    app = WarehouseCLI(my_warehouse)
    app.run()