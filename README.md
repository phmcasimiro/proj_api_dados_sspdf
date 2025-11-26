# ROTEIRO PROJETO API OCORRÊNCIAS SSPDF

## 1 SETUP INICIAL DO PROJETO

### 1.1 CRIAÇÃO DO DIRETÓRIO PAI DO PROJETO

```bash
mkdir projeto-ml-api
cd projeto-ml-api
```

### 1.2 INICIAR O GIT

```bash
git init
```

### 1.3 INSTALAR / ATIVAR VENV

```bash
python3.12 -m venv venv

source venv/bin/activate
```
### 1.4 Criar estrutura de diretórios

```bash
mkdir src
mkdir src/api
mkdir src/data
mkdir src/data/etl
mkdir src/data/etl/extractors
mkdir src/data/etl/transformers
mkdir src/data/etl/loaders
mkdir src/models
mkdir src/schemas
mkdir src/services
mkdir tests
mkdir logs
mkdir artifacts
mkdir artifacts/models
```
### 1.5 Criar arquivos `__init__.py`

```bash

# Mac/Linux
touch src/__init__.py
touch src/api/__init__.py
touch src/data/__init__.py
touch src/data/etl/__init__.py
touch src/data/etl/extractors/__init__.py
touch src/data/etl/transformers/__init__.py
touch src/data/etl/loaders/__init__.py
touch src/models/__init__.py
touch src/schemas/__init__.py
touch src/services/__init__.py
touch tests/__init__.py
```

### 1.6 Criar arquivos de configuração

**Criar `.gitignore`:**
```
venv/
__pycache__/
*.pyc
.pytest_cache/
.mypy_cache/
.ruff_cache/
logs/*.log
.env
*.pkl
.DS_Store
```

**Criar `requirements.txt`:**
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.6.0
pytest==7.4.3
pytest-cov==4.1.0
black==24.1.1
ruff==0.1.15
mypy==1.8.0
httpx==0.26.0
scikit-learn==1.4.0
pandas==2.2.0
seaborn==0.13.2
matplotlib==3.7.2
```

### 1.7 Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 2.0 Repositório Github 

### 2.1 Criar o Repositório Vazio no GitHub

Acesse o GitHub no navegador.

Clique no botão "New" (Novo) para criar um novo repositório.

Dê o nome proj_api_dados_sspdf (mesmo nome da sua pasta local).

Defina-o como Public.

Clique em "Create repository".


# 2.2 Conectar repositório remoto

 - O GitHub fornecerá a URL do repositório. Você usará essa URL para conectar sua pasta local.

 - Copie a URL do repositório vazio (use a opção HTTPS).

```bash
git remote add origin https://github.com/phmcasimiro/proj_api_dados_sspdf.git
``` 

### 2.3 Inicializar o repositório local

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 3 Pipeline de Dados

- Download dos dados em  [SSP-DF Ocorrências Policiais](https://www.ssp.df.gov.br/dados-por-regiao-administrativa/)
- Limpeza e consolidação dos dados em arquivo .csv
- Normalização com tabela de Regiões Administrativas e seus respectivos Códigos e tabela de Natureza das Ocorrências e seus respectivos Códigos