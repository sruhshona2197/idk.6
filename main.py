# 4
class FoodOrder:
    def __init__(self, food, price, is_delivered=False):
        self.food = food
        self.price = price
        self.is_delivered = is_delivered

    def deliver(self):
        self.is_delivered = True
        print("Buyurtma yetkazildi")

    def status(self):
        if self.is_delivered:
            print("Buyurtma yetkazildi")
        else:
            print("Hali yetkazilmadi")


# Test qilish
order1 = FoodOrder("Pizza", 50000)

order1.status()   
order1.deliver()
order1.status()
