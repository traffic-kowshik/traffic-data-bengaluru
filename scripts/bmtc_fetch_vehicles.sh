#!/bin/bash
set -e

project_dir="$HOME/code/traffic-kowshik/traffic-data-bengaluru"
log_dir=$project_dir/logs
venv=$project_dir/.venv

source $venv/bin/activate

mkdir -p $log_dir
cd $project_dir

echo "=== Run $(date '+%Y-%m-%d %H:%M:%S') ===" >> $log_dir/bmtc_fetch_vehicles.log
$venv/bin/python -m cli bmtc_fetch_vehicles >> $log_dir/bmtc_fetch_vehicles.log 2>&1

tail -n 100 $log_dir/bmtc_fetch_vehicles.log > $log_dir/bmtc_fetch_vehicles.tmp
mv $log_dir/bmtc_fetch_vehicles.tmp $log_dir/bmtc_fetch_vehicles.log
