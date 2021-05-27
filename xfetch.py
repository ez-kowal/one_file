#!/usr/bin/env python

import platform, cpuinfo, psutil, getpass, ctypes
from colorama import Fore,  init
init(convert=True,autoreset=True)

lib = ctypes.windll.kernel32 
t = lib.GetTickCount64() 
t = int(str(t)[:-3]) 
mins, sec = divmod(t, 60) 
hour, mins = divmod(mins, 60) 
  

ram_max = str(round(float(format(round(float((psutil.virtual_memory().total) / 1073741824),2)))))


cpu = cpuinfo.get_cpu_info()['brand_raw']

uname = platform.uname()

sep = "●" #some ideas: ■ ● ~ # - 
print("")
print(Fore.LIGHTGREEN_EX+"     OS  "+sep+"  "+Fore.RESET+f"{uname.system} {uname.release}")
print(Fore.LIGHTGREEN_EX+" Uptime  "+sep+"  "+Fore.RESET+f"{hour:02}:{mins:02}:{sec:02}")
print(Fore.LIGHTGREEN_EX+"    Cpu  "+sep+"  "+Fore.RESET+f"{cpu}")
print(Fore.LIGHTGREEN_EX+"    Ram  "+sep+"  "+Fore.RESET+f"{ram_max} GB")
print("")
print(" welcome to "+Fore.LIGHTGREEN_EX+f"{uname.node}"+Fore.RESET+","+Fore.LIGHTGREEN_EX+f" {getpass.getuser()}")