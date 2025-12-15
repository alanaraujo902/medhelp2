# MedEvolve - Sistema de Evolução Médica com IA

Este repositório contém o código-fonte completo para o **MedEvolve**, um sistema de evolução médica que utiliza IA para formatar texto livre em evoluções estruturadas, com base em modelos altamente configuráveis.

O projeto é dividido em duas partes principais:
- **Backend**: Uma API construída com Python e FastAPI.
- **Frontend**: Uma aplicação web construída com TypeScript, React, Next.js 15 e Tailwind CSS.

---

## Arquitetura e Decisões Técnicas

O sistema foi projetado para ser modular, escalável e fácil de manter, seguindo as melhores práticas de desenvolvimento de software.

### Backend (FastAPI)

- **Estrutura de Projeto**: O backend segue uma estrutura de projeto limpa, separando `api`, `core`, `models`, `schemas`, `services` e `utils`. Isso promove a separação de responsabilidades e facilita a navegação e manutenção do código.
- **Modelos e Schemas (Pydantic)**: Utiliza Pydantic para validação de dados, garantindo que os dados que entram e saem da API estejam sempre corretos e consistentes. Os `models` representam a lógica de negócio interna, enquanto os `schemas` definem os contratos da API.
- **Injeção de Dependência**: FastAPI é usado para gerenciar dependências de serviços, como o `template_service` e `perplexity_service`, tornando o código mais testável e desacoplado.
- **Integração com IA (Perplexity)**: O `perplexity_service` abstrai a comunicação com a API da Perplexity. Ele inclui um mecanismo de **fallback** que gera uma evolução básica caso a chave da API não esteja configurada, garantindo que a aplicação continue funcional.
- **CORS**: Configurado para permitir a comunicação com o frontend, com uma lista de origens permitidas que pode ser facilmente estendida.

### Frontend (Next.js 15)

- **Estrutura de Projeto**: Utiliza o App Router do Next.js 15, com uma organização de pastas que separa `components`, `lib` (API, utils), `store` e `types`.
- **Gerenciamento de Estado (Zustand)**: Zustand foi escolhido por sua simplicidade, performance e por evitar o excesso de boilerplate comum em outras bibliotecas. O `wizardStore` gerencia todo o estado do processo de configuração do modelo de forma centralizada.
- **Componentização (React & Tailwind CSS)**: A interface é construída com componentes reutilizáveis (em `src/components/ui`), estilizados com Tailwind CSS para um desenvolvimento rápido e consistente. A biblioteca `clsx` e `tailwind-merge` são usadas para um gerenciamento de classes CSS robusto.
- **Tipagem (TypeScript)**: O projeto é totalmente tipado, garantindo segurança e melhorando a experiência de desenvolvimento. Todos os tipos compartilhados entre frontend e backend estão definidos em `src/types/index.ts`.
- **Comunicação com API (Axios)**: Um cliente Axios (`src/lib/api.ts`) centraliza todas as chamadas à API do backend, facilitando a manutenção e o tratamento de erros.

---

## Guia de Implementação e Execução

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento localmente.

### Pré-requisitos

- Node.js (v18 ou superior)
- pnpm (ou npm/yarn)
- Python (v3.9 ou superior)
- `pip` e `venv`

### 1. Configuração do Backend

Navegue até a pasta do backend e configure o ambiente virtual:

```bash
cd medical-evolution-system/backend
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` a partir do exemplo. Se você tiver uma chave da API Perplexity, adicione-a aqui.

```bash
cp .env.example .env
# Abra o arquivo .env e adicione sua chave, se disponível
# PERPLEXITY_API_KEY=sua_chave_aqui
```

Inicie o servidor do backend:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

O backend estará disponível em `http://localhost:8000`.

### 2. Configuração do Frontend

Em um novo terminal, navegue até a pasta do frontend e instale as dependências:

```bash
cd medical-evolution-system/frontend
pnpm install
```

Crie um arquivo `.env.local` a partir do exemplo. Por padrão, ele já aponta para o backend local.

```bash
cp .env.example .env.local
```

Inicie o servidor de desenvolvimento do frontend:

```bash
pnpm dev
```

O frontend estará disponível em `http://localhost:3000`.

### 3. Utilização

- **Página Principal (`/`)**: Acesse para começar a escrever e gerar evoluções. Você pode selecionar um modelo pronto ou um dos seus modelos salvos.
- **Configurar Modelo (`/configure`)**: Siga o assistente de 5 passos para criar um modelo de evolução totalmente personalizado.
- **Gerenciar Modelos (`/templates`)**: Visualize, gerencie e exclua seus modelos salvos.

---

## Estrutura de Diretórios

```
medical-evolution-system/
├── backend/
│   ├── app/
│   │   ├── api/            # Endpoints da API
│   │   ├── core/           # Configurações centrais
│   │   ├── models/         # Modelos de domínio
│   │   ├── schemas/        # Schemas Pydantic (contratos da API)
│   │   ├── services/       # Lógica de negócio
│   │   └── main.py         # Ponto de entrada da aplicação FastAPI
│   ├── requirements.txt  # Dependências Python
│   └── .env.example      # Exemplo de variáveis de ambiente
├── frontend/
│   ├── src/
│   │   ├── app/            # Páginas e layouts (App Router)
│   │   ├── components/     # Componentes React (UI, layout, wizard)
│   │   ├── lib/            # Funções utilitárias e cliente API
│   │   ├── store/          # Gerenciamento de estado (Zustand)
│   │   └── types/          # Definições TypeScript
│   ├── package.json      # Dependências e scripts Node.js
│   └── .env.local.example # Exemplo de variáveis de ambiente
└── README.md             # Este arquivo
```
