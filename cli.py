from traffic_data_bengaluru.bmtc import fetch_routes
import fire

def fetch_routes_task(pattern: str):
    routes = fetch_routes(pattern=str(pattern))
    print(routes)

if __name__ == "__main__":
    fire.Fire({"fetch_routes": fetch_routes_task})
