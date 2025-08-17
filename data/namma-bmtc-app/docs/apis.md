# APIs

## API 1. Route points

Takes `route_id` as input and returns geo-locations of the route to be taken in response. There isn't an identifier for the bus stop in this dataset. Instead it'points are at regular distance along the route.

```bash
curl -X POST 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/RoutePoints' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  -d '{"routeid":3796}'
```

Sample response

```json
{
    "data": [
        {
            "latitude": "12.97751",
            "longitude": "77.57141",
            "responsecode": 200
        },
        {
            "latitude": "12.97749",
            "longitude": "77.57098",
            "responsecode": 200
        },
        {
            "latitude": "12.905319",
            "longitude": "77.543217",
            "responsecode": 200
        },
        {
            "latitude": "12.905319",
            "longitude": "77.543217",
            "responsecode": 200
        }
    ],
    "Message": "Success",
    "Issuccess": true,
    "exception": null,
    "RowCount": 560,
    "responsecode": 200
}
```

## API 2. List vehicles

Returns ID and registration number of vehicles which match the vehicle number passed in the argument. Ex: `0007` returns `KA53F0007` and `KA57F0007`.

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/ListVehicles' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"vehicleRegNo":"0007"}'
```

Sample response

```json
{
    "data": [
        {
            "vehicleid": 19100,
            "vehicleregno": "KA53F0007",
            "responsecode": 200
        },
        {
            "vehicleid": 18830,
            "vehicleregno": "KA57F0007",
            "responsecode": 200
        }
    ],
    "Message": "Success",
    "Issuccess": true,
    "exception": null,
    "RowCount": 2,
    "responsecode": 200
}
```

## API 3. Trip Details

Takes a `vehicle_id` as input and returns route details of the current trip along with the live location of the vehicle.

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/VehicleTripDetails_v2' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"vehicleId":21670}'
```

Sample response

```json
{
    "RouteDetails": [
        {
            "rowid": 1,
            "tripid": 68043555,
            "routeno": "210-N",
            "routename": "KBS-UTH",
            "busno": "KA57F0614",
            "tripstatus": "Running",
            "tripstatusid": "1",
            "sourcestation": "Kempegowda Bus Station",
            "destinationstation": "Uttarahalli Bus Stand",
            "servicetype": "Non AC/Ordinary",
            "webservicetype": "Non-AC",
            "servicetypeid": 72,
            "lastupdatedat": "17-08-2025 12:33:18",
            "stationname": "Uttarahalli Bus Stand",
            "stationid": 22569,
            "actual_arrivaltime": null,
            "etastatus": "12:41",
            "etastatusmapview": "12:41",
            "latitude": 12.90535,
            "longitude": 77.54327,
            "currentstop": "",
            "laststop": "Gowdanapalya (Towards Uttarahalli)",
            "weblaststop": "Gowdanapalya",
            "nextstop": "Chikkallasandra Aralimara (Towards Uttarahalli)",
            "currlatitude": 12.911503,
            "currlongitude": 77.555923,
            "sch_arrivaltime": "12:48",
            "sch_departuretime": "12:48",
            "eta": "12:41",
            "actual_arrivaltime1": null,
            "actual_departudetime": null,
            "tripstarttime": "11:50",
            "tripendtime": "12:55",
            "routeid": 3796,
            "vehicleid": 21670,
            "responsecode": 200,
            "lastreceiveddatetimeflag": 1,
            "srno": 1584405201,
            "tripposition": 1,
            "stopstatus": 1,
            "stopstatus_distance": 1.53,
            "lastetaupdated": "2025-08-17T12:41:00",
            "minstopstatus_distance": 0.38
        }
    ],
    "LiveLocation": [
        {
            "latitude": 12.911503,
            "longitude": 77.555923,
            "location": "Gowdanapalya (Towards Kadirenahalli)",
            "lastrefreshon": "17-08-2025 12:33:18",
            "nextstop": "Chikkallasandra Aralimara (Towards Uttarahalli)",
            "previousstop": "Prarthana School (Towards Uttarahalli)",
            "vehicleid": 21670,
            "vehiclenumber": "KA57F0614",
            "routeno": "210-N",
            "servicetypeid": 72,
            "servicetype": "Non AC/Ordinary",
            "heading": 241.00,
            "responsecode": 200,
            "trip_status": 1,
            "lastreceiveddatetimeflag": 1
        }
    ],
    "Message": "Success",
    "Issuccess": true,
    "exception": null,
    "RowCount": 29,
    "responsecode": 200
}
```

