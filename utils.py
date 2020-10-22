
def teste(texto):
    print(texto)

def test_json():
    import json

    with open('ecommerce/data/data.json') as json_file:
        data = json.load(json_file)

    for loja in data:
        
        #print(data[loja])
        
        for loja_info in data[loja]:
            
            if loja_info == 'loja':
                print(f"\nLoja: {data[loja][loja_info]}")
            
            elif loja_info == 'pedidos':
                for item in data[loja][loja_info]:
                    for idx, dados in enumerate(data[loja][loja_info][item]):
                        
                        if idx == 0:
                            print(f"Nome do produto : {dados}")
                        
                        elif idx == 1:
                            print(f"Valor do produto: {dados}")    

if __name__ == "__main__":
    test_json()
                

  