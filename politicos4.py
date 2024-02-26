import requests

gastos = {}

for x in range(1,44):

    url = "https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2023&ordem=ASC&ordenarPor=ano&pagina="+ str(x) + "&itens=15"
    dados = requests.get(url).json()
    


    for x in dados["dados"]:
        if x["nomeFornecedor"] not in gastos:
            gastos_att = {x["nomeFornecedor"]:x["valorDocumento"]}
            gastos.update(gastos_att)
        elif x["nomeFornecedor"] in gastos:
            gastos[x["nomeFornecedor"]] += x["valorDocumento"]
        

print(sorted(gastos.items(), key =lambda item: item[1], reverse=True))
