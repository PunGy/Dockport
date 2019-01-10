#!/bin/bash

service=$1
prefix=""


if [[ $1 = "--help" ]]
then
    echo "This app show you port with url(now only 'localhost') of your docker container
    
    Usage: port container [OPTIONS]
    -p: prefix: prefix of container, should be first option without '-'
    -o: Open in browser (google-chrome)
    -b: Copy url in buffer

    Example: port serve -p test -o

    Shortcuts for containers:
    serve: nginx
    pma: phpmyadmin
    "
    exit
fi
if [ -z $service ]
then
    echo "Enter name of container!"
    exit
fi
if [ $service = 'pma' ]
then
    service="phpmyadmin"
fi
if [ $service = 'serve' ]
then
    service="nginx"
fi

if [[ $2 = "-p" ]]
then
        prefix="$3-"
fi

result=$(docker port $prefix$service | sed -r 's/^[^:]+//')
result=localhost$result

echo $result

while [ -n "$2" ]
do
case "$2" in
-o) google-chrome http://$result > /dev/null 2>&1 ;;
-b) echo $result | xsel -b -i ;;
esac
shift
done

