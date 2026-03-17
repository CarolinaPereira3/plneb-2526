## TPC5
Neste trabalho foi dada continuidade ao exercício iniciado durante a aula. O objetivo foi realizar *web scraping* ao site "https://www.atlasdasaude.pt/doencasAaZ", que apresenta uma lista de doenças organizadas alfabeticamente.

Neste site, existe uma página para cada letra do alfabeto, onde são listadas várias doenças que começam por essa letra. Em cada uma dessas páginas aparece uma descrição curta de cada doença. Além disso, cada doença possui também uma página própria, acessível através de uma hiperligação, onde é apresentada uma descrição mais detalhada.

Durante a aula foi desenvolvido código que permitiu construir um dicionário em Python em que cada *key* correspondia ao nome de uma doença (de A a Z) e o respetivo *value* era a descrição curta apresentada na página da lista.

O objetivo deste trabalho foi estender esta solução, de forma a que o dicionário final tivesse a seguinte estrutura:

- cada *key* corresponde ao nome da doença
- cada *value* corresponde a outro dicionário com duas entradas:
    - `smallDescricao`: descrição curta da doença (obtida na página da lista)
    - `fullDescricao`: descrição completa da doença (obtida na página individual)

Ao analisar o HTML da página que lista as doenças, foi possível verificar que o nome de cada doença contém uma hiperligação (`<a>`) para a página individual dessa doença. Assim, dentro de cada elemento `div_doencas`, foi possível obter esse link através de:

```python
linkFullDescricao= div.div.h3.a["href"]
```

Este valor corresponde apenas ao caminho relativo da página (por exemplo /content/asma). Para obter o link completo, foi necessário concatenar este caminho com o endereço base do site, "https://www.atlasdasaude.pt". Desta forma foi possível construir o URL completo da página de cada doença.

Após da obtenção do link completo da doença, foi feito um novo request HTTP para descarregar o HTML dessa página. Esse HTML foi novamente processado utilizando a biblioteca BeautifulSoup.

Ao analisar o HTML das páginas individuais das doenças, verificou-se que a descrição completa estava sempre contida num elemento div com a classe "field-name-body". Assim, foi possível extrair o texto completo da descrição utilizando:

```python
fullDescricao = soup2.find("div", class_="field-name-body").text
```

Após isso, o dicionário foi reformulado de forma a que, em vez de as *keys* estarem associadas apenas à smallDescricao, passassem a estar associadas a um dicionário contendo a `smallDescricao` e a `fullDescricao`. Por fim, foi aplicado o método `strip()` a ambas as descrições, de modo a remover caracteres "\n" desnecessários no início e no fim do texto.