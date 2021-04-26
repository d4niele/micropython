import usocket
def wake(macaddress,ip_broadcast="255.255.255.255"):
    s = usocket.socket(usocket.AF_INET,usocket.SOCK_DGRAM)
    mac_int = [int(x,16) for x in macaddress.split(":")]
    message = bytearray(b'\xff'*6) + bytearray(mac_int*16)
    s.sendto(message,(ip_broadcast,9))
    s.close()