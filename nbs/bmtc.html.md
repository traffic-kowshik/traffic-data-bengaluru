---
title: BMTC
---




> Bengaluru Metropolitan Transport Corporation (BMTC) is a state-owned public road transport corporation in the Indian city of Bengaluru.



::: {#d0b1b226 .cell 0='h' 1='i' 2='d' 3='e'}
``` {.python .cell-code}
from nbdev.showdoc import *
```
:::


::: {#3fed9355 .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
import string
import json
import time
from pathlib import Path
import datetime

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

import requests
import pandas as pd
```
:::


::: {#0d35502d .cell 0='h' 1='i' 2='d' 3='e'}
``` {.python .cell-code}
# Inside the data directory, there is a directory to store BMTC data.
data_directory = Path('../data/bmtc/')
data_directory.mkdir(exist_ok=True, parents=True)
```
:::



# Routes

> Takes a route text for regex matching and returns matching routes in response.

## Sample request

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/SearchRoute_v2' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  -H 'lan: en' \
  --data-raw '{"routetext":"210"}'
```

## Sample response

```json
{
    "data": [
        {
            "union_rowno": 2,
            "row": 1,
            "routeno": "210-A",
            "responsecode": 200,
            "routeparentid": 7426
        },
        {
            "union_rowno": 2,
            "row": 3,
            "routeno": "210-AA",
            "responsecode": 200,
            "routeparentid": 7427
        }
    ],
    "Message": "Success",
    "Issuccess": true,
    "exception": null,
    "RowCount": 53,
    "responsecode": 200
}
```

::: {#aad284bf .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def fetch_routes(pattern: str = ""):
    logging.info(f"Fetching routes for pattern = '{pattern}'")
    url = "https://bmtcmobileapi.karnataka.gov.in/WebAPI/SearchRoute_v2"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "lan": "en"
    }

    if pattern != '':
        payload = {"routetext": pattern}
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()['data']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    else:
        routes = []
        characters = string.digits + string.ascii_lowercase
        for pattern in characters:
            time.sleep(0.1)
            routes += fetch_routes(pattern)
        return routes
```
:::


::: {#79af2bc7 .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
routes = fetch_routes()

# De-duplicate to get unique routes.
df_routes = pd.DataFrame(routes)
df_routes = df_routes.drop_duplicates(subset=["routeno"], keep="first")

df_routes.to_csv(data_directory / 'raw' / 'routes.csv', index=False)

print(df_routes.shape)
df_routes.head(3)
```
:::


::: {#0dcbb105 .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
df_routes = pd.read_csv(data_directory / 'raw' / 'routes.csv')

df_routes = df_routes \
    .rename(columns={'routeparentid': 'route_parent_id', 'routeno': 'route_number'})[['route_number', 'route_parent_id']] \
    .sort_values(by = 'route_number') \
    .reset_index(drop = True)

df_routes.to_csv(data_directory / 'cleaned' / 'routes.csv', index=False)

print(df_routes.shape)
df_routes.head(3)
```
:::




# Route Points

> Takes `route_id` as input and returns geo-locations of the route to be taken in response. There isn't an identifier for the bus stop in this dataset. Instead it'points are at regular distance along the route.

## Sample request

```bash
curl -X POST 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/RoutePoints' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  -d '{"routeid":3796}'
```

## Sample response

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

::: {#c901dccf .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def fetch_route_points(route_id: str):
    time.sleep(0.1)
    logging.info(f"Fetching route points for route ID = '{route_id}'")
    url = "https://bmtcmobileapi.karnataka.gov.in/WebAPI/RoutePoints"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "lan": "en"
    }

    payload = {"routeid": route_id}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
```
:::




# Vehicles

> Returns parent ID and registration number of vehicles which match the vehicle number passed in the argument. Ex: `0007` returns `KA53F0007` and `KA57F0007`.

## Sample request

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/ListVehicles' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"vehicleRegNo":"0007"}'

```

## Sample response

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

::: {#6058bda7 .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def fetch_vehicles(pattern: str = ""):
    time.sleep(0.1)
    logging.info(f"Fetching vehicles for pattern = '{pattern}'")
    url = "https://bmtcmobileapi.karnataka.gov.in/WebAPI/ListVehicles"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "lan": "en"
    }

    if pattern != '':
        payload = {"vehicleRegNo": pattern}
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()['data']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    else:
        vehicles = []
        characters = string.digits + string.ascii_lowercase
        for pattern in characters:
            time.sleep(0.1)
            vehicles += fetch_vehicles(pattern)
        return vehicles
```
:::


::: {#fbd52b0d .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
vehicles = fetch_vehicles()

# De-duplicate to get unique vehicles.
df_vehicles = pd.DataFrame(vehicles)
df_vehicles = df_vehicles.drop_duplicates(subset=["vehicleregno"], keep="first")

df_vehicles.to_csv(data_directory / 'raw' / 'vehicles.csv', index=False)
print(df_vehicles.shape)
df_vehicles.head(3)
```
:::


::: {#b9832c6b .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
df_vehicles = pd.read_csv(data_directory / 'raw/vehicles.csv')

df_vehicles = df_vehicles \
    .rename(columns={'vehicleid': 'vehicle_id', 'vehicleregno': 'registration_number'})[['vehicle_id', 'registration_number']] \
    .sort_values(by = 'vehicle_id') \
    .reset_index(drop = True)

df_vehicles.to_csv(data_directory / 'cleaned' / 'vehicles.csv', index=False)

print(df_vehicles.shape)
df_vehicles.head(3)
```
:::




# Trip details

> Takes a `vehicle_id` as input and returns route details of the current trip along with the live location of the vehicle.

## Sample request

```bash
curl 'https://bmtcmobileapi.karnataka.gov.in/WebAPI/VehicleTripDetails_v2' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  --data-raw '{"vehicleId":21670}'
```

## Sample response

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

::: {#77a99733 .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def fetch_trip_details(vehicle_id: int):
    time.sleep(0.1)
    logging.info(f"Fetching trip details for vehicle ID = '{vehicle_id}'")
    url = "https://bmtcmobileapi.karnataka.gov.in/WebAPI/VehicleTripDetails_v2"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    payload = json.dumps({"vehicleId": int(vehicle_id)})
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Response text:", getattr(e.response, "text", None))
        return None
```
:::


::: {#304d583e .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
directory = data_directory / 'raw' / 'trip_details' / str(int(datetime.datetime.now().timestamp()))
directory.mkdir(exist_ok=True, parents=True)

for index, row in df_vehicles.iterrows():
    trip_details = fetch_trip_details(vehicle_id = row['vehicle_id']) 
    with open(directory / f"{row['vehicle_id']}.json", "w") as f:
        json.dump(trip_details, f, indent = 4)
```
:::



## Issue 1. Vehicle is assigned to more than one route

Vehicles on some occassions are assigned to more than one route. Ex: Vehicle `KA57F5808` is assigned to two routes, `routeno = 210-NA` and `routeno = D33-PPLO`.

```json
"LiveLocation": [
    {
        "latitude": 12.909809,
        "longitude": 77.536422,
        "location": "Depot-33 Poornapragna layout (Towards Depot-33 (Poornapragna layout))",
        "lastrefreshon": "17-09-2025 23:19:34",
        "nextstop": null,
        "previousstop": "Arehalli (Towards Kengeri)",
        "vehicleid": 27211,
        "vehiclenumber": "KA57F5808",
        "routeno": "210-NA",
        "servicetypeid": 72,
        "servicetype": "Non AC/Ordinary",
        "heading": 210.18,
        "responsecode": 200,
        "trip_status": 1,
        "lastreceiveddatetimeflag": 1
    },
    {
        "latitude": 12.909809,
        "longitude": 77.536422,
        "location": "Depot-33 Poornapragna layout (Towards Depot-33 (Poornapragna layout))",
        "lastrefreshon": "17-09-2025 23:19:34",
        "nextstop": null,
        "previousstop": "Arehalli (Towards Kengeri)",
        "vehicleid": 27211,
        "vehiclenumber": "KA57F5808",
        "routeno": "D33-PPLO",
        "servicetypeid": 72,
        "servicetype": "Non AC/Ordinary",
        "heading": 210.18,
        "responsecode": 200,
        "trip_status": 1,
        "lastreceiveddatetimeflag": 1
    }
]
```

## Issue 2. Live location is missing

Live location was empty for about `2.5%` of vehicles (`185` out of `7,247` vehicles) when run on `2025-09-17`. Ex: Vehicle ID  `28622` with registration number `KA01AR4181`.

```json
{
    "RouteDetails": [],
    "LiveLocation": [],
    "Message": "No Records Found",
    "Issuccess": true,
    "exception": null,
    "RowCount": 0,
    "responsecode": 200
}
```

::: {#778c1884 .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def get_latest_directory(directory: Path):
    "Return the latest directory, sorting by name for a given directory."
    latest = (directory 
        .ls() 
        .filter(lambda f: not f.name.startswith('.')) 
        .sorted(key=lambda f: f.name)[-1]
    )
    return latest
```
:::


::: {#f5afdd68 .cell 0='e' 1='x' 2='p' 3='o' 4='r' 5='t'}
``` {.python .cell-code}
def extract_live_location(trip_detail):
    """Extract live location from trip detail."""
    locations = trip_detail['LiveLocation']

    # When there are more than one live locations, it's mostly because of the vehicle assigned to more than one route at a time.
    # We could use the route details and live location to determine which is the right route that the vehicle is running on.
    return locations
```
:::


::: {#7d0823c4 .cell}
``` {.python .cell-code}
# Pick the latest run of trip details.
def extract_live_locations(directory: Path):
    """Extract live location for all trip details in a directory."""
    live_locations = []
    for filepath in directory.ls():
        with open(filepath) as f:
            trip_detail = json.load(f)
            
            # Extract live locations.
            live_location = extract_live_location(trip_detail)
            live_locations += live_location
    live_locations = pd.DataFrame(live_locations)
    return live_locations
```
:::


::: {#01ba5c73 .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
directory = get_latest_directory(data_directory / 'raw' / 'trip_details')
df_live_locations = extract_live_locations(directory)

df_live_locations.to_csv(data_directory / 'cleaned' / 'live_locations.csv', index=False)
print(df_live_locations.shape)
df_live_locations.head(3)
```
:::


::: {#26fcaab2 .cell 0='h' 1='i' 2='d' 3='e' 4='
' 5='s' 6='k' 7='i' 8='p' 9='_' 10='e' 11='x' 12='e' 13='c'}
``` {.python .cell-code}
df_live_locations.groupby('location').size().sort_values(ascending=False).head(25)
```
:::



::: {#4517f397 .cell 0='h' 1='i' 2='d' 3='e'}
``` {.python .cell-code}
import nbdev; nbdev.nbdev_export()
```
:::



