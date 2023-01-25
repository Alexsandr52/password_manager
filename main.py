# Password manager 
import password_manager.user_interface as user_interface

cmd_commands = user_interface.cmd_commands
print('Password manager')
cmd_commands.cmd_help()

while True: 
    cmd = input(':') 
 
    if cmd == '0': 
        break 

    elif cmd == '':
        continue
    
    elif cmd.isdigit() and int(cmd) > 0 and int(cmd) < 6: 
        user_interface.commands[int(cmd)-1]()  

    else: 
        print('cmd error')
