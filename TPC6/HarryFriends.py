import spacy
from spacy.pipeline import EntityRuler
import json
file= open("Harry Potter e A Pedra Filosofal.txt", "r", encoding="UTF-8")
texto =file.read()

nlp = spacy.load("pt_core_news_sm")


ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "Pessoa", "pattern": [{"LOWER": "harry"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "potter"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "harry"}, {"LOWER": "potter"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "rony"}]},
    #{"label": "Pessoa", "pattern": [{"LOWER": "ronald"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "rony"}, {"LOWER": "weasley"}]},
    #{"label": "Pessoa", "pattern": [{"LOWER": "ronald"}, {"LOWER": "weasley"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "hermione"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "hermione"}, {"LOWER": "granger"}]}]
'''
    
    {"label": "Pessoa", "pattern": [{"LOWER": "dumbledore"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "alvo"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "alvo"}, {"LOWER": "dumbledore"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "mcgonagall"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "minerva"}, {"LOWER": "mcgonagall"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "snape"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "severo"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "hagrid"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "rúbeo"}]},

    {"label": "Pessoa", "pattern": [{"LOWER": "draco"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "malfoy"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "draco"}, {"LOWER": "malfoy"}]},

    {"label": "Pessoa", "pattern": [{"LOWER": "neville"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "longbottom"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "neville"}, {"LOWER": "longbottom"}]}]
 
    {"label": "Pessoa", "pattern": [{"LOWER": "quirrell"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "filch"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "binns"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "flitwick"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "hooch"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "sprout"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "pomfrey"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "potter"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "lílian"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "tiago"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "sr."}, {"LOWER": "dursley"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "sra."}, {"LOWER": "dursley"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "dursley"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "dudley"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "duda"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "válter"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "petúnia"}]},
    
    {"label": "Pessoa", "pattern": [{"LOWER": "voldemort"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "tom"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "crabbe"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "goyle"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "gina"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "fred"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "percy"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "seamus"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "finnigan"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "parvati"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "patil"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "pansy"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "parkinson"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "pansy"}, {"LOWER": "parkinson"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "zabini"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "nott"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "sirius"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "figg"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "diggle"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "flamel"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "nicolau"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "nick"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "edwiges"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "norberto"}]}
]'''

ruler.add_patterns(patterns)

hp = nlp(texto)

pessoas=[]
for ent in hp.ents:
    if ent.label_ == "Pessoa":
        if ent.text not in pessoas:
            pessoas.append(ent.text)

print(pessoas)


amigos={}
for pessoa in pessoas:
    amigos[pessoa]={}
    for sent in hp.sents:
        nome_sent=[ent.text for ent in sent.ents if ent.label_ == "Pessoa"] #vai buscar todas as entidades da frase e filtra apenas aquelas que forem Pessoa
        if pessoa in nome_sent:
            for amigo in nome_sent:
                if amigo != pessoa:
                    amigos[pessoa][amigo] = amigos[pessoa].get(amigo, 0) + 1 #inicializa como 0 e depois adiciona 1 caso ainda não exista


normalizacao = {
    "Harry": "Harry Potter",
    "HARRY POTTER": "Harry Potter",
    "POTTER": "Harry Potter",
    "Potter": "Harry Potter",
    
    "Rony": "Rony Weasley",
    
    "Hermione": "Hermione Granger",
    "Granger": "Hermione Granger"
}

amigos_normalizado = {}

for pessoa, relacoes in amigos.items():
    pessoa_norm = normalizacao.get(pessoa, pessoa)
    
    if pessoa_norm not in amigos_normalizado:
        amigos_normalizado[pessoa_norm] = {}
    
    for amigo, n_ocorrencias in relacoes.items():
        amigo_norm = normalizacao.get(amigo, amigo)
        
        if amigo_norm != pessoa_norm:
            amigos_normalizado[pessoa_norm][amigo_norm] = amigos_normalizado[pessoa_norm].get(amigo_norm, 0) + n_ocorrencias

f_out= open("HarryFriends.json", "w", encoding="UTF-8")
json.dump(amigos_normalizado,f_out, indent=4, ensure_ascii= False)
f_out.close()