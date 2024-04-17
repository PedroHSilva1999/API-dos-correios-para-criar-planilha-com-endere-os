import requests
import json
import csv


cep = input("Informe o cep: \n")
cep_formatado = cep.replace("-","")
url = f"https://viacep.com.br/ws/{cep_formatado}/json/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rua = data['logradouro']
    bairro =data['localidade']
    cidade = data['bairro']
    estado = data['uf']
    cep = data['cep']
    
with open("Endereços.csv", "w") as enderecos:
    writer = csv.writer(enderecos)
    writer.writerow([rua,bairro,cidade , estado,cep])


