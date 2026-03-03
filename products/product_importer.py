import csv


class ProductImporter:
    """
    Utility class dedicated solely to reading files and importing
    product data into the system.
    """
    
    @staticmethod
    def import_from_file(file_path: str) -> int:
        """
        Reads a CSV file and imports products into the system.
        Returns the number of products imported.
        """
        products_imported = 0
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None) # Skip header if present

                for row in reader:
                    # Defensive programming: ensure the row has exactly 3 columns
                    if len(row) != 3:
                        print(f"⚠️ Skipping malformed line: {row}")
                        continue
                    
                    name, price_str, stock_str = row
                    try:
                        price = float(price_str)
                        stock = int(stock_str)
                        # Here you would create a Product instance and add it to your system
                        # e.g., product = Product(name, price, stock)
                        products_imported += 1
                    except ValueError as ve:
                        print(f"⚠️ Skipping line with invalid data types: {row} ({ve})")
                        
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
        except Exception as e:
            print(f"❌ An error occurred while importing products: {e}")
        
        return products_imported