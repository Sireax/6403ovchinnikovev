import yaml

def read_config(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)