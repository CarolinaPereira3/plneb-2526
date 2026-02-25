## TPC2

Este trabalho consistiu na resolução de diferentes tipos de problemas envolvendo expressões regulares em Python.

Ao longo dos exercícios foram utilizados várias funções da biblioteca "re", nomeadamente "match", "search", "findall", "sub" e "split", permitindo explorar diferentes formas de interação com expressões regulares consoante o objetivo pretendido, utilizando diversos elementos fundamentais das expressões regulares, tais como:
- quantificadores;
- classes de caracteres;
- disjunções e intervalos;
- âncoras;
- grupos capturantes.

Em alguns exercícios foi utilizada a flag "IGNORECASE", permitindo realizar correspondências sem distinção entre maiúsculas e minúsculas.

Um dos exercícios que considerei mais interessante e desafiante foi o exercício 5, relacionado com a soma de números separados por vírgulas. A abordagem escolhida consistiu em capturar a sequência completa de números separados por vírgulas numa única correspondência e, posteriormente, dividir essa sequência pelas vírgulas para calcular a soma. Esta estratégia implicou a utilização de um grupo não capturante, de forma a estruturar corretamente o padrão de repetição sem criar subgrupos adicionais nas correspondências devolvidas. Tal opção foi necessária porque, ao utilizar findall, a presença de um grupo capturante altera o formato do resultado: em vez de devolver a correspondência completa, a função retorna apenas o conteúdo do grupo capturante. Neste caso específico, isso faria com que fosse devolvida apenas a última repetição do grupo (ou seja, apenas o último número precedido de vírgula), e não a sequência completa pretendida.

De forma geral, este trabalho permitiu consolidar conceitos teóricos sobre expressões regulares e desenvolver maior precisão na construção de padrões adequados a diferentes problemas.

