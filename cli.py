from fastcore.all import Path
import fire
from nbdev.config import get_config

from traffic_data_bengaluru.bmtc.routes import task_fetch_routes
from traffic_data_bengaluru.bmtc.vehicles import task_fetch_vehicles
from traffic_data_bengaluru.bmtc.route_points import task_fetch_route_points
from traffic_data_bengaluru.bmtc.trip_details import task_fetch_trip_details
from traffic_data_bengaluru.bmtc.route_details import task_fetch_route_details, task_fetch_route_details_v2

from traffic_data_bengaluru.namma_metro.ridership import task_fetch_ridership


import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

repo_directory = Path(get_config().nbs_path).parent

def bmtc_fetch_routes():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_routes(data_directory=data_directory)

def bmtc_fetch_vehicles():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_vehicles(data_directory=data_directory)

def bmtc_fetch_route_points():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_route_points(data_directory=data_directory)

def bmtc_fetch_trip_details():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_trip_details(data_directory=data_directory)

def bmtc_fetch_route_details():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_route_details(data_directory=data_directory)

def bmtc_fetch_route_details_v2():
    data_directory = repo_directory / "data" / "bmtc"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_route_details_v2(data_directory=data_directory)

def namma_metro_fetch_ridership():
    data_directory = repo_directory / "data" / "namma_metro"
    data_directory.mkdir(exist_ok=True, parents=True)
    task_fetch_ridership(data_directory=data_directory)

if __name__ == "__main__":
    fire.Fire({
        "bmtc_fetch_routes": bmtc_fetch_routes,
        "bmtc_fetch_vehicles": bmtc_fetch_vehicles,
        "bmtc_fetch_route_points": bmtc_fetch_route_points,
        "bmtc_fetch_trip_details": bmtc_fetch_trip_details,
        "bmtc_fetch_route_details": bmtc_fetch_route_details,
        "bmtc_fetch_route_details_v2": bmtc_fetch_route_details_v2,
        "namma_metro_fetch_ridership": namma_metro_fetch_ridership
    })
