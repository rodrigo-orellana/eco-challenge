#!/bin/bash
#Exit immediately if a command exits with a non-zero exit status.                               
set -e
echo
echo "Iniciando intall python."
##
#   Instala Python  
##
echo
echo "actualizando repo..."
apt-get update

echo "instalación ubuntu python ..."
apt-get install -y python3-pip
#				\
#                   python-dev \
#                   python-pip 
#		   \
#                   python-software-properties

echo
echo "preparando para instalar packetes python ..."
mkdir -p /home/vagrant/.pip_download_cache
# varliables de instalacion
export PIP_DOWNLOAD_CACHE=/home/vagrant/.pip_download_cache
export VIRTUALENV=/home/vagrant/env
# instalaciòn de virtualización python
pip3 install -U pip virtualenv
# creación VIRTUALENV
virtualenv --system-site-packages $VIRTUALENV
# Agrego variable de entorno requerida por el servicio. linea exta al final de archivo activate
echo -e "\nexport AMBIENTE=localhost" >> $VIRTUALENV/bin/activate
# uso del venv
source $VIRTUALENV/bin/activate
# creamos archivo requirements
echo -e "sanic-restplus==0.4.1\npymongo==3.9.0\ndnspython==1.16.0" > requirements.txt
# pip install de requerimientos
pip3 install -r requirements.txt
if [ $? -gt 0 ]; then
    echo 2> 'falla instalación de requirements.txt'
    exit 1
fi

echo
echo "Instalaciòn finalizada"
echo
exit 0
