from django.shortcuts import render
import utils
from . import models

def request_page(request):
    #print(f"Request: {request}")
    store = 'Empty'
    if request.method == 'POST':
        store = request.POST.getlist('commerce')
    
    if store != 'Empty' and len(store) > 0:
        models.add_pedido(store[0])
        
    return render(request, 'D:/Desktop/Pucrs/2020_2/ProjArq/MVC-django/e-commerce/ecommerce/templates/register.html')

def test(request_):
    data_file = open('C:/Users/Usuario/Desktop/PUCRS/5 Semestre/e-commerce/ecommerce/test.txt', 'r')
    data = data_file.read()
    context = {'ecommerce': data}
    return render(request_, 'C:/Users/Usuario/Desktop/PUCRS/5 Semestre/e-commerce/ecommerce/templates/test.html',context)