docker build --tag=friendlyhello .
docker run --rm -p 4000:80 --name fh friendlyhello
docker rmi friendlyhello
pause
