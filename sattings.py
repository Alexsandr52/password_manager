import json
import string

path = 'data_json/json_default_variabls.json'
default_variabls = {
    'default_len': 16, 
    'default_symbols': [string.ascii_letters, string.digits, string.punctuation],
    'default_path': 'data_json/passwords.json', 
    'config_path': path
}

if __name__ == '__main__':
    with open(path, 'w') as json_file:
        json.dump(default_variabls, json_file)
        