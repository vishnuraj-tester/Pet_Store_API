import requests
import logging
from config.config import BASE_URL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })

    def send_request(self, method, endpoint, payload=None):
        url = f"{BASE_URL}{endpoint}"
        logging.info(f"Request: {method} {url}")
        if payload:
            logging.info(f"Payload: {payload}")

        response = self.session.request(method, url, json=payload)
        logging.info(f"Response Status: {response.status_code}")
        logging.info(f"Response Body: {response.text}")
        return response

