##Imagen Base
FROM python:3.10.4-slim-bullseye

##Setear VAriables de Entorno

#Desabilita el checkeo de version de pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
#Indica a python que no indique los archivo pyc, util en entornos de produccion, ahorrar espacio
ENV PYTHONDONTWRITEBYTECODE 1
#Ejecucion sin almacenamiento en buffer
ENV PYTHONUNBUFFERED 1

##Setear directorio de trabajo en el contenedor docker
WORKDIR /code

##Instalar depedencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt


#Copiar el proyecto
COPY . .