# Python Microservice Development

## Notes taken from the book Python Microservices Development

see `src` and `tests`

## Dockerize a flask based service

see `flask_docker`

## Build a gRPC based microservice, security and best practices

this is based on the tutorial:
<https://realpython.com/python-microservices-grpc/#how-small-is-micro>

it takes a very thorough approach, explaining:

- why gRPC is a preference for many companies
- how to define types and services in protobuf
- how to dockerize the microservice
- how to orchestrate the services in Kubernetes
- how to organise protobuf (the "headers") cross multiple microservices
in a company scale
- how to deal with TLS and security

consider it a sibling tutorial to the `gomicro` project
I had created (which was based on JetBrain's webinar)
