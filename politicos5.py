import requests
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


nltk.download('stopwords')

nltk.download('punkt')


discursos = {}
pontuacao = string.punctuation + "''" + "``"

for x in range(1,5):

    url = "https://dadosabertos.camara.leg.br/api/v2/deputados/209787/discursos?dataInicio=2022-12-31&dataFim=2026-12-31&ordenarPor=dataHoraInicio&ordem=ASC&pagina="+ str(x) +"&itens=15"
    dados = requests.get(url).json()

    for x in dados["dados"]:
        cont = 0 
        texto = x["transcricao"]
        token = word_tokenize(texto)
        stop_words = set(stopwords.words('portuguese'))
        texto_sem_prep = [palavra for palavra in token if palavra.lower() not in stop_words and palavra.lower() not in pontuacao]
        for z in texto_sem_prep:
            if z not in discursos:
                cont = 1
                discursos_att = {z:cont}
                discursos.update(discursos_att)
            elif z in discursos:
                discursos[z] += 1
                
        

print(sorted(discursos.items(), key =lambda item: item[1], reverse=True))