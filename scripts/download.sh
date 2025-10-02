#!/bin/bash
set -e

# Directories
project_dir="$HOME/code/traffic-kowshik/traffic-data-bengaluru"
data_dir="$project_dir/data"
log_dir="$project_dir/logs"
cloud_dir="gs://traffic-kowshik-private/traffic-data-bengaluru/data/"

# Ensure both data and log directory exists
mkdir -p "$data_dir"
mkdir -p "$log_dir"

# Dynamically find gsutil
GSUTIL=$(command -v gsutil)
if [ -z "$GSUTIL" ]; then
    echo "Error: gsutil not found in PATH" >&2
    exit 1
fi
echo "Using gsutil at: $GSUTIL"

# Download: cloud -> local
echo "Downloading data from Google Cloud Storage..."
if ! "$GSUTIL" -m rsync -r "$cloud_dir" "$data_dir/" >>"$log_dir/download.log" 2>&1; then
    echo "gsutil download failed" >&2
    exit 1
fi

echo "Download complete."
