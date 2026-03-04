import re
f = open("dicionario_medico.txt", "r", encoding="utf8")
texto = f.read()


texto = re.sub(r"\f", "", texto) 

texto = re.sub(r"\n\n", "\n\n@", texto) 

conceitos= re.split(r"\.\n\n@", texto) #so faz split quando encontrar um ponto final, 2 paragrafos e um @

def limpa_descricao(descricao): 
    descricao =re.sub(r"\n", " ", descricao)
    return descricao

# correção:
conceitos_dict={} 
i= False 
for conceito in conceitos[1:]: 
    elems= re.split(r"\n", conceito, maxsplit=1)
    if len(elems) > 1: 
        designacao= elems[0] 
        descricao =elems[1] 
        conceitos_dict[designacao]= limpa_descricao(descricao) 
    else: 
        if not i: 
            designacao = conceito 
            i = True 
        elif i: 
            descricao = conceito 
            conceitos_dict[designacao] = limpa_descricao(descricao) 
            i= False 
            
#print(conceitos_dict) 
print(len(conceitos_dict))

#---------------------------------------

#transformação do dicionario num ficheiro json
import json

def gera_json(filename, conceitos_dict):
    f_out= open(filename, "w", encoding="utf8")
    json.dump(conceitos_dict, f_out, indent=4, ensure_ascii=False)

gera_json("dicionario_medico.json", conceitos_dict)


#transformacao do dicionario num ficheiro html
def gera_html(filename, conceitos_dict):
    html='''
<html>
    <head>
    <title> Dicionário Médico </title>
    <meta charset="UTF-8"/>
    </head>
    <body>'''
    for c in conceitos_dict:
        html =html + f"""
        <div>
        <p><b> {c} </b></p>
        <p> {conceitos_dict[c]} </p>
        </div>
        <hr>
        """
    html= html + '''</body>
</html>
'''
    f_out= open(filename, "w", encoding="utf8")
    f_out.write(html)

gera_html("dicionario_medico.html", conceitos_dict)