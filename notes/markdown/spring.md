## Create new project


```bash
# use the spring starter api

curl https://start.spring.io/starter.tgz -d style=web -d name=simple | tar -xzvf -

```

## Spring Boot 


```bash
#run eclipse project from cli

mvn spring-boot:run

## generate jar file into {eclipseproject}/target/

mvn clean install

## run app

java -jar target\spring-boot-service.jar

```
