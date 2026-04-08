from flask import Flask, render_template, request
import json
import unicodedata
#parent template
#o conteudo da pagina principal e esta, mas dependendo da pagina em que estou pode mudar
#parent tem o conteudo comum que quero que aparecam em todas as paginas

app = Flask(__name__)

f_db =open("dicionario_medico.json", "r", encoding="UTF-8") #vem da aula 3
db= json.load(f_db)


#funcao que retorna palavras sem acentos
def remover_acentos(texto):
    # Normaliza e remove diacríticos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

@app.get("/")
def home_page():
    return render_template("home.html")

@app.get("/conceitos") #/conceitos?letra=X
def listar_conceitos():
    letra= request.args.get("letra")
    conceitos_filtrados=[]
    if letra:                                               #se pedir letra os conceitos que aparecem sao apenas os começados por essa letra, senao sao todos
        for conceito in db.keys():
            if remover_acentos(conceito.upper()).startswith(letra.upper()): #permite que palavras que comecem com acentos tambem sejam incluidas
                conceitos_filtrados.append(conceito)
    else: 
        conceitos_filtrados= db.keys()
    return render_template("conceitos.html", conceitos= conceitos_filtrados)

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao= db[designacao]
        return render_template("conceito.html", designacao = designacao, descricao= descricao)
    else:
        return render_template("erro.html", erro="O conceito itroduzido nao existe")

#rotas de api- sao rotas para servidores falarem entre si
@app.get("/api/conceitos")
def conceitos_api():
    return db

app.run(host="localhost", port=4002, debug= True) #debug true podemos alterar o codigo sem tar sempre a ligar e desligar o servidor



