import PySimpleGUI as sg
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define the layout of the PySimpleGUI window
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Input(key='-TEXT-'),sg.Button('Speak')],
    [sg.Radio('Male', 'voice', key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-', default=True)],
]

# Create the PySimpleGUI window
window = sg.Window('Text-to-Speech App', layout)

# Event loop to process "Speak" button and "Exit" button clicks
while True:
    event, values = window.read()
    if event ==sg.WINDOW_CLOSED:  # If user closes window or clicks "Exit" button
        break
    voice=engine.getProperty('voices')
    if event == 'Speak':
        text = values['-TEXT-']
        if text.strip() != '':
            engine.setProperty('voice', voice[0].id if values['-MALE-'] else voice[1].id)
            engine.say(text)
            engine.runAndWait()

# Close the PySimpleGUI window
window.close()