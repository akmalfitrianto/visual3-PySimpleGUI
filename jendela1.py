import PySimpleGUI as sg
sg.theme("BlueMono")
sg.theme_text_color("#FF0000")
window = sg.Window(title="Latihan Pertama",layout=[[sg.Text("NPM     : 2210010546")],
                                                    [sg.Text("Nama    : Muhammad Akmal Fitrianto")],
                                                    [sg.Text("Kelas    : 5E Reguler Banjarmasin")],
                                                    [sg.Text("Matkul   : Pemrograman Visual 3")]],
                                                    size=(500,200),
                                                    font=("Times",18))
window()
window.close()