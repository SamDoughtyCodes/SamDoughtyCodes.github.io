import constants
import requests

URL = "https://api.coasterpedia.net/v1/attractions"

url_suffix = "?q=Voltron&limit=5"
data = requests.get(URL+url_suffix, headers={
    "Authorization": f"Bearer {constants.API_KEY}",
    "User-Agent": "CredCounterProto/1.0 (samdoughtycodes.github.io; sam@moocows.com)"
    })

for record in data.json()["data"]:
    print(record["name"])