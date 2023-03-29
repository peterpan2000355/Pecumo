'''(
    name='ip.py',
    version="1.0",
    description="Calculadora IP mediante el uso de la libreria ipaddress"
    author="Pedro C.",
    license="GPL"
)
'''

import ipaddress

Id=input("Entre la dirección de red IPv4 ó IPv6 con prefijo (ejemplo: 192.168.1.25/31):") 
ip=ipaddress.ip_network(Id.strip(), strict=False)  #Eliminamos espacios iniciales y finales, no funciona si metemos un espacio por error
print("Mascara de subred:",ip.netmask)
print("Wildcard es:",ip.hostmask)
print("Primera IP valida o usable es:", ip.network_address+1)
print("Última IP valida o usable es:",ip.broadcast_address-1)
print("Broadcast",ip.broadcast_address)
if (ip.num_addresses) == 2:                         # Necesario porque sino hay incoherencia con las IPv4 de mascara 31   
    print("Total de direcciones IP validas:", ip.num_addresses)
else:
    print("Total de direcciones IP validas:", ip.num_addresses-2)
print("Total de direcciones IP:", ip.num_addresses)
print("Es una dirección privada?:",ip.is_private)
print("Es una dirección reservada?:",ip.is_reserved)
print("Es una dirección global?:",ip.is_global)
