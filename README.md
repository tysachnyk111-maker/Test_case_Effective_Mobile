## Проект: nginx (reverse proxy) -> backend

Структура:
`backend/`, `nginx/`, `docker-compose.yml`, `README.md`.

### Как запустить

1. Убедитесь, что установлен Docker и Docker Compose.
2. Перейдите в корень проекта (где лежит `docker-compose.yml`).
3. Выполните:

```bash
docker compose up -d --build
```

### Как проверить результат

Откройте в браузере:
`http://localhost/`

Либо через `curl` (с хоста):

```bash
curl -i http://localhost/
```

Ожидаемый ответ на `/`:
`Hello from Effective Mobile!`

Дополнительно можно посмотреть статусы контейнеров:

```bash
docker ps
```

### Кратко о схеме работы (nginx -> backend)

- Контейнер `backend` слушает `8080` и отвечает на запросы к пути `/`.
- Контейнер `nginx` принимает HTTP-запросы на `80` (наружу) и делает reverse proxy по пути `/` на сервис `backend` (в Docker-сети).
- Порт `8080` наружу не публикуется: доступ к нему есть только внутри Docker-сети.

