# ROTEIRO PROJETO API OCORRÊNCIAS SSPDF

### CRIAÇÃO DO DIRETÓRIO PAI DO PROJETO

```bash
mkdir projeto-ml-api
cd projeto-ml-api
```

### INICIAR O GIT

```bash
git init
```

### INSTALAR / ATIVAR VENV

```bash
python3.12 -m venv venv

source venv/bin/activate
```
### 1.3 Criar estrutura de diretórios

```bash
mkdir src
mkdir src/api
mkdir src/data
mkdir src/models
mkdir src/models
mkdir src/services
mkdir tests
mkdir logs
mkdir artifacts
mkdir artifacts/models
```
### 1.4 Criar arquivos `__init__.py`

```bash
# Windows
type nul > src/__init__.py
type nul > src/api/__init__.py
type nul > src/data/__init__.py
type nul > src/models/__init__.py
type nul > tests/__init__.py

# Mac/Linux
touch src/__init__.py
touch src/api/__init__.py
touch src/data/__init__.py
touch src/models/__init__.py
touch src/schemas/__init__.py
touch src/services/__init__.py
touch tests/__init__.py
```

### 1.5 Criar arquivos de configuração

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
```

### 1.6 Instalar dependências

```bash
pip install -r requirements.txt
```

---