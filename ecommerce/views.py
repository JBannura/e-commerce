from django.shortcuts import render

def test(request):
    data_file = open('C:/Users/Usuario/Desktop/PUCRS/5 Semestre/e-commerce/ecommerce/test.txt', 'r')
    data = data_file.read()
    context = {'ecommerce': data}
    return render(request, 'C:/Users/Usuario/Desktop/PUCRS/5 Semestre/e-commerce/ecommerce/templates/test.html',context)