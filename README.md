# Atividade 03 TESI I - Geração de Embeddings Locais com Ollama

Repositório criado para a Avaliação Online 3 da disciplina Tópicos Específicos em Sistemas para Internet I (IFRN - TSI).

## Objetivo

Demonstrar a instalação, execução local do Ollama e a extração de representações vetoriais (embeddings) a partir de um texto utilizando Python.

## Pré-requisitos

- [Ollama](https://ollama.com/) instalado e em execução no Windows.
- Python 3.10 ou superior.

## Configuração do Ambiente

1. **Baixar o modelo de embeddings no Ollama:**

```powershell
ollama pull nomic-embed-text
```

2. **Criar e ativar o ambiente virtual (venv):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Instalar as dependências:**

3.1 Criei um arquivo `requirements.txt` com o texto:

```text
ollama>=0.1.0
```

3.2 Em seguida fiz o chamado através do terminal:

```powershell
pip install -r requirements.txt
```

4. **Após montar o código no `ollamaapp.py`, fiz a execução:**

```powershell
python ollamaapp.py
```