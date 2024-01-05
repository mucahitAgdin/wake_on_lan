import socket
import binascii
import tkinter as tk

def wake_on_lan(mac_address, ip_address, port=7):
    # MAC adresini hexadecimal formata dönüştürme
    mac_hex = binascii.unhexlify(mac_address.replace(':', ''))

    # Magic paketi oluşturma
    magic_packet = b'\xff' * 6 + mac_hex * 16

    # Soket oluşturma ve WOL paketini gönderme
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(magic_packet, (ip_address, port))
    sock.close()

def send_wol():
    mac_address = entry_mac.get()
    ip_address = entry_ip.get()
    wake_on_lan(mac_address, ip_address)
    status_label.config(text="WOL Paketi Gönderildi!")

# GUI oluşturma
app = tk.Tk()
app.title("Wake On LAN Uygulaması")

# MAC Adresi Giriş Kutusu
label_mac = tk.Label(app, text="MAC Adresi:")
label_mac.pack()
entry_mac = tk.Entry(app)
entry_mac.pack()

# IP Adresi Giriş Kutusu
label_ip = tk.Label(app, text="IP Adresi:")
label_ip.pack()
entry_ip = tk.Entry(app)
entry_ip.pack()

# Gönder Butonu
send_button = tk.Button(app, text="WOL Paketi Gönder", command=send_wol)
send_button.pack()

# Durum Etiketi
status_label = tk.Label(app, text="")
status_label.pack()

# Uygulamayı başlat
app.mainloop()
