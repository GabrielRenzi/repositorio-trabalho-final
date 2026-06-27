# Trabalho Final - Cloud Computing: Plataforma de Streaming de Vídeos Educacionais 🎥

**Instituição:** UNIDAVI - Centro Universitário para o Desenvolvimento do Alto Vale do Itajaí  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Cloud Computing  
**Professor:** Prof. Esp. Ademar Perfoll Junior  
**Autor:** Gabriel Wellington Renzi 

---

## 📌 Apresentação do Projeto
Este repositório contém a entrega da avaliação conclusiva do semestre da disciplina de Cloud Computing. O projeto consiste no desenvolvimento de uma API RESTful simulando o backend de uma **Plataforma de Streaming de Vídeos Educacionais**, com testes unitários e a implementação de uma cultura DevOps através de um pipeline de Integração Contínua (CI) via GitHub Actions.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.10+
* **Framework Web:** Flask 3.0.3
* **Testes:** Pytest e Pytest-Flask
* **Análise Estática (Linting):** Flake8
* **CI/CD:** GitHub Actions
* **Containerização:** Docker

## 📁 Estrutura de Diretórios
A organização do repositório segue a estrutura recomendada:

```text
repositorio-trabalho-final/
├── api/
│   ├── app.py                   # Código-fonte principal da API
│   ├── data/
│   │   └── videos.json          # Dados simulados da plataforma
│   └── tests/
│       └── test_api.py          # Casos de teste unitários (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml               # Configuração do pipeline de CI
├── Dockerfile                   # Instruções de containerização
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação principal
```


## ⚙️ Pré-requisitos
**Antes de iniciar, certifique-se de ter instalado em sua máquina:**

* Python 3.10 ou superior
* Git
* Docker Desktop (Caso deseje rodar a aplicação em container)

## 🚀 Como Executar Localmente (Sem Container)
**Clone o repositório:**

* git clone https://github.com/GabrielRenzi/repositorio-trabalho-final.git
* cd repositorio-trabalho-final

**Crie e ative um ambiente virtual:**

* python -m venv venv
* .\venv\Scripts\activate

**Instale as dependências listadas:**

* pip install -r requirements.txt

**Inicie a aplicação:**

* python api/app.py

**A API estará rodando localmente no endereço: http://localhost:5000**

## 🐳 Como Executar via Container (Com Docker)
**Caso prefira rodar a aplicação de forma isolada utilizando o Docker, siga os passos:**
Certifique-se de que o Docker Desktop está em execução.

**Faça o build da imagem na raiz do projeto:**

* docker build -t streaming-api .

**Execute o container mapeando a porta 5000:**

* docker run -d -p 5000:5000 --name api-streaming-edu streaming-api
**A API estará acessível no mesmo endereço: http://localhost:5000**

## 🧪 Como Rodar os Testes Unitários
Para garantir a estabilidade das rotas, a API conta com uma suíte de testes unitários desenvolvida com pytest.
**Com o ambiente virtual ativado na raiz do projeto, execute o comando:**

* pytest api/tests/
O console exibirá o resultado das validações das rotas e do formato JSON retornado.

📡 Endpoints (Rotas da API)
**GET /status: Retorna as informações de saúde da aplicação (nome, versão, status).**

* http://127.0.0.1:5000/status

**GET /videos: Retorna a lista completa com os registros de vídeos educacionais cadastrados no videos.json.**

* http://127.0.0.1:5000/videos

**GET /videos/<id>: Retorna o detalhamento de um vídeo específico com base no ID fornecido (Ex: /videos/3)**

* http://127.0.0.1:5000/videos/3

**Retorna erro 404 Not Found caso o vídeo não exista.** 

* http://127.0.0.1:5000/videos/999

## 🔄 Integração Contínua (CI)
O projeto possui um pipeline automatizado via GitHub Actions (ci.yml). A cada novo push para a branch main, o workflow executa:

Configuração do ambiente Python.

Instalação das dependências.

Etapa Adicional: Análise estática do código (linting) utilizando o Flake8 para identificar erros de sintaxe ou violações de boas práticas.

Execução automatizada da suíte de testes unitários com o Pytest.