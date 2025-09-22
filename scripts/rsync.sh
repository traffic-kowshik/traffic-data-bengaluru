#!/bin/bash
set -e

/usr/bin/gsutil -m rsync -r \
  "$HOME/code/traffic-kowshik/traffic-data-bengaluru/data/" \
  gs://traffic-kowshik-bmtc/traffic-data-bengaluru/data/