## API 4. Path Details

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/GetPathDetails' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"data":[{"tripId":68076592,"fromStationId":20921,"toStationId":21166},{"tripId":68068463,"fromStationId":21166,"toStationId":21545}]}'

{
    "data": [
        {
            "tripId": 68076592,
            "routeId": 1663,
            "routeNo": "KBS-3A",
            "stationId": 20921,
            "stationName": "ಕೆಂಪೇಗೌಡ ಬಸ್ ನಿಲ್ದಾಣ (ಟುವರ್ಡ್ಸ್  ನಿರ್ಗಮನ)",
            "latitude": 12.97751,
            "longitude": 77.57141,
            "eta": "",
            "sch_arrivaltime": "08/17/2025 13:30:00",
            "sch_departuretime": "08/17/2025 13:30:00",
            "actual_arrivaltime": "",
            "actual_departuretime": "",
            "distance": 0,
            "duration": null,
            "isTransfer": false
        },
        {
            "tripId": 68068463,
            "routeId": 2860,
            "routeNo": "13-F",
            "stationId": 21545,
            "stationName": "ಜಯನಗರ ಬಸ್ ನಿಲ್ದಾಣ (ಟುವರ್ಡ್ಸ್  ಸಂಗಂ ವೃತ್ತ)",
            "latitude": 12.92802,
            "longitude": 77.58364,
            "eta": "",
            "sch_arrivaltime": "08/17/2025 14:12:00",
            "sch_departuretime": "08/17/2025 14:12:00",
            "actual_arrivaltime": "",
            "actual_departuretime": "",
            "distance": 0,
            "duration": null,
            "isTransfer": false
        }
    ],
    "message": "Success",
    "issuccess": true,
    "exception": null,
    "rowCount": 0,
    "responsecode": 200
}
```

## API 5. Route Details

Takes a `route_id` as input and returns detils of the route along with live vehicles on that route.

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/SearchByRouteDetails_v4' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"routeid":2116,"servicetypeid":0}'
```

Sample response

```json
{
    "up": {
        "data": [
            {
                "routeid": 3796,
                "stationid": 20921,
                "stationname": "Kempegowda Bus Station",
                "from": "Kempegowda Bus Station",
                "to": "Uttarahalli Bus Stand",
                "routeno": "210-N",
                "distance_on_station": 0,
                "centerlat": 12.97751,
                "centerlong": 77.57141,
                "responsecode": 200,
                "isnotify": 0,
                "vehicleDetails": [
                    {
                        "vehicleid": 21635,
                        "vehiclenumber": "KA53F0124",
                        "servicetypeid": 72,
                        "servicetype": "Non AC/Ordinary",
                        "centerlat": 12.907606,
                        "centerlong": 77.540665,
                        "eta": "",
                        "sch_arrivaltime": "12:55",
                        "sch_departuretime": "12:55",
                        "actual_arrivaltime": "",
                        "actual_departuretime": "",
                        "sch_tripstarttime": "12:55",
                        "sch_tripendtime": "12:55",
                        "lastlocationid": 0,
                        "currentlocationid": 22198,
                        "nextlocationid": 0,
                        "currentstop": null,
                        "nextstop": null,
                        "laststop": null,
                        "stopCoveredStatus": 1,
                        "heading": 304,
                        "lastrefreshon": "17-08-2025 13:36:50",
                        "lastreceiveddatetimeflag": 0,
                        "tripposition": 1
                    }
                ]
            }
        ],
        "mapData": [
            {
                "vehicleid": 21778,
                "vehiclenumber": "KA57F4893",
                "servicetypeid": 72,
                "servicetype": "Non AC/Ordinary",
                "centerlat": 12.973747,
                "centerlong": 77.586714,
                "eta": "2025-08-17 14:13:00",
                "sch_arrivaltime": "14:18",
                "sch_departuretime": "14:18",
                "actual_arrivaltime": "",
                "actual_departuretime": "",
                "sch_tripstarttime": "13:20",
                "sch_tripendtime": "13:20",
                "lastlocationid": 0,
                "currentlocationid": 20939,
                "nextlocationid": 0,
                "currentstop": null,
                "nextstop": null,
                "laststop": null,
                "stopCoveredStatus": 0,
                "heading": 132,
                "lastrefreshon": "17-08-2025 13:36:34",
                "lastreceiveddatetimeflag": 0,
                "tripposition": 1
            }
        ]
    },
    "down": {},
    "message": "Success",
    "issuccess": true,
    "exception": null,
    "rowCount": 0,
    "responsecode": 200
}
```
