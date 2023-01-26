import nmap3
import PySimpleGUI as sg
from pprint import pformat 

nmap_basics = nmap3.Nmap()
nmap_scatec = nmap3.NmapScanTechniques()
nmap_basics_submits = [ 
    sg.Submit("Scanning Port",key="scan_top_ports"),
]
sg.theme("DarkBlack1")
layout = [
            [sg.Text("Alamat IP(IPv4): "),sg.InputText("127.0.0.1",key="ipv4_dst")],
            nmap_basics_submits,
            [sg.Text('Pernyataan'),sg.Output(key='statement',size=(50,1)),sg.Cancel("Kembali",key="cancel")],
            [sg.Text('Hasil'),sg.Output(key='hasil',size=(80,30))],
        ]
window = sg.Window(title='Simple Port Scan NMAP', layout=layout)
def scan_top_ports(dst):
    window['statement'].update("Ready!")
    results = nmap_basics.scan_top_ports(dst)
    results = pformat(results,compact=True)
    window['statement'].update("Hasil Scanning Port(SA: open,RA: filtered)")
    window['hasil'].update(results)

while True:
    event, values = window.read()
    dst = values["ipv4_dst"]
    if event == sg.WIN_CLOSED:
        break
    if event == "cancel":
        continue
    if event == "scan_top_ports":
        scan_top_ports(dst)
window.close()