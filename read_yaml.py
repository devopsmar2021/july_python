import yaml

with open(r'abc.yaml') as file:
    r_data = yaml.load(file, Loader=yaml.FullLoader)
    print(r_data)