#!/bin/bash

source /home/traffic_kowshik/code/traffic-kowshik/traffic-data-bengaluru/.venv/bin/activate
cd /home/traffic_kowshik/code/traffic-kowshik/traffic-data-bengaluru

mkdir -p logs
.venv/bin/python -m cli bmtc_fetch_routes >> logs/bmtc_fetch_routes.log 2>&1

tail -n 1000 logs/bmtc_fetch_routes.log > logs/bmtc_fetch_routes.tmp
mv logs/bmtc_fetch_routes.tmp logs/bmtc_fetch_routes.log
