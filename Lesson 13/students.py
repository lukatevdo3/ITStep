import json, os, sys

def create_json_file(path, file):
    file_path = None

    if len(path.split('/')) == 2:
        file_path = f"{path}/{file}.json"
    
    os.makedirs(path, exist_ok=True)

    try:
        with open(file_path, mode = "x", encoding = "utf-8") as f:
            ...
    except FileExistsError:
        print(f"File '{file_path}' Already Exists...")
        print("Keep Working...\n")
    except TypeError:
        print(f"The path must be two-level... for example: 'files/json")
        print("Exiting")
        sys.exit()
    
    return file_path


def write_json_file(path, json_data):
    with open(path, mode = "w", encoding = "utf-8") as f:
        f.write(json.dumps(json_data, indent = 2))


def read_json_file(path):
    with open(path, mode = 'r', encoding = 'utf-8') as f:
        return json.loads(f.read())
    

def update_json_file(path, json_data):
    data = read_json_file(path)

    for st in data:
        if st['id'] == json_data['id']:
            print(f"Student with ID {json_data['id']} Already Exists... ")
            break
    else:
        data.append(json_data)
        data.sort(key=lambda x: x['id'])
        
        write_json_file(path, data)
    
    return data