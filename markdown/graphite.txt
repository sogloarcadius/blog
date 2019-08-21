docker run -d\
 --name graphite\
 --restart=always\
 -p 8080:80\
 -p 2003-2004:2003-2004\
 -p 2023-2024:2023-2024\
 -p 8125:8125/udp\
 -p 8126:8126\
 graphiteapp/graphite-statsd
 
 
 while true; do echo -n "example:$((RANDOM % 100))|c" | nc -w 1 -u 127.0.0.1 8125; done
 
 
  while true; do echo -n "stackstorm:$((RANDOM % 100))|c" | nc -w 1 -u  192.168.246.122 80; done

 https://hub.docker.com/r/graphiteapp/graphite-statsd/