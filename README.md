# Projeto Flask Frete - Docker Compose

## Descrição

Aplicação Flask containerizada que se conecta a um banco de dados MySQL, orquestrada com Docker Compose, pronta para ambientes de desenvolvimento e produção, seguindo boas práticas de segurança, organização e otimização.

---

## Estrutura do Projeto

```
my-flask-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .env
├── docker-compose.yml
├── docker-compose.dev.yml
├── README.md
```

---

## Como Executar

### 1. Desenvolvimento

```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

- O código é montado como volume para hot reload.
- O banco de dados fica acessível na porta 3306.

### 2. Produção

```sh
docker-compose -f docker-compose.yml up --build -d
```

- O código não é montado como volume.
- O banco de dados não expõe porta externa.
- Rede e volume exclusivos para produção.

---

## Variáveis de Ambiente

Configure o arquivo `.env` na raiz do projeto:

```
FLASK_PORT=5002
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=mydatabase
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_PORT=3306
```

---

## Otimizações no Dockerfile

- **Imagem leve:** Baseada em `python:3.12-alpine`.
- **Sem root:** Executa como `USER nobody`.
- **Apenas dependências essenciais:** Instaladas via `requirements.txt`.
- **Sem cache:** Uso de `--no-cache-dir` no pip.
- **Exposição mínima:** Apenas porta 5002.

---

## Segurança Adotada

- **Usuário não-root** no container.
- **Banco de dados não exposto** em produção.
- **Redes separadas** para dev e prod.
- **Volumes nomeados** para persistência e backup.
- **Imagem enxuta** e sem dependências desnecessárias.

---

## Comunicação entre Containers

- **Rede Docker interna** (`app-net` ou `dev-net`), garantindo que apenas os containers do mesmo ambiente se comuniquem.
- **Banco de dados acessível apenas pela aplicação** em produção.

---

## Boas Práticas Aplicadas

- **Volumes nomeados** para persistência do banco.
- **Montagem do código** apenas em desenvolvimento.
- **Isolamento de ambientes** por rede e volume.
- **Backup do volume do banco:**
  ```sh
  docker run --rm -v my-flask-app_db-data:/volume -v %cd%:/backup alpine tar czf /backup/backup.tar.gz -C /volume .
  ```

---

## Publicação da Imagem no Docker Hub

1. Faça login:
   ```sh
   docker login
   ```
2. Build e push:
   ```sh
   docker build -t matheushcg04/flask-frete:1.0 ./app
   docker push matheushcg04/flask-frete:1.0
   ```
3. [Link para a imagem no Docker Hub](https://hub.docker.com/)

---

## Análise de Segurança

Execute:
```sh
docker scout cves seu-usuario/flask-frete:1.0
```
Inclua o resultado ou print no repositório.

---

## Troca de Ambiente

- **Desenvolvimento:**  
  `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build`
- **Produção:**  
  `docker-compose -f docker-compose.yml up --build -d`
- **Ajuste variáveis no `.env` conforme necessário.**

---
