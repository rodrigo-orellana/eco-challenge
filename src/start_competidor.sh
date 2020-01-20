#!/bin/bash
source /home/vagrant/env/bin/activate; nohup python3 /vagrant/competidores/sanic_rest.py </dev/null >/dev/null 2>&1 & sleep 1
