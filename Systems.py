import platform
import psutil
import wmi

# Installed software list
print("List of installed software:")
for software in psutil.process_iter(['name']):
    print(f"- {software.info['name']}")

# Internet speed
print(f"\nInternet speed: {psutil.net_if_stats()['Ethernet'][2] / 1000000} Mbps")

# Screen resolution
print(f"\nScreen resolution: {str(wmi.WMI().Win32_VideoController()[0].CurrentHorizontalResolution)}x{str(wmi.WMI().Win32_VideoController()[0].CurrentVerticalResolution)}")

# CPU model
print(f"\nCPU model: {platform.processor()}")

# No of core and threads of CPU
print(f"\nNo of cores: {psutil.cpu_count(logical=False)}")
print(f"No of threads: {psutil.cpu_count(logical=True)}")

# GPU model ( If exist )
try:
    print(f"\nGPU model: {wmi.WMI().Win32_VideoController()[0].Name}")
except:
    print("\nGPU model: Not found")

# RAM Size ( In GB )
print(f"\nRAM size: {round(psutil.virtual_memory().total / (1024.0 ** 3), 2)} GB")

# Screen size ( like, 15 inch, 21 inch)
print(f"\nScreen size: Not found")

# Wifi/Ethernet mac address
print("\nWifi/Ethernet MAC address:")
for interface in psutil.net_if_addrs():
    if interface == 'Wi-Fi' or interface == 'Ethernet':
        print(f"- {psutil.net_if_addrs()[interface][0].address}")

# Public IP address
print(f"\nPublic IP address: {psutil.net_if_addrs()['Ethernet'][1].address}")

# Windows version
print(f"\nWindows version: {platform.platform()}")