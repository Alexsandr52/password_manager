import json
import password_manager.functions as functions
import password_manager.sattings as sattings
from os.path import exists
 
with open(sattings.path) as json_file:
        default_variabls = json.load(json_file)

# User interface commands
class cmd_commands:
  
    default_len = default_variabls['default_len']
    default_symbols = default_variabls['default_symbols']
    path = default_variabls['default_path']

    def cmd_help() -> None:
        print('''
            Password manager
            commands:
                [1]: generate new password
                [2]: to save password
                [3]: to watch all passwords
                [4]: to remove password
                [5]: help information
                [0]: to exit
        ''')

    @classmethod
    def cmd_gen_pass(cls) -> None:
        params = input('Change length or symbols array? y/n: ') 
        new_len = int(input('Enter new length: ')) if params == 'y' else cls.default_len 
        symbols = ''.join([input(f'Use {i}? y/n: ') for i in ['ascii_letters', 'digits','punctuation']]) if params == 'y' else 'yyy'
        symbols = ''.join([cls.default_symbols[i] for i, value in enumerate(symbols) if value in ['y','']]) 
        if len(symbols) < new_len: 
            raise f'Password length {new_len} must be less or equal to symbols lenth {len(symbols)}'

        password = functions.gen_pass(length=new_len, total=symbols)
        print(password) 
        
        if input('Do you want to save password? y/n: ') == 'y':
            cls.cmd_save_pass(password=password)
    
    @classmethod
    def cmd_save_pass(cls, password=None) -> None:
        if password == None:
            password = input('Input password or Enter to generate new: ')
            if password == '': return cls.cmd_gen_pass()

        title = input('Input title: ')
        path = cls.path
        functions.save_pass(path=path, password=password, title=title)
    
    @classmethod
    def cmd_remove_pass(cls):
        title = input('Enter title: ')
        if cls.cmd_show_pass(title):
            functions.save_pass(path=cls.path, password='', title=title)
        else:
            print(f'Title {title} not find')

    @staticmethod
    def cmd_change_settings():
        default_variabls = sattings.default_variabls
        print(default_variabls.keys(), sep='\n')
        print('stop to exit')
        while True:
            key = input('Input key: ')
            value = input(f'Input value for {key}: ')
            if 'stop' in [key, value]: break
            default_variabls[key] = value

        sattings.chenge_settings(default_variabls)
            
    @classmethod
    def cmd_show_pass(cls, title=None) -> None:
        if not exists(cls.path): raise 'file doesn\'t exist'
        if title != None: 
            if functions.show_pass(cls.path, title): return True 
        else: 
            title = input('Input title or Enter to skip: ')
            if title != '': 
                functions.show_pass(cls.path, title) 
                return False

            functions.show_pass(cls.path)
        return False

commands = [cmd_commands.cmd_gen_pass, 
            cmd_commands.cmd_save_pass, 
            cmd_commands.cmd_show_pass, 
            cmd_commands.cmd_remove_pass, 
            cmd_commands.cmd_help]    
