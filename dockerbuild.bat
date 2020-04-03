$v = 2.3
$name = “saba1”
docker rm --force $name
docker build --tag smartlauncher:$v .
#docker run --publish 80:80 --detach --name $name smartlauncher:$v


#Go into docker

docker run -it --rm --privileged --pid=host  --publish 80:80 smartlauncher:$v
