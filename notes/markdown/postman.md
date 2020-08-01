## Install Postman


```bash
#!/bin/bash
# Get postman app
wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
sudo tar -xzf postman.tar.gz -C /opt
sudo ln -s /opt/Postman/Postman /usr/bin/postman

#Create a Desktop Entry
cat > ~/.local/share/applications/postman.desktop <<EOL
[Desktop Entry]
Encoding=UTF-8
Name=Postman
Exec=postman
Icon=/opt/Postman/app/resources/app/assets/icon.png
Terminal=false
Type=Application
Categories=Development;
EOL

```


### Get started

* [Swagger OPEN API](https://swagger.io/docs/specification/about/)

* [Swagger Stackstorm](https://github.com/StackStorm/st2apidocs/blob/master/openapi.yaml)

* [JSON2YAML](https://www.json2yaml.com/)

* Read the documentation to get an API KEY [Postman integrations dashboard](https://docs.api.getpostman.com/)

* To update an existing collection, retrieve the `collection_uid` and `collection_id` by submitting a `GET` request using the [Postman API](https://docs.api.getpostman.com/#3190c896-4216-a0a3-aa38-a041d0c2eb72). 

