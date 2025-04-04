import json

db = "user_data.json"
sample = {"1": {"status": True, "attempts": 5, "r_value": 10, "count": 1}}


def read(id=0):
    try:
        with open(db) as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(db, "w") as f:
            json.dump(sample, f)
            data = json.load(f)
    else:
        if id == 0:
            return data
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


def user_in_db(id):
    data = read()
    if id in data:
        return True
    else:
        return False
