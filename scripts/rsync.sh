#!/bin/bash
set -e

project_dir=/home/traffic_kowshik/code/traffic-kowshik/traffic-data-bengaluru
log_dir=$project_dir/logs

/usr/bin/gsutil -m rsync -r \
  "$HOME/code/traffic-kowshik/traffic-data-bengaluru/data/" \
  gs://traffic-kowshik-bmtc/traffic-data-bengaluru/data/ >> $log_dir/rsync.log 2>&1
