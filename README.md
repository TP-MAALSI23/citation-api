# Build for x86 arch from a Mac M1

docker buildx build .  --platform linux/amd64 -t citation-api:0.1.0-x86

# First install

Its a two step process.

## Init SSL certs

This will boot up an nginx server with ACME webroot challenge minimal config and use cerbtot to fetch a set of SSL certificates.

```sh
docker compose -f init-ssl-compose.yml up -d nginx
docker compose -f init-ssl-compose.yml up certbot
docker compose -f init-ssl-compose.yml kill
```

## Application start up

```sh
docker compose up -d
```

# Renew SSL cert

```sh
docker compose up certbot
```

# .env content

APP_ENV
APP_PORT
DOMAIN
EMAIL