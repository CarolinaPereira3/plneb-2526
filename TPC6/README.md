## TPC6

O objetivo deste trabalho, "Harry Friends", foi extrair todos os personagens do livro *Harry Potter e a Pedra Filosofal* e computar as relações entre eles com base na co-ocorrência numa mesma frase. Por exemplo, se Harry e Rony aparecem na mesma frase, isso é considerado uma ocorrência da sua amizade. O resultado final esperado é um dicionário onde:

- Cada chave representa um personagem do texto;

- O valor de cada chave é outro dicionário cujas chaves correspondem aos amigos desse personagem, e os valores representam o número de vezes que os seus nomes aparecem juntos numa frase.

Para realizar este exercício utilizou-se a biblioteca de processamento de linguagem natural spaCy.

Inicialmente, criei uma lista chamada `pessoas`, percorrendo todos os tokens do texto e adicionando à lista aqueles cujo `ent_type_` fosse `"PER"`. Embora essa abordagem capturasse praticamente todos os personagens, também incluía muitos tokens irrelevantes, como caracteres de formatação ("\n") e palavras que não eram nomes próprios, portanto optei por ir por um caminho diferente.

Através da lista pessoas que me tinha dado, retirei todos os reais personagens que tinham sido encontrados e criei *entity rulers* para estes. Cada personagem recebeu padrões (*patterns*) que incluíam nome próprio, apelido e uma combinação de ambos, garantindo que nomes como "Harry Potter" fossem reconhecidos como uma única entidade do tipo "Pessoa". Adicionalmente, os padrões foram configurados como case-insensitive através de "LOWER", por exemplo:

```
    {"label": "Pessoa", "pattern": [{"LOWER": "harry"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "potter"}]},
    {"label": "Pessoa", "pattern": [{"LOWER": "harry"}, {"LOWER": "potter"}]},
```
Adicionei estes padrões antes do NER (named entity recognition) do modelo (``before="ner"`), de modo a evitar conflitos entre as entidades definidas manualmente e aquelas detetadas automaticamente pelo modelo.

Após definir os padrões, percorri todas as entidades do texto e adicionei à lista pessoas apenas aquelas cujo `label_` fosse `"Pessoa"`. Assim, garantimos que apenas os personagens definidos no EntityRuler fossem considerados.

Para cada personagem da lista pessoas:

- Criei uma chave no dicionário amigos;

- O valor desta chave é outro dicionário, contendo todos os outros personagens que aparecem na mesma frase, com o número de vezes que isso ocorre;

- Se um par de amigos aparece pela primeira vez, inicia-se o contador em zero e adiciona-se 1. Para ocorrências subsequentes, incrementa-se o valor em 1.

No entanto, um grande problema que me deparei na realização deste exercício foi o grande poder computacional que ele exige. Por isso, para tornar o exercício viável, o cálculo foi restrito ao trio principal (Harry, Rony e Hermione).

Como existiam diferentes formas de referir o mesmo personagem (por exemplo, Harry Potter, Harry, HARRY POTTER, POTTER), criei um dicionário de normalização. Nesse dicionário, cada variação do nome funciona como chave e o valor correspondente é o nome completo e padronizado do personagem.

De seguida, foi construído um novo dicionário chamado `amigos_normalizado`. Neste dicionário, as chaves correspondem apenas aos nomes normalizados (ou seja, os valores do dicionário de normalização). Para cada personagem, foram agregadas todas as relações de amizade associadas às diferentes variações do seu nome original, garantindo que toda a informação de cada personagem fique numa única instância.

Por fim, o dicionário resultante foi exportado para um ficheiro JSON para facilitar a visualização.