#!/bin/bash
set -e

PROJECT_DIR="$HOME/code/traffic-kowshik/traffic-data-bengaluru"
LOG_DIR=$PROJECT_DIR/logs/namma_metro
VENV=$PROJECT_DIR/.venv

source $VENV/bin/activate

mkdir -p $LOG_DIR
cd $PROJECT_DIR

echo "=== Run $(date '+%Y-%m-%d %H:%M:%S') ===" >> $LOG_DIR/fetch_ridership.log
$VENV/bin/python -m cli namma_metro_fetch_ridership >> $LOG_DIR/fetch_ridership.log 2>&1

tail -n 100 $LOG_DIR/fetch_ridership.log > $LOG_DIR/fetch_ridership.tmp
mv $LOG_DIR/fetch_ridership.tmp $LOG_DIR/fetch_ridership.log
