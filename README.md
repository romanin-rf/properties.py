# properties.py
## Description
Module for reading/writing properties-files.

## Installation
```shell
pip install -U properties.py
```

## Usage
#### Code
```python
import properties

user = {"name": "NoName", "age": -1, "sex": "M", "data": {"region": 39, "keywords": ["man", "human", 14.88]}}

with open("test.properties", "w", encoding="utf-8", errors="ignore") as file:
    properties.dump(user, file)

with open("test.properties", "r", encoding="utf-8", errors="ignore") as file:
    data = properties.load(file)

print(data)
```
#### Output
```python
{'name': 'NoName', 'age': -1, 'sex': 'M', 'data': {'region': 39, 'keywords': ['man', 'human', 14.88]}}
```