# OOPS is used to build real world complex applications like shopping app, instagram , fb, banking site

# The following code allows us to purchase different products.
# All products have 10% of discount

def purchase_product(product_type, price):
    discount = 10
    total_price = price - price * discount / 100
    return "Total price of " + product_type + " is "+str(total_price)


print(purchase_product("Mobile", 20000))
print(purchase_product("Shoe", 200))

###################################################################################################################################################

# Now I want to update our code such that:
# 1. if the mobile brand is Apple then the discount is 10% else the discount is 5%
# 2. all shoes have 2% tax and no discount
# We can do this by adding additional parameters to the function and updating the logic.


def purchase_product(product_type, price, mobile_brand=None):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 / 100

    print("Total price of " + product_type + " is "+str(total_price))


purchase_product("Mobile", 20000, "Apple")
purchase_product("Shoe", 200)

#####################################################################################################################################################

# The solution we came up with has a key problem.
# Data for mobiles and shoes are mixed up in the same code.
# If we have to make changes to the logic for purchasing shoes, we have to modify method that has logic for both shoes and mobiles.
# For example, if we have to add 'material' to the shoe and have a 5% tax on 'leather' shoes,
# then we have to go through code related to mobile as well, as shown below:


def purchase_product(product_type, price, mobile_brand, material):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price + price * tax / 100
    print("Total price of "+product_type+" is "+str(total_price))


purchase_product("Mobile", 20000, "Apple", None)
purchase_product("Shoe", 200, None, "leather")

##########################################################################################################################################################

# A better solution would be to modularize the code and separate the logic for Mobiles and Shoes.

# Modify the code in the below code pane as per the following guidelines:

# Create two functions: purchase_mobile and purchase_shoe
# purchase_mobile() takes two parameters: price and brand
# purchase_shoe() takes two parameters: price and material
# If the mobile brand is “Apple”, discount is 10%, else discount is 5%
# If the shoe material is “leather”, tax is 5%, else tax is 2%


def purchase_mobile(price, brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100

    print("Total price of Mobile is "+str(total_price))


def purchase_shoe(price, material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100

    print("Total price of Shoe is "+str(total_price))


purchase_mobile(20000, "Apple")
purchase_shoe(200, "leather")

#########################################################################################################################################################################

# Now We want to provide users with facility to return products as well.
# During return, refund amount should be displayed

# we can use global variables.
# We calculate the price during purchase and store it in a global variable.
# Later during return we access the calculated price from the global variable.
# But this brings more complications than it tries to solve.

total_price_mobile = 0
total_price_shoe = 0


def purchase_mobile(price, brand):
    global total_price_mobile
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print("Total price for Mobile is "+str(total_price_mobile))


def purchase_shoe(price, material):
    global total_price_shoe
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print("Total price for Shoe is "+str(total_price_shoe))


def return_mobile():
    print("Refund price for Mobile is ", total_price_mobile)


def return_shoe():
    print("Refund price for Shoe is ", total_price_shoe)


purchase_mobile(20000, "Apple")
purchase_shoe(200, "leather")
return_mobile()

##################################################################################################################################################################################################################

# What if we want to purchase two mobiles and return one of them? Which will be returned?
# Also, can we be sure that purchase_shoe() won't accidentally modify the global value for mobile?

# We can see that with our current style of programming, we quickly run into complications trying to simulate real world scenarios, like purchasing and returning a product.
# The problem arises due to the fact that in real life everything has some data/characteristic associated with it and some behavior associated with it and we are not able to replicate this in a code.
# For example:
# All mobiles have price and brand as its data and purchase and return as its behavior.
# All shoes have price and material as its data and purchase and return as its behavior.

# We need a way of programming which allows to club together the data and behavior so that it becomes easier to code real world scenarios.
# Once we have a template of the data and the related behavior we can use that template to create many copies.
# This style of programming where we create a template and create copies from that template is called object oriented programming.
# This style allows us to code for scenarios closely linked with real life.
# The template we create is called a Class and the copies we create out of it is called an object.
