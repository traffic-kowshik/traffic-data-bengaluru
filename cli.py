import datetime
import geojson
import json
from fastcore.all import Path
import fire
from tqdm import tqdm
from traffic_data_bengaluru.utils import read_file
from traffic_data_bengaluru.bmtc import fetch_routes, process_routes, fetch_vehicles, process_vehicles, fetch_route_points, get_routes, get_route_id, convert_route_to_geojson

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# BMTC
def bmtc_fetch_routes():
    data_directory = Path('data/bmtc/')
    filename = f'{str(int(datetime.datetime.now().timestamp()))}'

    logger.info("Fetching routes ...")
    routes = fetch_routes()

    filepath = data_directory / 'raw' / 'routes' / f'{filename}.json'
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(routes, f, indent=2)
    logger.info(f"Raw routes saved successfully to {filepath}")

    logger.info("Processing routes ...")
    df_routes = process_routes(routes)

    filepath = data_directory / 'cleaned' / 'routes' / f'{filename}.csv'
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df_routes.to_csv(filepath, index=False)
    logger.info(f"Processed routes saved successfully to {filepath}")


def bmtc_fetch_vehicles():
    data_directory = Path('data/bmtc/')
    filename = f'{str(int(datetime.datetime.now().timestamp()))}'

    logger.info("Fetching vehicles ...")
    vehicles = fetch_vehicles()

    filepath = data_directory / 'raw' / 'vehicles' / f'{filename}.json'
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(vehicles, f, indent=2)
    logger.info(f"Raw vehicles saved successfully to {filepath}")

    logger.info("Processing vehicles ...")
    df_vehicles = process_vehicles(vehicles)

    filepath = data_directory / 'cleaned' / 'vehicles' / f'{filename}.csv'
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df_vehicles.to_csv(filepath, index=False)
    logger.info(f"Processed vehicles saved successfully to {filepath}")

def bmtc_fetch_route_points():
    data_directory = Path('data/bmtc/')
    df_routes = get_routes(data_directory)

    now = str(int(datetime.datetime.now().timestamp()))
    logger.info("Fetching route points ...")
    raw_directory = data_directory / 'raw' / 'route_points' / now
    raw_directory.mkdir(exist_ok=True, parents=True)
    for index, row in tqdm(df_routes.iterrows(), total = df_routes.shape[0], desc = 'Fetching route points'):
        trip_details = fetch_route_points(route_id = row['route_id']) 
        with open(raw_directory / f"{row['route_id']}.json", "w") as f:
            json.dump(trip_details, f, indent = 4)


    logger.info("Processing route points ...")
    cleaned_directory = data_directory / 'cleaned' / 'route_points' / now
    cleaned_directory.mkdir(exist_ok=True, parents=True)

    features = []
    for filepath in tqdm(raw_directory.ls(), total = raw_directory.ls().__len__(), desc = 'Converting route points to geojson'):
        route = read_file(filepath)
        if route is None:
            continue
        route_id = get_route_id(filepath)
        properties = {'route_id': route_id}
        feature = convert_route_to_geojson(route, properties)

        with open(cleaned_directory / f"{route_id}.json", "w") as f:
            json.dump(feature, f, indent = 4)

        features.append(feature)

    # Write to a file as a geojson FeatureCollection.
    fc = geojson.FeatureCollection(features = features)
    with open(data_directory / 'cleaned' / 'route_points' / f'{now}.geojson', 'w') as f:
        json.dump(fc, f)


if __name__ == "__main__":
    fire.Fire({
        "bmtc_fetch_routes": bmtc_fetch_routes,
        "bmtc_fetch_vehicles": bmtc_fetch_vehicles,
        "bmtc_fetch_route_points": bmtc_fetch_route_points,
    })
