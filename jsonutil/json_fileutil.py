import json

def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(filename, json_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(json_object, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    filename = 'emp_data.txt'
    js_obj = {"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}
    write_json_file(filename, js_obj)
    print(read_json_file(filename))
