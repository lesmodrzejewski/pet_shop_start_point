# WRITE YOUR FUNCTIONS HERE

from ssl import get_protocol_name


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, cash_amount):
    total_cash["admin"]["total_cash"] += cash_amount
    
def get_pets_sold(total_pets_sold):
    return total_pets_sold["admin"]["pets_sold"]

def increase_pets_sold(total_pets_sold, increase_total_pets_sold_by):
    total_pets_sold["admin"]["pets_sold"] += increase_total_pets_sold_by

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(pets_by_bread, bread_name):
    total_pets_by_bread = []
    for pet in pets_by_bread["pets"]:
        if pet["breed"] == bread_name:
            total_pets_by_bread.append(bread_name)

    return total_pets_by_bread

def find_pet_by_name(pet_shop, given_pet_name): 

    for pet in pet_shop["pets"]:
        if pet["name"] == given_pet_name:
            return pet
    
    return None

def remove_pet_by_name(pet_shop_names, given_pet_name):
    
    for pet in pet_shop_names["pets"]:
        if pet["name"] == given_pet_name:
            pet["name"] = None
            return pet["name"]

def add_pet_to_stock(pet_shop_pets, new_pet):
    new_pets_list = pet_shop_pets["pets"]
    pet_shop_pets["pets"].append(new_pet)
    return len(new_pets_list)

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove
    return customer  

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet:
        customer["pets"].append(pet)
        pet_shop["admin"]["pets_sold"] += 1
        customer["cash"] -= pet["price"]
        pet_shop["admin"]["total_cash"] += pet["price"]

    else:
        return




