import datetime
import json
from pathlib import Path
import fire
from traffic_data_bengaluru.bmtc import fetch_routes, process_routes

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

if __name__ == "__main__":
    fire.Fire({"bmtc_fetch_routes": bmtc_fetch_routes})
