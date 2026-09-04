from time import time
import psutil 
import os
import platform
import socket

           #PC SYSTEM MONITORING#

cpu_pc = psutil.cpu_percent(interval=0.5)
ram = psutil.virtual_memory().percent
sistema = platform.system()
disco = psutil.disk_usage("C:\\")
user_name = psutil.Process().username()
uptime = time() - psutil.boot_time()
process = len(psutil.pids())
interfaces = psutil.net_if_addrs()

for nome in interfaces:
    print(nome)
           #Operating System Monitoring#
    #Uptime Calculation#
horas = uptime // 3600
minutos = uptime % 3600 // 60
            #PRINTS OF SYSTEM MONITORING#
print("=====================SYSTEM MONITORING=====================\n")

print(f"CPU Usage: {cpu_pc}%")
print(f"RAM Usage: {ram}%")
print(f"Disk Usage: {disco.percent}%")
print(f"Platform: {platform.system()}")
print(f"Uptime: {int(horas)}h:{int(minutos)}min")
print(f"Process: {process}")

print("=====================NETWORK INTERFACES=====================\n")
for nome, enderecos in interfaces.items():
    print(f"-----{nome}-----")

    for endereco in enderecos:                              
        if endereco.family == socket.AF_INET:
            print(f"IPv4: {endereco.address}")
