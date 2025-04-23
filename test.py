import requests

BASE_URL = "http://localhost:8000/api"  # yoki sening server manziling

# 1. Login
token = '41388d3256b4dc4cf2dfd497ead17917bc707270'
headers = {"Authorization": f"Token {token}"}
response = requests.get(f"{BASE_URL}/admin/places/")
print("Joylar ro‘yxati:", response.json())

# Taomlar
response = requests.get(f"{BASE_URL}/admin/dishes/")
print("Taomlar ro‘yxati:", response.json())

