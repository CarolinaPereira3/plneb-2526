#TF-idf
import spacy
import math

raw_collection= ["The sky is blue",
              "The sun is bright",
              "The sun in the sky"]



nlp = spacy.load("en_core_web_sm")

#tpc fazer o pre_processamento, remover stop words, pontuacao, tokenizar
def pre_processamento(collection):
    new_collection=[]
    for d in collection:
        doc= nlp(d)
        tokens_doc=[]

        for token in doc:
            if not token.is_punct and not token.is_stop:
                tokens_doc.append(token.text.lower())
        new_collection.append(tokens_doc)

    return new_collection

collection= pre_processamento(raw_collection)
#print(resultado)

#tf(t,d) = count(t) / total words(d)

def tf(d):
    N=len(d)
    res= {}
    for term in d:
        if  term in res:
            res[term] +=1
        else:
            res[term] = 1
    res ={k: v/N for k,v in res.items()}
    return res
    #output: {"termo": freq_relativa}

#idf(t,D) = log(N/df)
def idf(collection):
    res= {}
    N= len(collection)
    unique_terms = set([term for d in collection for term in d]) #lista com todos os termos da minha colecao mas sem repetidos
    
    for term in unique_terms:
        counter=0 
        for d in collection:
            if term in d:
                counter +=1

        rarity = math.log(N / counter, 10)
        res[term] = rarity

    return res # {"termo": rarity}

#tf-idf(t,d,D) = tf(t,d) * idf(t,D)
def tf_idf(collection): #falta aparecer os zeros, pois estes tambem fazem parte do vetor
    unique_terms = sorted(set([term for d in collection for term in d]))
    idf_values= idf(collection)
    res=[]
    for doc in collection:
        doc_tf_idf =[]
        tf_values = tf(doc)
        for term in unique_terms:
            if term in tf_values:
                tf_idf = tf_values[term] * idf_values[term]
                doc_tf_idf.append(tf_idf)
            else:
                doc_tf_idf.append(0)
        res.append(doc_tf_idf)

    return res 

#print(tf_idf(collection))



query="The bright sun"

def preprocessamento_query(q):
    tokens=[]
    q_nlp=nlp(q)
    for token in q_nlp:
        if not token.is_punct and not token.is_stop:
            tokens.append(token.text.lower())

    return tokens

def vetor_query(query, collection):
    query_tokens= preprocessamento_query(query)
    tf_query= tf(query_tokens)
    idf_values= idf(collection)

    unique_terms = sorted(set([term for d in collection for term in d]))

    query_vetor=[]

    for term in unique_terms:
        if term in tf_query:
            tf_idf_query = tf_query[term] * idf_values[term]
            query_vetor.append(tf_idf_query)
        else:
            query_vetor.append(0)
    
    return query_vetor

def similaridade_coseno(query_vector, doc_vector):
    prod=0
    for term_q, term_d in zip(query_vector, doc_vector):
        prod += term_q * term_d

    norm_q=0
    for term in query_vector:
        norm_q += term ** 2
    norm_q = math.sqrt(norm_q)

    norm_d=0
    for term in doc_vector:
        norm_d += term ** 2
    norm_d = math.sqrt(norm_d)

    if norm_q == 0 or norm_d == 0:
        return 0

    res = prod / (norm_q * norm_d)
    return res

def ranking(query, collection):
    docs_vectors= tf_idf(collection)
    query_vector=vetor_query(query, collection)
    scores =[]
    
    for i, doc_vector in enumerate(docs_vectors):
        score=similaridade_coseno(query_vector, doc_vector)
        scores.append((i,score))
        
    ranking= sorted(scores, key= lambda x: x[1], reverse=True)
    return ranking

print(ranking(query, collection))
