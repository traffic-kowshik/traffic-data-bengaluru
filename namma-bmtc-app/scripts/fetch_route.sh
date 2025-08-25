#!/bin/bash

OUTPUT_FILE="route_details.json"
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/SearchByRouteDetails_v4' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'deviceType: WEB' \
  --data-raw '{"routeid":2116,"servicetypeid":0}' \
  --silent >> "$OUTPUT_FILE"

# Add a newline for separation
echo "" >> "$OUTPUT_FILE"
