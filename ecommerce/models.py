import json
#import pandas as pd
from django.shortcuts import render

def mount_data():
    
    with open('D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/data/data.json') as json_file:
        data = json.load(json_file)
    
    return data

def add_pedido(store):

    data = mount_data()
    print(data[store])

def store_report(request):
    data = mount_data()
    
    store_list = []
    for store in data:
        for info_loja in data[store]:        
            if info_loja == 'pedidos':
                for pedido in data[store][info_loja]:
                    nome_loja = data[store]['loja']
                    #print(f'Loja: {nome_loja} -- Produto: {data[store][info_loja][pedido][0]} Preço: {data[store][info_loja][pedido][1]} Data de Entrega: {data[store][info_loja][pedido][2]}')
                    store_list.append((nome_loja, data[store][info_loja][pedido][0], float(data[store][info_loja][pedido][1]), data[store][info_loja][pedido][2]))
    
    with open('D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/reports/sorted_by_store.txt', 'w') as sorted_w:
        for item in store_list:
            sorted_w.write("Loja: " + item[0] + " Produto: " + item[1] + " Preco: " + str(item[2]) + " Data: " + item[3] + "\n")

    return render(None, 'D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/templates/report.html')

def date_report(request):
    #print("date")
    data = mount_data()
    
    return render(None, 'D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/templates/report.html')

def price_report(request):
    #print("price")
    data = mount_data()
    
    price_list = []
    for store in data:
        for info_loja in data[store]:        
            if info_loja == 'pedidos':
                for pedido in data[store][info_loja]:
                    nome_loja = data[store]['loja']
                    #print(f'Loja: {nome_loja} -- Produto: {data[store][info_loja][pedido][0]} Preço: {data[store][info_loja][pedido][1]} Data de Entrega: {data[store][info_loja][pedido][2]}')
                    price_list.append((nome_loja, data[store][info_loja][pedido][0], float(data[store][info_loja][pedido][1]), data[store][info_loja][pedido][2]))
    
    price_list.sort(key=lambda tup: tup[2])
    
    with open('D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/reports/sorted_by_price.txt', 'w') as sorted_w:
        for item in price_list:
            sorted_w.write("Loja: " + item[0] + " Produto: " + item[1] + " Preco: " + str(item[2]) + " Data: " + item[3] + "\n")
    
    return render(None, 'D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/templates/report.html')    
if __name__ == "__main__":
    
    store_report()
    #date_report()
    price_report()