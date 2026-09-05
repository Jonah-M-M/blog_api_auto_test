import os.path
import yaml

def read_yaml(filename):
    path = os.path.join("./data", filename)
    with open(path,"r",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

