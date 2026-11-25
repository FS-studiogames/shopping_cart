# the cart is a dictionary that looks like this:

# {"Apple": {"price": 0.5, "quantity": 3}, "Milk": {"price": 1.2, "quantity": 1}}

# add_item(cart, name, price, quantity) adds the item to the cart. If it's already there, it increases the quantity instead. Returns nothing.

# remove_item(cart, name) deletes the item if it's in the cart. Returns nothing.

# show_cart(cart) returns a list of text lines, like ["Apple x3 $1.50"]. It must return the list, not print it, or the cart box stays empty.

# total_price(cart) returns the total as a number.
.
.
.
.
.
.
.
def add_item(cart, name, price, quantity)
    if name in cart.values():
        cart[quantity] = quantity +1
        cart[price] = price * quantity 

def remove_item(cart, name):
       del cart[name]

def show_cart(cart):
        new_list = ["{cart[name]} x{cart[quantity]} ${cart[price]}"]
return(new_list)

def total_price(cart):
total = 0
        for i in cart.values():
               not_total_still = sum(i[price]) 
               not_total_still += total
      return total