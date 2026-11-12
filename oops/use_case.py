# ABC Mart has made its service online for few of the products available in the mart by providing additional online discount and with a feature of shipping the order to the customers through courier.
# The process of calculation of the order price and shipping the order request to customer and providing them tracking id process has to be automated.

class Mart:
    item_name_list = ["Chocolate", "Perfume", "Bouquet", "Apparel"]
    item_price_list = [200, 400, 150, 300]
    item_quantity_list = [10, 20, 30, 40]

    def find_price_per_item(self, item_name):
        if item_name in Mart.item_name_list:
            index = Mart.item_name_list.index(item_name)
            return Mart.item_price_list[index]
        return -1


class OnlineMart(Mart):
    def __init__(self, order):
        self.__online_discount_percentage = None
        self.__order = order

    def identify_online_discount(self):
        if self.__order.get_payment_mode() == 'Prepaid':
            self.__online_discount_percentage = 5
        elif self.__order.get_payment_mode() == 'COD':
            self.__online_discount_percentage = 2
        else:
            self.__online_discount_percentage = -1

    def get_order(self):
        return self.__order

    def find_price_per_item(self, item_name):
        price = super().find_price_per_item(item_name)
        if price != -1:
            self.identify_online_discount()
            if self.__online_discount_percentage != -1:
                price = price - \
                    (price * (self.__online_discount_percentage/100))
                return price
        return -1

    def check_item_availability(self):
        if self.__order.get_item_name() in Mart.item_name_list:
            index = Mart.item_name_list.index(self.__order.get_item_name())
            if self.__order.get_quantity_required() <= Mart.item_quantity_list[index]:
                Mart.item_quantity_list[index] -= self.__order.get_quantity_required()
                return self.__order.get_quantity_required()
        return -1

    def ship_order(self):
        quantity = self.check_item_availability()
        price_per_item = self.find_price_per_item(self.__order.get_item_name())

        if quantity == -1 or price_per_item == -1:
            self.__order.set_order_price(-1)
            self.__order.set_tracking_id("NA")
        else:
            self.__order.set_order_price(quantity * price_per_item)
            self.__order.set_tracking_id(self.__order.generate_tracking_id())


class Order:
    __counter = 1000

    def __init__(self, item_name, quantity_required, payment_mode):
        self.__tracking_id = None
        self.__item_name = item_name
        self.__quantity_required = quantity_required
        self.__payment_mode = payment_mode
        self.__order_price = None

    def get_tracking_id(self):
        return self.__tracking_id

    def set_tracking_id(self, tracking_id):
        self.__tracking_id = tracking_id

    def get_item_name(self):
        return self.__item_name

    def get_quantity_required(self):
        return self.__quantity_required

    def get_payment_mode(self):
        return self.__payment_mode

    def get_order_price(self):
        return self.__order_price

    def set_order_price(self, order_price):
        self.__order_price = order_price

    def generate_tracking_id(self):
        Order.__counter += 1
        return f"TR{Order.__counter}"


# You may modify the below code for testing
order_obj = Order('Bouquet', 20, 'Prepaid')
online_mart_object = OnlineMart(order_obj)
online_mart_object.ship_order()
print('Tracking ID :', online_mart_object.get_order().get_tracking_id())
print('Order Price :', online_mart_object.get_order().get_order_price())
