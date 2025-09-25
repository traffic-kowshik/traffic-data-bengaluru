#!/bin/bash
set -e

project_dir=$HOME/code/traffic-kowshik/traffic-data-bengaluru
data_dir=$project_dir/data
log_dir=$project_dir/logs

cloud_dir="gs://traffic-kowshik-private/traffic-data-bengaluru/data/"

GSUTIL=$(command -v gsutil)
"$GSUTIL" -m rsync -r "$data_dir/" "$cloud_dir" >> "$log_dir/rsync.log" 2>&1
