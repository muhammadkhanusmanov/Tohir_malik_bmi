import requests

BASE_URL = "http://localhost:8000/api"  # yoki sening server manziling

# 1. Login
token = '41388d3256b4dc4cf2dfd497ead17917bc707270'
headers = {"Authorization": f"Token {token}"}
reservation_data = {
    "place": 1,
    "full_name": "Ali Valiyev",
    "phone_number": "+998901234567",
    "date": "2025-04-26",
    "start_time": "18:00",
    "end_time": "20:00",
    "order_items": [
        {"dish": 1, "quantity": 2},
        {"dish": 2, "quantity": 1}
    ]
}

response = requests.post(f"{BASE_URL}/reserve/", json=reservation_data)
print(response.status_code)
print(response.json())