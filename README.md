# RestAppExample
Example REST Application 

# Testing

### Create environment variables:
`superuser.env`
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin
```

and `postgres.env`:
```
POSTGRES_DB=postgres
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### Build docker images for the services
```
docker-compose -f docker/docker-compose.yml build
```

### Run the system
Specifying the number N of REST server instances.
```
docker-compose -f docker/docker-compose.yml up --scale web=N
```

### Run tests
```
export $(cat superuser.env | xargs)
cd qa
SERVER_URL=http://localhost:8000/ bash test.sh
```