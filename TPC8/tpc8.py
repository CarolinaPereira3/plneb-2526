from flask import Flask, render_template, request
import json
import re
#parent template
#o conteudo da pagina principal e esta, mas dependendo da pagina em que estou pode mudar
#parent tem o conteudo comum que quero que aparecam em todas as paginas

app = Flask(__name__)

f_db =open("dicionario_medico.json", "r", encoding="UTF-8") #vem da aula 3
db= json.load(f_db)

@app.get("/")
def home_page():
    return render_template("home.html")

@app.get("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos= db.keys())

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao= db[designacao]
        return render_template("conceito.html", designacao = designacao, descricao= descricao)
    else:
        return render_template("erro.html", erro="O conceito itroduzido nao existe")
    
@app.post("/conceitos")
def adicionar_conceito(): #query string quando tem ? e passo informacao ao proprio url; nao se deve passar info sensivel na query string que fica visivel
    #form pode ser post ou get;se for um get passa a informacao pela query string (podes testar mudando o methodo do forma adicionar conceito para get)
    descricao= request.form["descricao"]#form funciona como um dicionario de todos os elementos que passamos(designacao e descricao ), passamos lhe o que pussemos no name
    designacao= request.form["designacao"]
    db[designacao]= descricao
    #fazer json dumb porque se a aplicacao for abaixo a memoria apagasse e ficamos sem esse novo conceitos, portanto adicionamos tambem no ficheiro
    f_out=open("db.json", "w", encoding="utf-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return render_template("conceitos.html", conceitos=db.keys())

@app.delete("/conceitos/<designacao>")
def apagar_conceito(designacao):
    del db[designacao]
    f_out=open("db.json", "w", encoding="utf-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return {"redirect_url": "/conceitos", "message": "Conceito apagado com sucesso!"}

@app.get("/tabela")
def tabela():
    return render_template("tabela.html", conceitos= db)

@app.get("/pesquisar")
def pesquisar():
    return render_template("pesquisar.html")

@app.post("/pesquisar")
def pesquisar_post():
    res=[]
    termo=request.form["termo"]
    caseSensitive= request.form.get("caseSensitive") == "on"
    wordBoundary= request.form.get("wordBoundary") == "on"
    for designacao, descricao in db.items():
        conceito= f"{designacao} - {descricao}"


        if wordBoundary:
            pattern = rf"\b{re.escape(termo)}\b"
            if caseSensitive:
                match = re.search(pattern, conceito)
            else:
                match = re.search(pattern, conceito, re.IGNORECASE)
        else:
            pattern = re.escape(termo)
            if caseSensitive:
                match = re.search(pattern, conceito)
            else:
                match = re.search(pattern, conceito, re.IGNORECASE)

        if match:
            if caseSensitive:
                res_negrito = re.sub(pattern, f"<b>{termo}</b>", conceito)
            else:
                res_negrito = re.sub(pattern,  lambda m: f"<b>{m.group()}</b>", conceito, flags=re.IGNORECASE) #m.goup() dá aquilo que foi encontrado com o case correspondente

            res.append(res_negrito)
    
    return render_template("pesquisar.html", res=res)

#rotas de api- sao rotas para servidores falarem entre si
@app.get("/api/conceitos")
def conceitos_api():

    return db

app.run(host="localhost", port=4002, debug= True) #debug true podemos alterar o codigo sem tar sempre a ligar e desligar o servidor