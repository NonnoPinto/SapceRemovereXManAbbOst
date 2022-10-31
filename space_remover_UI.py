""" Python GUI to remove space from ANY string
    And copying outuput to clipboard """

import space_remover
import PySimpleGUI as sg
import pyperclip as py

window = sg.Window(title="IBAN space remover X Manifesti Abbastanza Ostili", layout=[
    [sg.Text('Metti qui l\'IBAN con gli spazi'), sg.InputText()],
    ##[sg.Text(), sg.InputText()],
    [sg.Button('Togli spazi'), sg.Button('Exit')]])

while 1:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Togli spazi': ##or ky.read_key() == 'enter':
        ##values[1] = space_remover.spaceRemover(values[0])
        ##window.Refresh()
        py.copy(space_remover.spaceRemover(values[0]))
        sg.popup_notify('L\'IBAN senza spazi è stato copiato negli appunti (basta che fai \'Incolla\'')
        ##sg.Print(space_remover.spaceRemover(values[0]))

window.close()