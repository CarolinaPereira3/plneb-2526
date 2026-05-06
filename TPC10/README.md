## **TPC10**
Este trabalho consistiu na continuação do trabalho desenvolvido em aula, onde foi implementado um modelo de Named Entity Recognition (NER) baseado em BERT com fine-tuning.

O objetivo principal deste trabalho foi adaptar um modelo de linguagem pré-treinado para a tarefa de reconhecimento de entidades nomeadas em texto em português.

Para este trabalho foi utilizado um modelo pré-treinado disponível na plataforma Hugging Face:

- Modelo: `neuralmind/bert-large-portuguese-cased`

Este modelo já tinha sido previamente treinado em grandes volumes de texto em português, sendo capaz de compreender contexto linguístico, mas não estando ainda adaptado especificamente para a tarefa de NER.

Também foi utilizado um dataset disponível no Hugging Face:

Dataset: `lfcc/portuguese_ner`

Este dataset contém frases anotadas com entidades no formato BIO, permitindo treinar o modelo para reconhecer:

- Pessoa
- Organização
- Local
- Data
- Profissão
- Outras entidades (e tokens que não são entidades representados por O)

O modelo foi carregado para token classification da seguinte forma:

```
model= AutoModelForTokenClassification.from_pretrained("neuralmind/bert-large-portuguese-cased",num_labels= n_labels, id2label=id2label, label2id=label2id) 
```

A utilização de id2label e label2id foi essencial para garantir que o modelo devolve diretamente as classes corretas (ex: B-Pessoa, I-Organizacao) em vez de rótulos genéricos como LABEL_0.

Durante o pré-processamento dos dados foi necessário limitar o tamanho das frases a no máximo 512 tokens, pois algumas delas excediam este limite e o modelo BERT só consegue receber entradas até esse tamanho. Por isso, todas as frases maiores que esse limite foram cortadas.

Durante o treino foi utilizada a classe Trainer da biblioteca Hugging Face.

Hiperparâmetros utilizados:

- Learning rate: 2e-5

- Batch size (train/eval): 4

- Número de épocas: 2

- Weight decay: 0.01

A escolha de batch size reduzido deveu-se a limitações de memória da GPU utilizada no Google Colab.

Foi também utilizada a função, que calcula automaticamente em cada época, os valores de precisão, cobertura, F1-score e accuracy.

O modelo foi então treinado ao longo de duas épocas, apresentando uma evolução consistente do desempenho. Durante o processo de treino, observou-se uma diminuição significativa da loss de treino, bem como uma melhoria geral nas métricas de avaliação. Na primeira época, o modelo já demonstrava um desempenho elevado, com valores de precision, recall, F1-score e accuracy bastante satisfatórios. Na segunda época, verificou-se uma melhoria adicional nas métricas de precisão e F1-score, indicando uma melhor capacidade do modelo em identificar corretamente entidades no texto. No entanto, a validation loss manteve-se aproximadamente estável, sugerindo que o modelo já se encontrava próximo da sua capacidade de generalização ótima para este dataset.

Após o treino, o modelo foi testado em frases novas utilizando uma pipeline de inferência e este demonstrou capacidade de identificar corretamente as entidades.