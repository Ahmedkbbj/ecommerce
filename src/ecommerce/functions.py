from .models import Product

def pack(_list):
    item = []
    new_list = []
    i=0
    for l in _list:
        i+=1
        if len(item) < 3:
            item.append(l)
    
        if len(item) == 3 :
            new_list.append(tuple(item))
            item = []
            
    return new_list


def search_products(search, products):
    products = products.filter(name__contains=search)
    if products.exists():
        return products
    else:
        return None

