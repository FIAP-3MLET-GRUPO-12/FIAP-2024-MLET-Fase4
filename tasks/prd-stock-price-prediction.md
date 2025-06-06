## Modelagem LSTM

### Justificativa para Escolha do Modelo LSTM
O modelo LSTM (Long Short-Term Memory) foi escolhido devido à sua capacidade de capturar dependências de longo prazo em séries temporais, o que é essencial para prever preços de ações que são influenciados por tendências passadas.

### Descrição Técnica da Arquitetura Inicial
A arquitetura inicial do modelo LSTM será composta por:
- Uma camada LSTM com 50 unidades
- Uma camada densa totalmente conectada para a saída
- Função de ativação ReLU
- Otimizador Adam

### Estratégia de Divisão dos Dados
Os dados serão divididos em:
- 70% para treino
- 15% para validação
- 15% para teste

### Métricas Usadas para Avaliação
As métricas de avaliação incluirão:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)
- MAPE (Mean Absolute Percentage Error)

### Plano para Ajuste de Hiperparâmetros
O ajuste de hiperparâmetros será realizado utilizando técnicas de busca em grade (grid search) para otimizar parâmetros como:
- Número de unidades LSTM
- Taxa de aprendizado
- Tamanho do batch 