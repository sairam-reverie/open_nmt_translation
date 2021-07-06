FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
EXPOSE 5000
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


#Default for flask is to listen on localhost only, in this case that would be localhost within the container
#and not localhost of the docker host.

#docker container run --name web -p 5000:80 alpine:3.9 -Here 5000 external port, 80 internal port
#sudo docker container run --name translation_api -p 5000:5000 -d translate_app:version_0.0
#sudo docker build -t translate_app:version_0.1 .

# opennmt/ctranslate2:latest-ubuntu20.04-cuda11.2
# Latest throwing errors - opennmt/ctranslate2:2.1.0-ubuntu20.04-cuda11.2
# Need to include this library in requirements.txt if using python base ctranslate2==2.1.0