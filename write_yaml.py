
import yaml

abc = {'a':1, 'b':2, 'c':[1,2,3], 'd': {'x':'s'}}

with open(r'output.yaml', 'w') as file:
    documents = yaml.dump(abc, file)
