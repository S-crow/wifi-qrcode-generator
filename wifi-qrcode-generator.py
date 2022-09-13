import pyqrcode

ssid = "NOMDETONWIFI"
security = "WPA"
password = "MDPDETONWIFI"

qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
qr.png('wificode.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])