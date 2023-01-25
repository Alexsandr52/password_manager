import random
import json

def gen_pass(length: int, total: str) -> str: 
    password = ''.join(random.sample(total, length)) 
    return password 

def save_pass(path: str, password: str, title: str) -> None:
    try:
        with open(path) as json_file:
            data = json.load(json_file)
        data[title] = password
    except:
        data = {title: password}

    with open(path, 'w') as json_file:
        json.dump(data, json_file)

def show_pass(path: str, title=None) -> None:
    with open(path, 'r', encoding='UTF-8')as json_file:
        data = json.load(json_file)
        
        if title != None:
            try:
                print(f'{title}: {data[title]}')
                return True
            except: 
                print(f'{title} not find')
                return False

        for k, v in data.items():
            print(f'{k}: {v}', end='\n')

        return False

