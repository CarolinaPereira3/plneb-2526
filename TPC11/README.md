## TPC11
Neste trabalho foi dado seguimento à implementação do modelo TF-IDF, com o objetivo de permitir a recuperação de documentos relevantes a partir de uma *query*.

Em primeiro lugar, foi melhorada a função de pré-processamento da coleção de documentos. Para isso, foi utilizado o modelo de linguagem inglês do spaCy, que permite a tokenização automática do texto. Durante este processo, cada documento foi transformado numa lista de *tokens*, removendo *stop words* e pontuação, e convertendo todas as palavras para minúsculas. Desta forma, obteve-se uma coleção estruturada como uma lista de listas de *tokens*.

De seguida, foi realizado o pré-processamento da *query* de forma equivalente à coleção, garantindo que ambos se encontram no mesmo espaço de representação.

Posteriormente, foi construído o vetor TF-IDF da *query*. Este vetor é obtido através do cálculo da frequência dos termos na *query* (TF), multiplicada pelo valor de IDF calculado a partir da coleção de documentos. O resultado é um vetor numérico com a mesma dimensão do vocabulário global da coleção, onde cada posição representa o peso de um termo e assume valor zero caso o termo não esteja presente na *query*.

Após isso, foi implementada a função de similaridade do cosseno, que permite medir a proximidade entre dois vetores (*query* e documento). Esta métrica é calculada através do produto interno entre os vetores, dividido pelo produto das suas normas, permitindo obter um valor entre 0 e 1 que representa o grau de similaridade entre eles.

Por fim, foi criada a função de ranking, que calcula a similaridade entre a *query* e cada documento da coleção. Os resultados são ordenados de forma decrescente, devolvendo assim os documentos mais relevantes para a *query*, juntamente com o respetivo *score* de similaridade.

A *query* utilizada foi:

"The bright sun"

A coleção de documentos utilizada foi:

- "The sky is blue"

- "The sun is bright"

- "The sun in the sky"

Deste modo, o resultado do *ranking* obtido foi:

```
[(1, 1.0), (2, 0.24482975009584626), (0, 0.0)]
```

Sendo assim, o segundo documento é o mais similar à *query*, seguido do terceiro documento e, por último, o primeiro documento, que apresenta um score de similaridade de 0, ou seja, não possui qualquer relação relevante com a query considerada.