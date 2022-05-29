# RestAppExample
Example REST Application 

# Testing

### Build server docker image:
```
docker build . -f .\docker\Dockerfile -t app-server
```

### Create `superuser.env`:
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin
```

### Run server
```
docker run -p 8000:8000 -w /workspace --env-file superuser.env --rm -d docker.io/library/app-server bash qa/start_test_server.sh
```

### Run tests
```
export $(cat superuser.env | xargs)
cd qa
SERVER_URL=http://localhost:8000/ bash test.sh
```