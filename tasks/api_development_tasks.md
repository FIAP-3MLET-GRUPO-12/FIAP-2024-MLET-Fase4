# Lista de Tarefas para o Projeto de Previsão de Ações com LSTM - Dia 3

## Arquivos Relevantes

- `api/main.py` - Arquivo principal da API FastAPI com as rotas e configurações
- `api/models.py` - Modelos Pydantic para validação de entrada/saída
- `api/services.py` - Lógica de negócio para carregar modelo e fazer previsões
- `api/tests/test_main.py` - Testes de integração para as rotas da API
- `api/tests/test_services.py` - Testes unitários para os serviços
- `models/` - Diretório para armazenar o modelo LSTM e scaler salvos
- `requirements.txt` - Atualizado com dependências da API

### Notas

- Execute os testes com `pytest api/tests/`
- Inicie a API localmente com `uvicorn api.main:app --reload`
- Acesse a documentação Swagger em `http://localhost:8000/docs`

## Tarefas

- [ ] **1.0 Preparar Estrutura do Projeto**
  - [ ] 1.1 Criar diretório `api/` e subdiretórios
  - [ ] 1.2 Atualizar `requirements.txt` com FastAPI, uvicorn, pytest
  - [ ] 1.3 Criar arquivo `.gitignore` para arquivos temporários e cache

- [ ] **2.0 Salvar Modelo e Scaler**
  - [ ] 2.1 Implementar função para salvar modelo LSTM em formato keras
  - [ ] 2.2 Salvar scaler usando joblib ou pickle
  - [ ] 2.3 Criar função para carregar modelo e scaler
  - [ ] 2.4 Testar carregamento do modelo e scaler

- [ ] **3.0 Definir Modelos de Dados**
  - [ ] 3.1 Criar modelo Pydantic para dados de entrada (janela temporal)
  - [ ] 3.2 Criar modelo para resposta da previsão
  - [ ] 3.3 Adicionar validações personalizadas para dados de entrada

- [ ] **4.0 Implementar Serviços**
  - [ ] 4.1 Criar função para preprocessar dados de entrada
  - [ ] 4.2 Implementar função de previsão usando modelo carregado
  - [ ] 4.3 Criar função para pós-processar resultado (desnormalização)
  - [ ] 4.4 Adicionar tratamento de erros e exceções

- [ ] **5.0 Desenvolver API FastAPI**
  - [ ] 5.1 Configurar aplicação FastAPI básica
  - [ ] 5.2 Implementar rota POST `/predict`
  - [ ] 5.3 Adicionar documentação com docstrings
  - [ ] 5.4 Configurar CORS e middleware necessário

- [ ] **6.0 Implementar Testes**
  - [ ] 6.1 Criar testes unitários para serviços
  - [ ] 6.2 Implementar testes de integração para API
  - [ ] 6.3 Adicionar casos de teste para validação de entrada
  - [ ] 6.4 Testar cenários de erro e exceções

- [ ] **7.0 Documentação e Exemplo de Uso**
  - [ ] 7.1 Documentar formato de entrada/saída da API
  - [ ] 7.2 Criar exemplo de requisição com curl/Python
  - [ ] 7.3 Adicionar instruções de instalação e execução
  - [ ] 7.4 Documentar possíveis códigos de erro 