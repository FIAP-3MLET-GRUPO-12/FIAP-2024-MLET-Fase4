# Instruções de Deploy

Este guia explica como fazer o deploy da API de previsão de ações em diferentes plataformas.

## Preparação

Antes de fazer o deploy, certifique-se de que:

1. O modelo LSTM (`models/tesla_lstm_model.keras`) está presente
2. O scaler (`models/scaler.joblib`) está presente
3. Todos os arquivos estão commitados no Git
4. Você testou a API localmente com Docker

## Deploy no Railway

1. Crie uma conta no [Railway](https://railway.app/)

2. Conecte seu repositório GitHub:
   - Vá para o dashboard do Railway
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. Configure as variáveis de ambiente:
   - Vá para a aba "Variables"
   - Adicione:
     ```
     PORT=8000
     ENVIRONMENT=production
     ```

4. O Railway detectará automaticamente o Dockerfile e fará o deploy

5. Acesse sua API:
   - Railway fornecerá uma URL única
   - Teste com: `https://seu-app.railway.app/health`

## Deploy no Render

1. Crie uma conta no [Render](https://render.com/)

2. Crie um novo Web Service:
   - Clique em "New +"
   - Selecione "Web Service"
   - Conecte seu repositório GitHub

3. Configure o serviço:
   - Nome: `stock-prediction-api`
   - Environment: "Docker"
   - Branch: `main`
   - Region: Escolha a mais próxima
   - Instance Type: Free (para testes)

4. Configure as variáveis de ambiente:
   ```
   PORT=8000
   ENVIRONMENT=production
   ```

5. Clique em "Create Web Service"

6. Acesse sua API:
   - Render fornecerá uma URL única
   - Teste com: `https://seu-app.onrender.com/health`

## Monitoramento

A API inclui endpoints para monitoramento:

### 1. Métricas Prometheus (/metrics)
```bash
curl https://sua-api.com/metrics
```

Métricas disponíveis:
- `api_requests_total`: Total de requisições
- `api_request_latency_seconds`: Latência das requisições
- `model_predictions_total`: Total de previsões

### 2. Health Check (/health)
```bash
curl https://sua-api.com/health
```

### 3. Logs
- Os logs são formatados em JSON
- Incluem request ID, tempo de resposta e status
- Podem ser visualizados no dashboard da plataforma

## Troubleshooting

1. **Erro de memória no Railway**:
   - Aumente a memória nas configurações do projeto
   - Ou otimize o carregamento do modelo

2. **Deploy falha no Render**:
   - Verifique os logs no dashboard
   - Confirme se os arquivos do modelo estão presentes
   - Verifique se o Dockerfile está correto

3. **API lenta na primeira requisição**:
   - Normal devido ao cold start
   - Configure um health check para manter a instância ativa

## Próximos Passos

1. Configure um domínio personalizado
2. Adicione HTTPS
3. Configure alertas de monitoramento
4. Implemente rate limiting
5. Adicione autenticação

## Custos Estimados

- Railway: Gratuito para projetos pequenos
- Render: Gratuito no plano individual
- Custos aumentam com mais recursos/tráfego 