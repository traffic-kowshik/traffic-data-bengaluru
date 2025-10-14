#!/bin/bash
set -e

PROJECT_DIR="$HOME/code/traffic-kowshik/traffic-data-bengaluru"
LOG_DIR=$PROJECT_DIR/logs
VENV=$PROJECT_DIR/.venv

source $VENV/bin/activate

mkdir -p $LOG_DIR
cd $PROJECT_DIR

echo "=== Run $(date '+%Y-%m-%d %H:%M:%S') ===" >> $LOG_DIR/bmtc_fetch_route_details_v2.log
$VENV/bin/python -m cli bmtc_fetch_route_details_v2 >> $LOG_DIR/bmtc_fetch_route_details_v2.log 2>&1

tail -n 100 $LOG_DIR/bmtc_fetch_route_details_v2.log > $LOG_DIR/bmtc_fetch_route_details_v2.tmp
mv $LOG_DIR/bmtc_fetch_route_details_v2.tmp $LOG_DIR/bmtc_fetch_route_details_v2.log

find "$PROJECT_DIR/data/bmtc/raw/route_details_v2" -type f -name "*.json" -exec gzip {} \;
