#OOPS with python

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item_price_total = item1_price * item1_quantity

# print(type(item1))

# print(type(item1_price))


class item:
    # __init__ is a constructor
    # The __init__ function will run itself automatically
    #name:str makes the user to use string as mandatary
    def __init__(self,name:str,price:float,quantity = 0) -> None:
        # Run validations to the received arguments
        assert price >=0 , f"Price {price} should not be Negative"
        assert quantity >=0,  f"Quantity {quantity} should be Positive"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def myfun(self):
        return self.price * self.quantity
        

myItem = item("Car",3600,2)

second_item = item("Mobile", 29999, 3)

print(myItem.myfun())
print(second_item.myfun())
print(myItem.__dict__)
print(item.__dict__)
