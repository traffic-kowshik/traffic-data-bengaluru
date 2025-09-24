import datetime
import json
from fastcore.all import Path
import fire
from tqdm import tqdm
from nbdev.config import get_config

from traffic_data_bengaluru.bmtc.apis.routes import task_fetch_routes
from traffic_data_bengaluru.bmtc.apis.vehicles import task_fetch_vehicles
from traffic_data_bengaluru.bmtc.apis.route_points import task_fetch_route_points
from traffic_data_bengaluru.bmtc.apis.vehicle_trip_details import task_fetch_vehicle_trip_details

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

repo_directory = Path(get_config().nbs_path).parent
data_directory = repo_directory / "data" / "bmtc"
data_directory.mkdir(exist_ok=True, parents=True)

def bmtc_fetch_routes():
    task_fetch_routes(data_directory=data_directory)

def bmtc_fetch_vehicles():
    task_fetch_vehicles(data_directory=data_directory)

def bmtc_fetch_route_points():
    task_fetch_route_points(data_directory=data_directory)

def bmtc_fetch_vehicle_trip_details():
    task_fetch_vehicle_trip_details(data_directory=data_directory)


if __name__ == "__main__":
    fire.Fire({
        "bmtc_fetch_routes": bmtc_fetch_routes,
        "bmtc_fetch_vehicles": bmtc_fetch_vehicles,
        "bmtc_fetch_route_points": bmtc_fetch_route_points,
        "bmtc_fetch_vehicle_trip_details": bmtc_fetch_vehicle_trip_details
    })
