#bin/sh

python3 web_driver_v.py
cd /mnt/c/pentaho-server-ce-7.1.0.0-12/pdi-ce-9.0.0.0-423/data-integration
./kitchen.sh -file=/mnt/d/ASUS/Documents/PROYECTOS/selenium/job_bd.kjb -level=Detail > /mnt/d/ASUS/Documents/PROYECTOS/selenium/logs/ejecucion.log
