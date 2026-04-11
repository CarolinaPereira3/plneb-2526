## TPC8
Este trabalho consistiu na continuação do TPC7, relativo ao desenvolvimento de uma aplicação *web* em Flask de um dicionário médico.

Neste trabalho foi implementada a funcionalidade de pesquisa, acessível através do botão “Pesquisar” na página inicial ou através da barra de navegação na secção correspondente.

A página de pesquisa permite ao utilizador procurar um termo presente nas designações ou descrições do dicionário médico. Esta pesquisa pode ser configurada através de duas opções: *word boundary* e *case sensitive*. A opção *word boundary* permite restringir a pesquisa apenas a palavras completas, evitando correspondências parciais dentro de outras palavras (por exemplo, impedir que “teste” corresponda a “testemunha”). Já a opção *case sensitive* define se a pesquisa deve distinguir entre letras maiúsculas e minúsculas.

Os resultados obtidos são apresentados na mesma página, sendo o termo pesquisado destacado em negrito.

Para a implementação desta funcionalidade foram criadas duas rotas associadas à página de pesquisa: uma rota GET e uma rota POST.

A rota GET é responsável apenas por renderizar a página de pesquisa quando o utilizador a acede através do botão ou da barra de navegação. Por outro lado, a rota POST trata do processamento dos dados submetidos pelo utilizador, nomeadamente o termo de pesquisa e as opções selecionadas (*case sensitive* e *word boundary*).

Para a pesquisa, cada entrada do dicionário foi construída como uma string no formato “designação - descrição”. Em seguida, foram aplicadas condições consoante as opções selecionadas pelo utilizador.

A verificação da existência do termo foi realizada recorrendo a expressões regulares (`re.search`). Quando a opção *word boundary* é ativada, o padrão de pesquisa inclui delimitadores de palavra (`\b`), garantindo que apenas palavras completas são consideradas. Caso contrário, a pesquisa é realizada por correspondência parcial. Adicionalmente, foi utilizada a função `re.escape` para garantir que caracteres especiais no termo não sejam interpretados como expressões regulares.

Quando a opção *case sensitive* não está ativa, é utilizada a *flag* `re.IGNORECASE`, permitindo ignorar diferenças entre maiúsculas e minúsculas.

Quando é encontrado um resultado, este é adicionado à lista de resultados. Para o destaque do termo em negrito, foram consideradas duas situações:

- Quando a pesquisa é *case sensitive*, a substituição é direta, envolvendo o termo encontrado com a *tag* `<b>`.

- Quando a pesquisa não é *case sensitive*, é utilizada uma função `lambda` em conjunto com `m.group`, de forma a preservar exatamente o texto encontrado (incluindo maiúsculas e minúsculas) no `match` e apenas envolvê-lo em negrito.

A página HTML de pesquisa foi implementada utilizando formulários (`forms`) com um campo de texto para introdução do termo a pesquisar e duas caixas de seleção (*checkboxes*) para as opções *case sensitive* e *word boundary*. Estes dados são enviados através do método `POST`.

Por fim, os resultados são apresentados na mesma página, sendo cada entrada exibida de forma individual, facilitando a leitura e organização dos resultados.