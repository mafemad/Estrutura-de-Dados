import requests

url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
dados = requests.get(url).json()

for x in dados["dados"]:
    if x["siglaPartido"] == "PL" and x["siglaUf"] == "SP" or x["siglaPartido"] == "PT" and x["siglaUf"] == "MA":
        print(x["nome"] + "-" + x["siglaPartido"])