# csvutil

csvutil simplifies the code to read and write csv files without using external modules.

## Installation

Download the csutilpy file in the root of source code directory.

## Usage
employees.csv
```csv
Name,Department,Location
John,Science,Texas
Scott,Biology,London
```

```python
from csvutil import read_csv, write_csv

get_rows = read_csv('employees.csv')
print(get_rows)
# output - [{'Name': 'John', 'Department': 'Science', 'Location': 'Texas'}, {'Name': 'Scott', 'Department': 'Biology', 'Location': 'London'}]

data = [{'firstname': 'John', 'lastname':'Walker'},
		{'firstname': 'Clark', 'lastname':'Alex'},
		{'firstname': 'Scott', 'lastname':'Ben'}]
columns=['firstname', 'lastname']
createcsv = write_csv('names.csv', data=data, columns=columns)

get_rows = read_csv('names.csv')
print(get_rows)
#output - [{'firstname': 'John', 'lastname': 'Walker'}, {'firstname': 'Clark', 'lastname': 'Alex'}, {'firstname': 'Scott', 'lastname': 'Ben'}]
```
