
# Proxy during build

sudo docker-compose build --build-arg http_proxy="http://proxy.rennes.lab:8080"  --build-arg https_proxy="http://proxy.rennes.lab:8080" django

