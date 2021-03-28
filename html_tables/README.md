# htmltable

htmltable module converts csv data to HTML Tables.

## Installation

Download the htmltable file in the root of source code directory.

## Usage
employees.csv
```csv
Name,Department,Location
John,Science,Texas
Scott,Biology,London
```

```python
from htmltable import to_htmltable
from csvutil import read_csv, write_csv

csvdata = read_csv('employees.csv')
print(csvdata)
# output - [{'Name': 'John', 'Department': 'Science', 'Location': 'Texas'}, {'Name': 'Scott', 'Department': 'Biology', 'Location': 'London'}]

print(to_htmltable(csvdata))
# output - creates index.html file and return below output as string
#<div><table class='tablecss' style='border:1'><caption></caption><tr><th>Name</th><th>Department</th><th>Location</th></tr><tr><td>Scott</td><td>Biology</td><td>London</td></tr></tr></div>

#data with list of dictionaries can also be passed to htmltable to convert its data to html table
data = [{'firstname': 'John', 'lastname':'Walker'},
		{'firstname': 'Clark', 'lastname':'Alex'},
		{'firstname': 'Scott', 'lastname':'Ben'}]

print(to_htmltable(data))
#output - <div><table class='tablecss' style='border:1'><caption></caption><tr><th>firstname</th><th>lastname</th></tr><tr><td>Clark</td><td>Alex</td></tr><tr><td>Scott</td><td>Ben</td></tr><tr><td>Goldman</td><td>Sean</td></tr></tr></div>
```
