import time
import requests
import json
from .utils import load_known_whales, is_anomalous_activity

ETHERSCAN_API = "https://api.etherscan.io/api"
API_KEY = "YourApiKeyToken"

def fetch_transactions(address):
    """Fetch recent transactions for a whale address."""
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": API_KEY
    }
    response = requests.get(ETHERSCAN_API, params=params)
    data = response.json()
    return data.get("result", [])

def monitor_whales():
    whales = load_known_whales()
    for whale in whales:
        txs = fetch_transactions(whale["address"])
        if txs:
            recent = txs[:5]  # check last 5 txs
            if is_anomalous_activity(recent, whale):
                print(f"[ALERT] Suspicious activity detected for whale {whale['name']} ({whale['address']})")
