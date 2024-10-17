import PySimpleGUI as anjay
anjay.theme("DarkGreen4")
anjay.theme_text_color("#FFFF00")
window = anjay.Window(title="Contoh Button",
                      layout=[[anjay.Text("Contoh Button")],
                              [anjay.Button("Button Simpan")],
                              [anjay.Button("Button keluar")]],
                      size=(400,200),
                      font=("Times",18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()