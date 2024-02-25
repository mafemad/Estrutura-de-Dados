import requests

url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
dados = requests.get(url).json()

for x in dados["dados"]:
    if x["siglaPartido"] == "PL" and x["siglaUf"] == "SP" or x["siglaPartido"] == "PT" and x["siglaUf"] == "MA":
        url_imagem = x["urlFoto"]
        imagem = requests.get(url_imagem)
        nome_arquivo = x["nome"] + ".jpg"
        with open(nome_arquivo, "wb") as arquivo:
            arquivo.write(imagem.content)
        
