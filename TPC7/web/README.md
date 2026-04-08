## TPC7 
O objetivo deste trabalho foi finalizar a interface *web* utilizando a *framework* Flask, que começou a ser desenvolvida durante a aula. A única parte que faltava implementar era a página inicial da aplicação.

Esta interface *web* consiste num dicionário médico. Na página de conceitos, já existente, apresentava-se uma lista de todas as designações médicas por ordem alfabética. Ao clicar em cada conceito, o utilizador era direcionado para uma página correspondente contendo a descrição detalhada dessa designação. Todo o trabalho foi realizado utilizando Bootstrap 5, garantindo uma interface responsiva e agradável visualmente.

Para a página inicial, foi utilizado o componente "Centered Hero" do Bootstrap. Esta página apresenta, em destaque, um título e uma breve descrição da interface, e fornece duas formas de explorar os conceitos médicos:

1. Explorar conceitos: um botão que leva à lista completa de conceitos de A-Z.
2. Filtro por letra: um botão para cada letra do alfabeto; ao selecionar uma letra, são exibidos apenas os conceitos que começam por essa letra.

Para que o filtro por letra funcionasse, a função associada à rota `/conceitos` foi modificada. Agora, se o URL contiver o parâmetro letra, a lista de conceitos é filtrada apenas pelos que começam com essa letra. Caso contrário, são exibidos todos os conceitos.

Além disso, foi criada a função `remover_acentos`, que elimina os acentos das palavras. Isto garante que conceitos que começam com letras acentuadas, como "ácino", também apareçam corretamente ao filtrar por "A".

Com estas alterações, a interface *web* ficou completa, funcional e intuitiva, permitindo ao utilizador explorar facilmente os conceitos médicos de forma organizada.