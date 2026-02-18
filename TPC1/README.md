## TPC1

Este trabalho consistiu na resolução de problemas utilizando funções em Python.

De forma geral, foram aplicados conceitos como:

-Slicing de strings, utilizado para inverter uma string ('s[::-1]') e para extrair subconjuntos da mesma, permitindo comparar apenas partes específicas; 
-Métodos embutidos como 'upper()' e 'lower()', para conversão entre maiúsculas e minúsculas;
-Utilização de ciclos 'for';
-Retorno de valores booleanos (True ou False), quer através de uma variável auxiliar (res), quer com retorno direto quando não havia necessidade de continuar a execução, tornando a função mais eficiente.

Um dos aspetos mais relevantes deste trabalho foi a implementação da função da pergunta 9, anagrama(), que verifica se duas strings são anagramas. A lógica que utilizada consistiu em percorrer cada letra da primeira string e removê-la da segunda string utilizando:

```
s2 = s2.replace(letra, "", 1)
```

Esta função garante que apenas a primeira ocorrência da letra é removida de cada vez. Assim, no caso de letras repetidas, apenas uma instância é eliminada por iteração.