from datetime import datetime, timedelta
import json


with open("something.json") as f:
    data = json.load(f)

for set in data["access"]:
    cur_time = datetime.strptime(set["expiration"], "%Y-%m-%dT%H:%M:%S.%f")
    ff_time = cur_time - timedelta(hours=3, minutes=0)
    set["expiration"] = ff_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

with open("something.json", "w") as f:
    json.dump(data, f)
