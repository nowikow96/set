import json

db = "user_data.json"
sample = {"1": {"status": True, "attempts": 5, "r_value": 10, "count": 1}}


def read(id):
    try:
        with open(db) as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(db, "w") as f:
            json.dump(sample, f)
            data = json.load(f)
    else:
        return data[id]


def write(id, **args):
    try:
        with open(db) as f:
            data = json.load(f)
            data[id] = args
    except FileNotFoundError:
        data = {}
        data[id] = args
        with open(db, "w") as f:
            json.dump(data, f)
    else:
        with open(db, "w") as f:
            json.dump(data, f)
