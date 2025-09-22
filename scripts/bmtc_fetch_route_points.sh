#!/bin/bash
set -e

PROJECT_DIR=/home/traffic_kowshik/code/traffic-kowshik/traffic-data-bengaluru
LOG_DIR=$PROJECT_DIR/logs
VENV=$PROJECT_DIR/.venv

source $VENV/bin/activate

mkdir -p $LOG_DIR
cd $PROJECT_DIR

echo "=== Run $(date '+%Y-%m-%d %H:%M:%S') ===" >> $LOG_DIR/bmtc_fetch_route_points.log
$VENV/bin/python -m cli bmtc_fetch_route_points >> $LOG_DIR/bmtc_fetch_route_points.log 2>&1

tail -n 1000 $LOG_DIR/bmtc_fetch_route_points.log > $LOG_DIR/bmtc_fetch_route_points.tmp
mv $LOG_DIR/bmtc_fetch_route_points.tmp $LOG_DIR/bmtc_fetch_route_points.log
