"""
Analogy:
Factory -> Creates and returns Objects.
"""

"""
Understand the business Problem:
===============================

You are building an e-commerce application which supports Three Payment Gateways.
1. RazorPay
2. Stripe
3. PayPal

Requirement:
============
1. Indian customers use RazorPay
2. International customers use Stripe
3. Some Users use Paypal.

A customer buys a product worth Rs. 5000
Your backend must select the correct payment gateway based on the payment method.
"""

# Initial Code
def process_payment(payment_method, amount):
    if payment_method == "stripe":
        # Stripe Payment Processing logic
        print("Processing payment through Stripe")
    
    elif payment_method == "razorpay":
        # RazorPay Payment Processing logic
        print("Processing payment through RazorPay")

    elif payment_method == "paypal":
        # Paypal Payment Processing logic
        print("Processing payment through Paypal")

    else:
        raise ValueError("Invalid Payment Method.")


# But, after fewdays you want to add 10 more payment gateways.
# Then what will you do?
# writing if-else statements? soon, the function becomes difficult to maintain.

# Problems we have?
# 1. Too many responsibilities: 
#       The process_payment() function decides which gateway to use and also contains payment-processing logic.
# 2: Difficult to extend:
#       Whenever a new gateway is introduced, we modify the existing function.
# 3: Tight coupling:
#       Your business logic knows about Razorpay, Stripe and PayPal implementations.
# 4: Difficult to test:
#       Testing payment selection and individual gateway implementations together becomes harder.


# This is where the Factory Pattern becomes useful.

"""
What is Factory Pattern?
Factory Pattern is a creational design pattern that centralizes object creation and 
returns the appropriate object based on the input or requirement.

Let's understand that in simple terms.

Imagine a restaurant.

You don't go into the kitchen and prepare a pizza yourself. You tell the waiter what you want.
- You request Pizza → Kitchen prepares Pizza.
- You request Burger → Kitchen prepares Burger.
- You request Pasta → Kitchen prepares Pasta.
The kitchen decides which object to create.

In software:
- You request Razorpay → Factory creates a Razorpay payment object.
- You request Stripe → Factory creates a Stripe payment object.
- You request PayPal → Factory creates a PayPal payment object.
"""

# Designing/Refactoring our Logic to Factory Method

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RazorPay(PaymentGateway):
    def process_payment(self, amount):
        # RazorPay Logic
        print("Processing Payment through RazorPay.")

class Stripe(PaymentGateway):
    def process_payment(self, amount):
        # Stripe Logic
        print("Processing Payment through Stripe.")

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        # PayPal Logic
        print("Processing Payment through PayPal.")

# Factory Class to create a Factory
class PaymentFactory():
    @staticmethod
    def get_payment_method(method):
        if method == "razorpay":
            return RazorPay()
        elif method == "stripe":
            return Stripe()
        elif method == "paypal":
            return PayPal()
        else:
            raise ValueError("Unsupported payment method")

# Instead of using mulitple if-else, we can also improve this by adding a registry

class PaymentFactoryImproved():
    _gateways = {
        "razorpay": RazorPay,
        "stripe": Stripe,
        "paypal": PayPal
    }

    @classmethod
    def get_payment_method(cls, method):
        gateway_class = cls._gateways.get(method)
        if gateway_class is None:
            raise ValueError("Unsupported payment method")
        return gateway_class



# Actual Business Logic
def checkout(amount, payment_method):
    gateway = PaymentFactory.get_payment_method(payment_method)
    gateway.process_payment(amount)


checkout("razorpay", 5000)
checkout("stripe", 3000)
checkout("paypal", 2000)
