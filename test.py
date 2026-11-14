class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        self.items.pop(item_name, None)

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание магазинов
store1 = Store("Фруктовый рай", "ул. Ленина, 10")
store2 = Store("У дома", "пр. Мира, 25")
store3 = Store("ЭкоМаркет", "ул. Садовая, 5")

store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.2)
store2.add_item("bread", 0.8)

store3.add_item("avocado", 2.5)
store3.add_item("mango", 3.0)

# Тестирование методов на первом магазине
store1.add_item("oranges", 1.1)
store1.update_price("apples", 0.6)
store1.remove_item("bananas")

print("Цена яблок:", store1.get_price("apples"))
print("Цена бананов:", store1.get_price("bananas"))
