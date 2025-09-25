#!/bin/bash
set -e

# Directories
project_dir="$HOME/code/traffic-kowshik/traffic-data-bengaluru"
data_dir="$project_dir/data"
log_dir="$project_dir/logs"
cloud_dir="gs://traffic-kowshik-private/traffic-data-bengaluru/data/"

# Ensure log directory exists
mkdir -p "$log_dir"

# Dynamically find gsutil
GSUTIL=$(command -v gsutil)
if [ -z "$GSUTIL" ]; then
    echo "Error: gsutil not found in PATH" >&2
    exit 1
fi
echo "Using gsutil at: $GSUTIL"

# Upload: local -> cloud
echo "Uploading data to Google Cloud Storage..."
"$GSUTIL" -m rsync -r "$data_dir/" "$cloud_dir" >> "$log_dir/upload.log" 2>&1 || {
    echo "gsutil upload failed" >&2
    exit 1
}

echo "Upload complete."
