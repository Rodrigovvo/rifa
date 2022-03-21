### Pré-requisitos:

- Docker
- Docker-compose

# Trabalhando com o projeto:

#### GitHub - clone do projeto 

```bash
git clone https://github.com/Rodrigovvo/rifa
```

#### Configure o arquivo .env

```bash
cp .env.example .env
```

#### Executando a aplicação pela primeira vez

É necessário criar o banco de dados antes das aplicações (*web* e *frontend*).

Em um terminal suba o baco de dados:

```bash
docker-compose up bd 
```

Em um outro terminal rode a migração do Django e popule com os dados básicos:

```bash
sudo docker-compose run --rm web python manage.py migrate
```

Depois de rodar a migração pode derrubar o database:

```bash
sudo docker-compose down
```

E agora pode subir o projeto normalmente:

```bash
sudo docker-compose up
```

Os endereços e portas das aplicações são:

Backend - Django:
```bash
http://localhost:8080
```

#### Executando a aplicação

Depois de criado o ambiente com o banco de dados é só subir normalmente:

```bash
sudo docker-compose up
```

No desenvolvimento do backend (Django), não é necessário subir o frontend.
Para subir somente a aplicação web, execute:

```bash
sudo docker-compose up web
```

# Observações

#### Executando comandos do framework Django:

Para executar qualquer comando do Django (startapp, createsuperuser, makemigrations, populate_db, etc) deve considerar se a aplicação está *no ar* ou não.

Se o service **web** estiver *no ar* e *rodando* corretamente, basta utilizar o próprio service para executar o comando desejado.
Exemplos:

```bash
sudo docker-compose exec web python manage.py startapp {novo_app}
sudo docker-compose exec web python manage.py makemigrations
sudo docker-compose exec web python manage.py migrate
```

Se o service **web** não estiver *no ar* ou com *erro de execução*, deve-se executar o comando desejado em um novo service.
Exemplos:

```bash
sudo docker-compose run --rm web python manage.py startapp {novo_app}
sudo docker-compose run --rm web python manage.py makemigrations
sudo docker-compose run --rm web python manage.py migrate
```

#### Permissões ao arquivos criados utilizando o docker-compose

Ao executar comandos utilizando **docker-compose** que geram novos arquivos, é necessário alterar as configurações de permissionamento dos arquivos criados utilizando o comando linux **chown**. Na raiz do projeto execute o comando abaixo:

```bash
sudo chown -R $USER:$USER ./
```
