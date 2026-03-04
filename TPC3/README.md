## TPC3
O objetivo deste TPC foi corrigir um detalhe no trabalho desenvolvido durante a aula. O exercício consistia em converter um ficheiro PDF contendo um dicionário médico num dicionário em Python, em que as *keys* correspondem às designações dos conceitos e os *values* às respetivas descrições.

Durante a aula, o processo foi realizado convertendo previamente o PDF para texto e utilizando um marcador ("@") para assinalar o início de cada conceito. Este marcador foi inserido sempre que eram encontradas duas quebras de linha consecutivas ('\n\n'), assumindo que estas representavam a separação entre conceitos. De seguida, foi realizado um 'split' sempre que surgia o padrão '\n\n@', permitindo obter uma lista em que cada elemento correspondia, idealmente, a um conceito completo. Posteriormente, cada bloco foi dividido apenas no primeiro '\n', partindo do princípio de que a primeira linha correspondia à designação e o restante texto à descrição.

De um modo geral, esta abordagem funcionou corretamente. No entanto, verificou-se um problema específico: em alguns casos, a designação de um conceito encontrava-se no final de uma página e a respetiva descrição no início da página seguinte. Ao remover o carácter de mudança de página ('\f'), estas situações passaram a ser interpretadas como blocos separados, fazendo com que o split pela expressão regular '\n\n@' gerasse dois elementos distintos na lista 'conceitos', quando na realidade pertenciam ao mesmo conceito.

Para resolver este problema, foi alterado o critério de segmentação da lista de conceitos. Em vez de dividir apenas por '\n\n@', passou a ser dividido da seguinte forma:

```
conceitos= re.split(r"\.\n\n@", texto)
```

Desta forma, o 'split' só ocorre quando existe um ponto final seguido de duas quebras de linha e do marcador "@". Como o ponto final indica o término de uma definição, esta alteração garante que apenas são separados blocos cujo conceito anterior está efetivamente concluído. Assim, evita-se a divisão incorreta de um mesmo conceito quando existem quebras de linha intermédias entre a designação e a descrição.

Adicionalmente, manteve-se uma verificação durante o processamento da lista 'conceitos'. Caso, após o 'split', um elemento não contém qualquer '\n' (ou seja, não é possível separar designação e descrição), isso indica que ocorreu uma quebra de página entre ambos.

Nesses casos, o programa entra no bloco 'else', onde é utilizada uma variável booleana ('i') para controlar o estado da leitura. Esta variável é inicializada como 'False' antes do ciclo 'for'.
- Se 'i' for 'False', significa que se trata da primeira parte do conceito (a designação). Essa linha é então guardada como designacao e a variável 'i' passa a 'True'.
- Quando o programa encontra o elemento seguinte (correspondente à descrição), entra novamente no 'else'. Como 'i' está agora 'True', essa linha é interpretada como descricao, sendo então associada à designação previamente guardada e adicionada ao dicionário. De seguida, 'i' volta a 'False'.

Desta forma, cumprimos o objetivo do exercício e garantimos que conceitos cuja designação e descrição foram separados por uma mudança de página sejam corretamente reconstruídos e armazenados no dicionário final.