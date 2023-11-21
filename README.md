# Build for x86 arch from a Mac M1

docker buildx build .  --platform linux/amd64 -t citation-api:0.1.0-x86

# First install

You need to fill the .env file check the [env content section](#env-content)
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

set to true to enable debug mode
APP_ENV
default is 3000
APP_PORT  
the domain name to set in the nginx server config
DOMAIN  
EMAIL  