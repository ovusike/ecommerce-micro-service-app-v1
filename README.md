# Ecommerce Microservice App

This repository hosts the backend service of an Ecommerce Microservice Application. The service is written in Python using the Flask framework and can be built and run inside a Docker container.

## Getting Started

These instructions will get you a copy of the backend service up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Docker installed on your machine. You can download Docker [here](https://www.docker.com/get-started).

### Clone the Repository

First, clone this repository onto your local machine by using the following command:

```
git clone https://github.com/cvamsikrishna11/ecommerce-micro-service-app.git
```

### Navigate to the Directory
Change your directory to ecommerce-micro-service-app:

```
cd ecommerce-micro-service-app
```

### Building the Docker Image
To build the Docker image from the Dockerfile, use this command:

```
docker build -t ecommerce-backend .
```

### Running the Docker Container
Start a Docker container from the image:

```
docker run -d -p 5000:5000 --name ecommerce-backend-container ecommerce-backend
```

The Flask application inside the Docker container will start and listen on port 5000.

### Testing the Application
Now, your backend Flask application should be running at http://localhost:5000. You can send HTTP requests to this URL to interact with the application.

If you deploy it in an EC2 instance, enable the security group of instance to accept taffic on port 5000 and access the
backend app with Postman app on http://instance-public-ip:5000.

### Endpoints
The following endpoints are available:

- GET / : Returns a welcome message.
- POST /signup : Creates a new user. Expects a JSON payload with 'username' and 'password' fields.
- POST /signin : Authenticates a user. Expects a JSON payload with 'username' and 'password' fields.
