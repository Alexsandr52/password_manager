import dearpygui.dearpygui as dpg
import sattings as sattings
import json
import functions

with open(sattings.path) as json_file:
        default_variabls = json.load(json_file)



varibals = {
    25: default_variabls['default_len'],
    26: False,
    27: False,
    28: False,
}

def get_value(key, data):
    varibals[key] = data



def show_passwd():
    total = ''.join([default_variabls['default_symbols'][i] for i, var in enumerate([26, 27, 28]) if varibals[var]])
    if total == '': print('no values'); return False
    try:
        password = functions.gen_pass(varibals[25], total)
        print(password)
    except:
        return False


dpg.create_context()
with dpg.window(tag="Primary Window"):
    dpg.add_text('password manager', )
    dpg.add_button(label='generate password', callback=show_passwd)
    #add default_value == pass

    dpg.add_input_text(label='string', default_value='Quick brown fox')
    dpg.add_slider_int(label='password lenth', min_value=6, default_value=16, max_value=30, callback=get_value)
    dpg.add_checkbox(label='ascii_letters', callback=get_value)
    dpg.add_checkbox(label='digits', callback=get_value)
    dpg.add_checkbox(label='punctuation', callback=get_value)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(tag="Primary Window"):
#     dpg.add_text("Hello, world")

# dpg.create_viewport(title='Custom Title', width=600, height=200)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.set_primary_window("Primary Window", True)
# dpg.start_dearpygui()
# dpg.destroy_context()