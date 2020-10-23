import json

def mount_data():
    
    with open('ecommerce/data/data.json') as json_file:
        data = json.load(json_file)
    
    return data

def add_pedido(store):

    data = mount_data()
    
    print(data[store])