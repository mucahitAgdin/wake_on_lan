import socket
import binascii

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

# Bilgisayarın MAC adresi ve IP adresini burada değiştirebilirsiniz

mac_address = '74:56:3C:73:4C:F6'
ip_address = '192.168.1.144'

wake_on_lan(mac_address, ip_address)

