import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Helvetica 20", button_element_size=(6,3))
    button_size = (6,3)
    sg.theme_background_color('blue')
    button_color = ("green")

#hitta koden för att lägga in bild inom en button här: https://stackoverflow.com/questions/70416061/create-custom-buttons-in-pysimplegui
    layout = [
        [sg.Text("Yessir",font = "Helvetica 26", justification="right", expand_x= True,  pad = (10,20), right_click_menu= theme_menu, key = "-Text-")],
        [sg.Button("Clear",image_filename='button.png', border_width=0,expand_x = True), sg.Button("Enter",image_filename='button.png',expand_x = True),sg.Button("Check",image_filename='button.png' ,expand_x = True)],
        [sg.Button(7, button_color=button_color,border_width=0, size = button_size), sg.Button(8,button_color=button_color, size = button_size), sg.Button(9,button_color=button_color, size = button_size), sg.Button("*", image_filename='button.png',size = button_size)],
        [sg.Button(4, button_color=button_color,size = button_size), sg.Button(5,button_color=button_color, size = button_size), sg.Button(6,button_color=button_color, size = button_size), sg.Button("/",image_filename='button.png', size = button_size)],
        [sg.Button(1,button_color=button_color, size = button_size), sg.Button(2,button_color=button_color, size = button_size), sg.Button(3,button_color=button_color, size = button_size), sg.Button("-",image_filename='button.png', size = button_size)],
        [sg.Button(0,button_color=button_color,expand_x = True), sg.Button(".",image_filename='button.png',size = button_size), sg.Button("+",image_filename='button.png',size = button_size)],
    ]

    return sg.Window("Calculator", layout)

theme_menu = ["menu",["LightGrey1", "Dark","DarkGray8", "random"]]
window = create_window("dark")

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["0","1","2","3","4","5","6","7","8","9", ",","."]:
        current_num.append(event)
        num_string = "".join(current_num)
        window["-Text-"].update(num_string)

    if event in ["+", "-", "/","*"]:
        full_operation.append("".join(current_num))
        current_num = []
        full_operation.append(event)
        print(full_operation)
        window["-Text-"].update("")

    if event == "Enter":
        full_operation.append("".join(current_num))
        result = (eval("".join(full_operation)))
        window["-Text-"].update(result)
        full_operation = []

    if event == "Clear":
        current_num = []
        full_operation = []
        window["-Text-"].update("")


   #hitta hur man kan göra pop up windows https://www.tutorialspoint.com/pysimplegui/pysimplegui_popup_windows.htm
    if event == "Check":
        ekvation = "".join(full_operation) + "".join(current_num)
        sg.popup(f"Din ekvation är: {ekvation}")




window.close()