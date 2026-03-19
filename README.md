# 🧠 copilot-openai-workshop

Laboratórios práticos de IA generativa com **Microsoft Copilot** e **Azure OpenAI**, baseados no laboratório DIO “Explorando os recursos de IA generativa com Copilot e OpenAI”.  
O objetivo é **aprender fazendo**: criar scripts, explorar prompts e integrar IA generativa em fluxos de trabalho reais.

## 🎯 Objetivos

- Entender o básico de IA generativa e como ela se aplica a produtividade e programação.
- Usar **Azure OpenAI** via código em Python.
- Utilizar **GitHub Copilot** como assistente de programação em Python.
- Praticar **uso responsável de IA** (segurança, filtros de conteúdo, controle de dados).

## 🧩 Laboratórios

Cada laboratório é um diretório em `labs/` com um README próprio e código de exemplo:

- `lab-01-azure-openai-playground`: chamada simples à API do Azure OpenAI.
- `lab-02-github-copilot-refatoracao`: refatorar código com ajuda do Copilot.
- `lab-03-automacoes-365`: textos e recomendações para uso de Copilot no Microsoft 365 (não requer código).
- `lab-04-chatbot-simples`: um chatbot de linha de comando com Azure OpenAI.

## 🔧 Requisitos

- Conta na **plataforma DIO** (opcional, para acompanhar a trilha).
- Conta no **Azure** com acesso para criar um recurso **Azure OpenAI Service**.
- Instalado:
  - Python 3.9+
  - Git
  - Azure CLI (opcional, para scripts de provisionamento).
- Editor preferido com **GitHub Copilot** (VS Code, JetBrains, etc.).

## ⚙️ Instalação e configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/copilot-openai-workshop.git
   cd copilot-openai-workshop
   ```

2. Crie um ambiente virtual e instale dependências:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   # ou
   .venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. Configure o Azure OpenAI:

   - Crie um recurso **Azure OpenAI Service** no portal Azure.
   - Anote:
     - `AZURE_OPENAI_ENDPOINT`
     - `AZURE_OPENAI_KEY`
     - `AZURE_OPENAI_DEPLOYMENT_ID` (ex.: `gpt-35-turbo`).
   - Copie `.env.example` para `.env`:

     ```bash
     cp .env.example .env
     ```

   - Edite `.env` com suas credenciais:

     ```env
     AZURE_OPENAI_ENDPOINT=https://seu-recurso.openai.azure.com
     AZURE_OPENAI_KEY=xxxxxx
     AZURE_OPENAI_DEPLOYMENT_ID=gpt-35-turbo
     ```

4. Executar um exemplo simples:

   ```bash
   python labs/lab-01-azure-openai-playground/example.py
   ```

## 📚 Documentação

Veja a pasta `docs/` para leituras complementares:

- `01-introducao-ia-generativa.md`
- `02-configurando-azure-openai.md`
- `03-usando-github-copilot.md`
- `04-boas-praticas-de-uso-responsavel.md`

## 🤝 Contribuindo

Sua contribuição é bem-vinda! Consulte o arquivo [`CONTRIBUTING.md`](CONTRIBUTING.md) para ver como:

- Adicionar novos laboratórios.
- Melhorar a documentação em português.
- Criar exemplos em outras linguagens (JavaScript, .NET, etc.).

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.

---

> **Dica:** se você está fazendo o bootcamp **“Coding The Future – IA Generativa com Microsoft Copilot”** na DIO, este repositório pode servir como **portfolio de estudos** e código prático para mostrar em entrevistas.
