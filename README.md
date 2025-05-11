# 🚌 Controle de Acesso - Registro de Ônibus

Este é um aplicativo Flask simples para registrar entradas e saídas de ônibus, colaboradores e visitantes na empresa. Os registros são salvos em um banco de dados SQLite e podem ser exportados para Excel.

---

## 🚀 Funcionalidades

- Formulário para registro de entradas/saídas
- Consulta automática de nome por registro (funcionários)
- Listagem de registros
- Exportação para Excel

---

## 📦 Instalação

Clone este repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
python app.py
```

Acesse a aplicação em [http://localhost:5000](http://localhost:5000)

---

## 📂 Estrutura do Projeto

```
├── app.py
├── onibus.db                # Banco SQLite
├── requirements.txt         # Dependências
├── static/
│   └── css/
│       └── style.css        # Estilos
├── templates/
│   ├── registro.html        # Formulário de registro
│   └── visualizar.html      # Lista de registros
└── static/downloads/        # Pasta onde Excel será salvo
```

---

## 📄 Requisitos

- Python 3.7+
- Flask
- Pandas
- openpyxl

---

## 📤 Exportação

- Acesse `/visualizar` para ver os registros.
- Clique em **Exportar para Excel** para gerar um arquivo `.xlsx`.

---

## ✅ Sugestões Futuras

- Filtro por data/categoria
- Autenticação de usuários
- Upload de CSV para importar funcionários

---

Desenvolvido com ❤️ usando Flask.
#




## Autores

- [@Rodrigo Rodrigues](https://www.instagram.com/imrodrigorodrigues)


## Funcionalidades

- Preview em tempo real
- Modo tela cheia
- Multiplataforma

