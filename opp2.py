from abc import ABC, abstractmethod

# Принцип SRP: клас має лише одну відповідальність — зберігати дані про замовлення
class Order:
    def __init__(self, items):
        self.items = items  # список кортежів (назва, ціна)

    def total_price(self):
        return sum(price for name, price in self.items)

# Принцип OCP: клас може розширюватися новими типами виводу без зміни існуючого коду
class Printer(ABC):
    @abstractmethod
    def print(self, order: Order):
        pass

class ConsolePrinter(Printer):
    def print(self, order: Order):
        print("Список замовлення:")
        for name, price in order.items:
            print(f"- {name}: {price} грн")
        print(f"Загальна сума: {order.total_price()} грн")

class FilePrinter(Printer):
    def print(self, order: Order):
        with open("order.txt", "w") as f:
            f.write("Список замовлення:\n")
            for name, price in order.items:
                f.write(f"- {name}: {price} грн\n")
            f.write(f"Загальна сума: {order.total_price()} грн\n")

# Використання
if __name__ == "__main__":
    items = [("Піца", 200), ("Сік", 50), ("Десерт", 70)]
    order = Order(items)

    printer = ConsolePrinter()
    printer.print(order)
