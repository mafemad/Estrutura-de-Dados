import requests

total_gasto = 0

for x in range(1,44):

    url = "https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2023&ordem=ASC&ordenarPor=ano&pagina="+ str(x) + "&itens=15"
    dados = requests.get(url).json()

    for y in dados["dados"]:
        total_gasto += y["valorDocumento"]

print(f'total gasto por tabata do amaral: {total_gasto: .2f}')