import json

my_data= {
    "Numbers": [12, 234, 65, 99, 77, 12],
    "Names": ['Bob', 'Billy', 'Betty', 'Jeannie'],
    "PhoneNumbers": [123456789, 4351239876, 8013459876, 2088675309]
}

def write_data_to_json_file(filename, data):
    with open(filename, 'wt') as filehandle:
        json_data = json.dumps(data)
        filehandle.write(json_data)

def read_data_from_json_file(filename):
    with open(filename, 'rt') as filehandle:
        data = filehandle.read()
        dictionary_data = json.loads(data)
        return dictionary_data

def main():
    print(my_data['Numbers'])
    print(my_data)

    filename = 'jsonexample5.json'
    write_data_to_json_file(filename, my_data)

    new_data = read_data_from_json_file(filename)
    print(new_data['Numbers'])

main()