# Shop API
Flask application that creates an endpoint for management of products in a shop

## Requirements
- Python 3.8
- Docker
- Flask
- Flask-Restx

All requirements are installed from requirements.txt during docker container build.

## Build
### Docker Compose
Clone repo and then execute the following code in root directory of application
```
docker-compose up -d --build
```

## Test
Run the following commands and ensure tests past
```
docker-compose exec backend pytest
```
Navigate to the below in brower to ensure server is operational:
```
http://localhost:5001/ping
```

## Swagger
For an overview of endpoints go to:
```
http://127.0.0.1:5001/doc
```
