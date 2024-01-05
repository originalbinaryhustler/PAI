# from ip2location import IP2Location
import ssl
import socket
import time
import asyncio
# import whois
import requests
from bs4 import BeautifulSoup
import subprocess
import platform
import random
import concurrent.futures
import os
def append_color(color):
   for name, obj in globals().items():
       if callable(obj) and name in ['printb']:
           globals()[name + color] = obj

append_color('b')


def prnt_clr(text, color):
  if color == 'blue':
      printb('\033[94m' + text + '\033[0m')
  elif color == 'red':
      printb('\033[91m' + text + '\033[0m')
  elif color == 'green':
      printb('\033[92m' + text + '\033[0m')
  elif color == 'yellow':
      printb('\033[93m' + text + '\033[0m')
  elif color == 'light_purple':
      printb('\033[94m' + text + '\033[0m')
  elif color == 'purple':
      printb('\033[95m' + text + '\033[0m')
  elif color == 'cyan':
      printb('\033[96m' + text + '\033[0m')
  elif color == 'light_gray':
      printb('\033[97m' + text + '\033[0m')
  elif color == 'black':
      printb('\033[98m' + text + '\033[0m')

def printb(text):
    print('\033[94m' + text + '\033[0m')
def printr(text):
    print('\033[91m' + text + '\033[0m')
def imputb(text):
    input('\033[94m' + text + '\033[0m')
def inputr(text):
    input('\033[91m' + text + '\033[0m')

def input_clr(text, color):
  if color == 'blue':
      input('\033[94m' + text + '\033[0m')
  elif color == 'red':
      input('\033[91m' + text + '\033[0m')
  elif color == 'green':
      input('\033[92m' + text + '\033[0m')
  elif color == 'yellow':
      input('\033[93m' + text + '\033[0m')
  elif color == 'light_purple':
      input('\033[94m' + text + '\033[0m')
  elif color == 'purple':
      input('\033[95m' + text + '\033[0m')
  elif color == 'cyan':
      input('\033[96m' + text + '\033[0m')
  elif color == 'light_gray':
      input('\033[97m' + text + '\033[0m')
  elif color == 'black':
      input('\033[98m' + text + '\033[0m')



prnt_clr('''
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
                                            Predator AI Token presents...
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      ''', 'red')

time.sleep(1)
prnt_clr('''
    
    
    
    
    
    
        
                                ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗
                                ║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝
                                ║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ 
                                ║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ 
                                ║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗
                            lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝






      ''', 'cyan')
time.sleep(2)





def get_proxies():
 r = requests.get('https://free-proxy-list.net/')
 soup = BeautifulSoup(r.content, 'html.parser')
 table = soup.find('tbody')
 proxies = []
 prnt_clr(f'\n\nThe proxies are currently being scraped from the internet and subsquently checked.\nScraping and testing of proxies may take a few moments...\n', 'cyan')
 for row in table:
    if row.find_all('td')[4].text =='elite proxy':
        proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
        try:
               proxies.append(proxy)
               extract(proxy)
        except requests.ConnectionError as err:
            pass
#  printb(f'{proxies} \n')
 prnt_clr(f'The proxies above are all working when checked against https://httpbin.org/ip hence the 200 HTTP response code.\n Use #3. on the Main Menu the IP checker to get further information on the proxies found.\nFound {len(proxies)} proxies alltogether.\n', 'cyan')
 printr('''   
    / \-----------------------------------------------------------------, 
    \_,|                                                                | 
       |       Below is a list of all the proxies that where scraped.   | 
       |  ,--------------------------------------------------------------
       \_/______________________________________________________________/ 
       
       ''')
 return prnt_clr(f'''
            {proxies} \n
                              ▒█▀▄▒█▀▄░▄▀▄░▀▄▀░█▒██▀░▄▀▀
            above are all the ░█▀▒░█▀▄░▀▄▀░█▒█░█░█▄▄▒▄██ found. \n
         ''', 'yellow')

def extract(proxy):
 headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
 try:
    r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
    print(r.json(), str(r.status_code)+ '\n')
 except requests.ConnectionError as err:
    pass



def get_local_ipv6():
   get_network_info()
   printb('''
                    
░█▒░░▄▀▄░▄▀▀▒▄▀▄░█▒░░░░█▒█▀▄░█▒█░█▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
▒█▄▄░▀▄▀░▀▄▄░█▀█▒█▄▄▒░░█░█▀▒░▀▄▀░██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄

        ''')
   prnt_clr("This function will help you change the IPv6 Link-Local address manually.", 'yellow')
   prnt_clr("This can be useful for enhancing privacy and security.", 'yellow')
   prnt_clr("However, it may cause issues with network compatibility and performance.", 'yellow')
   
   prntr('''
Positive Implications:

Anonymity:
    \nChanging your IPv6 Link-Local address can provide a degree of anonymity. \nThis is because each time you change the address, it becomes harder to track your internet activity over time.
    \nPrevent IP Exhaustion: If you are using a lot of IPv6 addresses in your network, manually changing the addresses can help prevent IP exhaustion. \nThis is because IPv6 addresses are much more plentiful than IPv4 addresses, so the risk of running out of them is much lower.
\nNegative Implications:

Potential Network Disruptions: 
    \nIf not done correctly, manually changing the IPv6 Link-Local address can disrupt your network. \nThis is because the new address might not be properly configured, or it might conflict with an existing address. You might need to manually reconfigure your network settings to fix these issues.
    \nIncreased Complexity: Adding a function to your Python script to manually change the IPv6 Link-Local address can increase the complexity of your script. \nThis can make the script harder to maintain and debug. You might also need to add error handling code to deal with potential issues that arise from changing the IP address.
    \nPotential Security Risks: While changing the IPv6 Link-Local address can provide a degree of anonymity, it can also potentially expose you to security risks. \nFor example, if you change the address to a value that is predictable or that is used by another device, it could be easier for an attacker to target your device.
                     
\n                  
Note: If you don't know the interface name, you can find it by scrolling up''')
 
   interface = input('''              
.---------------------------------------------------------------------------------------------------------------------------.
| Enter the interface of the devices Temporary IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'---------------------------------------------------------------------------------------------------------------------------'      ''')
   if interface == 'q':
       printbr("Returning to Menu")
       main()
   ips = input('''
.---------------------------------------------------------------------------------------------------.
| Enter the  Temporary IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'---------------------------------------------------------------------------------------------------'      ''')

  
   if interface == 'q' or ips == 'q':
       printbr("Returning to Menu")
       main()
   change_ipv6_address(interface,ips)

def change_local_ipv6(interface,ips):
   printbr("Running the command to change the IPv6 Link-Local address...")
   
   if os.name == 'nt':
       printbr("Running on Windows...")
       command = f'netsh interface ipv6 set address "{interface}" static {ips}'
       subprocess.call(command, shell=True)
   elif os.name == 'posix' and 'darwin' in platform.system():
       printbr("Running on macOS...")
       command = f'sudo ifconfig {interface} inet6 {ips} prefixlen 64 alias'
       subprocess.call(command, shell=True)
   elif os.name == 'posix' and 'linux' in platform.system():
       printbr("Running on Linux...")
       command = f'sudo ip -6 addr add {ips} dev {interface}'
       subprocess.call(command, shell=True)
   else:
       printbr('Invalid OS')
       return

   printbr(f'Command complete. Check network config for {interface} Link-Local IPV6. It should now have a new Link-Local IPV6 address {ips}.')

def get_ipv6():
    get_network_info()
    printb('''
░█▒█▀▄░█▒█░█▀
░█░█▀▒░▀▄▀░██

                    
Local Network: \nIf you're changing your IPv6 address on a local network, it could cause issues with network communication.\nOther devices on your local network would no longer be able to reach you at your old IP address.\nHowever, since IPv6 addresses are typically used for local network communication, this is less of a concern.\n
Internet: \nIf you're changing your IPv6 address on the internet, it could cause issues with internet connectivity.\nWebsites and services that you're connected to would no longer be able to reach you at your old IP address.\nThis could result in loss of connection to those services.\n
Security: \nChanging your IP address can also provide a temporary measure of security.\nIf you suspect that your IP address has been compromised, changing it can prevent attackers from using it to access your network or internet services.
                
                
Note: If you don't know the interface name, you can find it by scrolling up''')
    interface = input('''                  
.-----------------------------------------------------------------------------------------------------------------.
| Enter the interface of the devices IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------------------------------'      ''')
    if interface == 'q':
       printb("Returning to Menu")
       main()
    ips = input('''
.-----------------------------------------------------------------------------------------.
| Enter the  IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------'      ''')

  
    if interface == 'q' or ips == 'q':
       printbr("Returning to Menu")
       main()
    
    change_ipv6(interface,ips)

def change_ipv6(interface, ips):
   if os.name == 'nt':
       command = f'netsh interface ipv6 set address "{interface}" static {ips} 64'
   elif os.name == 'posix' and 'darwin' in platform.system():
       command = f'sudo ip -6 addr add {ips}/64 dev {interface}'
   elif os.name == 'posix' and 'linux' in platform.system():
       command = f'sudo ifconfig {interface} inet6 {ips}/64'
   else:
       printbr('Invalid OS')
       return

   printbr(f'Running command: {command}')
   try:
       subprocess.check_call(command, shell=True)
   except subprocess.CalledProcessError as e:
       printbr(f'Error running command: {e}')
   



def get_temp_ipv6():
   get_network_info()
   printb('''
                    
░▀█▀▒██▀░█▄▒▄█▒█▀▄░░░█▒█▀▄░█▒█░█▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
░▒█▒░█▄▄░█▒▀▒█░█▀▒▒░░█░█▀▒░▀▄▀░██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄

        ''')
   printr("This function will help you change the IPv6 temporary address interval.")
   printr("This can be useful for enhancing privacy and security.")
   printr("However, it may cause issues with network compatibility and performance.")
 
   printb('''                                  
Pros:

Privacy: Changing the IPv6 temporary address can provide a level of privacy. Since the temporary address changes frequently, \nit can make it more difficult for external systems to track your device based on its IP address.
\nSecurity: If you suspect that your IP address has been compromised, changing it can prevent attackers from using it to access your network or internet services.
\n
Cons:

Network Compatibility: Changing the IPv6 temporary address can cause issues with network compatibility. \nSome networks and routers may not support the generation of temporary IPv6 addresses, or may not be configured to do so.
\nNetwork Performance: Frequent changes to the IPv6 temporary address can potentially affect network performance. \nEach time the address changes, the network has to establish a new connection, which can take time and resources.
\n                  
Note: If you don't know the interface name, you can find it by scrolling up.''')
   interface = input('''
 
                  
.---------------------------------------------------------------------------------------------------------------------------.
| Enter the interface of the devices Temporary IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'---------------------------------------------------------------------------------------------------------------------------'      ''')
 

   if interface == 'q':
       printb("Returning to main menu")
       main()
   temp_ipv6(interface)

def temp_ipv6(interface):
 printb("Running the command to change the IPv6 temporary address interval...")
 
 if os.name == 'nt':
     printb("Running on Windows...")
     command = f'netsh interface ipv6 set global randomizeidentifiers=enabled'
     subprocess.call(command, shell=True)
     command = f'netsh interface ipv6 set privacy state=enabled'
     subprocess.call(command, shell=True)
 elif os.name == 'posix' and 'darwin' in platform.system():
     printb("Running on macOS...")
     command = f'sudo sysctl -w net.inet6.ip6.use_tempaddr=1'
     subprocess.call(command, shell=True)
 elif os.name == 'posix' and 'linux' in platform.system():
     printb("Running on Linux...")
     command = f'sudo sysctl -w net.ipv6.conf.{interface}.temp_valid_lft=7200'
     subprocess.call(command, shell=True)
     command = f'sudo sysctl -w net.ipv6.conf.{interface}.temp_prefered_lft=3600'
     subprocess.call(command, shell=True)
 else:
     printb('Invalid OS')
     return

 printb('Command complete. Check network config for {interface} Temporary IPV6. It should now have a new temporary address.')


def ip_changer(interface_name, new_ip):
    if os.name == 'nt': # Windows
        # subnet_mask = f'{subnet_mask}.0.0.0' 
        command = f'netsh interface ip set address name="{interface_name}" static {new_ip}'
    else: # Linux
        command = f'sudo ip addr add {new_ip} dev {interface_name};'
    subprocess.run(command, shell=True)
    printb('Command ran check your network info')
 
def change_ip():
    get_network_info()
    prnt_clr(f'''

          
░█▄░█▒██▀░▀█▀░█░░▒█░▄▀▄▒█▀▄░█▄▀░░░█░█▀▄░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
░█▒▀█░█▄▄░▒█▒░▀▄▀▄▀░▀▄▀░█▀▄░█▒█▒░░█▒█▄▀▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄
    

          
          ''','green')
    interface_name = input('''
Note: If you don't know the interface name, you can find it by scrolling up.
 
                  
.---------------------------------------------------------------------------------------------------------------.
| Enter the interface of the devices IP Address you are trying to change or Enter q to return to the main Menu: |
'---------------------------------------------------------------------------------------------------------------'      ''')
    if interface_name == 'q':
       printr("Returning to Menu")
       main()
    new_ip = input('''
.---------------------------------------------------------------------------------------.
| Enter the  IP Address you are trying to change or Enter q to return to the main Menu: |
'---------------------------------------------------------------------------------------'      ''')

  
    if interface_name == 'q' or new_ip == 'q':
       printr("Returning to Menu")
       main()
    
    # default_gateway = input('Input new default gateway which is an IP you would want to change to: ')
    # subnet_mask = input('Linux and MAC e.g 24\nWindows e.g 255.255.255.0\n Input new Subnet Mask Gateway: ')
    ip_changer(interface_name, new_ip)
   
     

def get_network_info():
   printb('''
         
         
         ░█▄░█▒██▀░▀█▀░█░░▒█░▄▀▄▒█▀▄░█▄▀░░░█░█▄░█▒█▀░▄▀▄▒█▀▄░█▄▒▄█▒▄▀▄░▀█▀░█░▄▀▄░█▄░█
         ░█▒▀█░█▄▄░▒█▒░▀▄▀▄▀░▀▄▀░█▀▄░█▒█▒░░█░█▒▀█░█▀░▀▄▀░█▀▄░█▒▀▒█░█▀█░▒█▒░█░▀▄▀░█▒▀█

Loading...
         ''')
   if os.name == 'nt': # Windows
       command = 'ipconfig'
   else: # Linux
       command = 'ip a'
   result = subprocess.run(command, shell=True, capture_output=True, text=True)
   printb(result.stdout)
   return result.stdout

def mac_change(interface_name, new_mac):
    if os.name.lower() == 'nt': # Windows
        printb("Changing MAC address is only supported on Mac and Linux at this moment.  📼\n ")
    else:
        subprocess.run(f'sudo ifconfig {interface_name} down', shell=True)
        subprocess.run(f'sudo ifconfig {interface_name} hw ether {new_mac}', shell=True)
        subprocess.run(f'sudo ifconfig {interface_name} up', shell=True)
       
def change_mac():
    get_network_info()
    prnt_clr('''
          
          
░█▄▒▄█▒▄▀▄░▄▀▀░░▒▄▀▄░█▀▄░█▀▄▒█▀▄▒██▀░▄▀▀░▄▀▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
░█▒▀▒█░█▀█░▀▄▄▒░░█▀█▒█▄▀▒█▄▀░█▀▄░█▄▄▒▄██▒▄██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄
          
          
          ''', 'green')
    if os.name.lower() == 'nt': # Windows
        printr("Changing MAC address is only supported on Mac and Linux at this moment.\n\n To change your MAC on a Windows computer, open the Device Manager, expand the list of Network adapters,\n right-click or press and hold the network card for which you intend to change the MAC address,\n and select Properties in the contextual menu from there you will be able to change your MAC address on windows.\n")
        printr('Returning to menu.')
        main()
    else:
        interface_name = input('''
Note: If you don't know the interface name, you can find it by scrolling up.
 
                  
.------------------------------------------------------------------------------.
| Enter the Interface name of the device you wish to change the MAC address of:|
'------------------------------------------------------------------------------'      ''')
        if interface_name == 'q':
            printb("Returning to Menu")
            main()
        new_mac = input('''
    .------------------------------------------------------------.
    | example mac: 00:11:22:33:44:55 Enter the new MAC address:: |
'------------------------------------------------------------'      ''')
    
        mac_change(interface_name, new_mac)
    # change_mac_choice = input("Do you want to change the MAC address? (yes/no): ")
    # if change_mac_choice.lower() == 'no' or change_mac_choice.lower() == 'n':
    #     printb('''
    #       ░█▄░█▒██▀░▀▄▀░▀█▀
    #       ░█▒▀█░█▄▄░█▒█░▒█▒

    #       ''')
    # else:
       
def geo_info(ip_address):
   
    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)
    data = response.json()


    
    result = ""
    for key, value in data.items():
       result += f"'{key}': '{value}', \n"
    return result


def get_geo_info():
    get_network_info()
    printb('''
          
          
░█▒█▀▄░░░▀█▀▒█▀▄▒▄▀▄░▄▀▀░█▄▀▒██▀▒█▀▄
░█░█▀▒▒░░▒█▒░█▀▄░█▀█░▀▄▄░█▒█░█▄▄░█▀▄

          
        ''')
    ip_address = input('''
Note: If you don't know the interface name, you can find it by scrolling up.
 
                  
.----------------------------------------------------------------------------------------------------.
| Enter the IP address you wish to ascertain information from or Enter q to return to the main Menu: |
'----------------------------------------------------------------------------------------------------'   ''')
    if ip_address == 'q':
       printb("Returning to Menu")
       main()
    # Check if the user has encrypted traffic
    check_encrypted_traffic = is_encrypted_traffic(ip_address)
    printb(f"\n The likelyhood user has Encrypted Traffic: {check_encrypted_traffic}")
    
#     is_vpn_or_proxy = ip_address in known_vpn_or_proxy_ips
#     printb(f"Is VPN or Proxy: {is_vpn_or_proxy}")

    

#     # Check if the user is using a proxy
#     is_proxy = ip_address in known_proxy_ips
#    printb(f"Is Proxy: {is_proxy}")
   
    result = geo_info(ip_address)
    return f"\nGeoInfo for {ip_address}:\n{result}\n"


def is_encrypted_traffic(ip_address):
   response = requests.get(f'https://www.ssllabs.com/ssltest/analyze.html?d={ip_address}')
   return 'Protocols' in response.text
# def is_proxy(ip_address):
#    ip2location = IP2Location.IP2Location()
#    record = ip2location.get_all(ip_address)
#    return record.is_proxy == 1
# def is_vpn_or_proxy(ip_address):
#    ip2location = IP2Location.IP2Location()
#    record = ip2location.get_all(ip_address)
#    return record.is_proxy == 1 or record.is_vpn == 1

def change_DNS():
    printb('''
          
          
░█▀▄░█▄░█░▄▀▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
▒█▄▀░█▒▀█▒▄██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄

           
          ''')
    dns = input('''Examples DNS: \nGoogle 8.8.8.8 - 8.8.4.4\nCloudfare 1.1.1.1 - 1.0.0.1 \nOpenDNS 208.67.222.222 - 208.67.220.220 \n\n
.----------------------------------------------.
| Input DNS or enter q to return to main menu: |
'----------------------------------------------'      ''')
    if dns.lower() == 'q':
        printr('\nReturning to Menu.\n')
        main()
    DNS_changer(dns)
def DNS_changer(dns):
   os_type = platform.system()
   printb('Changing DNS now.. Check your configurations after.')
   if os_type == 'Windows':
       os.system(f'netsh interface ip set dns name="Local Area Connection" static {dns}')
   elif os_type == 'Linux':
       with open('/etc/resolv.conf', 'w') as f:
           f.write(f'nameserver {dns}\n')
   elif os_type == 'Darwin':
       os.system(f'networksetup -setdnsservers Wi-Fi {dns}')
   else:
       printb('Unsupported OS')

def reset_dns():
   printr('''

In order to reset manually you must:

- Power off your router: Start by unplugging your router from the power outlet. Wait for about 10 seconds to ensure the router is fully powered off. This step is necessary to ensure that the router is completely reset

- Wait for a few moments: After powering off your router, wait for a few minutes. This is to allow the router to completely reset

- Power on your router: Once you've waited for a few minutes, plug your router back into the power outlet and turn it on. The router will start up and, in the process, it will request a new IP address from your Internet Service Provider (ISP)

- Verify the new IP address: After your router has restarted, you can verify that it has received a new IP address by checking your IP address. 

        
.-------------.
| Checking OS |
'-------------'

        ''')
   os_type = platform.system()

   if os_type == 'Windows':
       commands = [
           'ipconfig /flushdns',
           'ipconfig /registerdns',
           'ipconfig /release',
           'ipconfig /renew',
           'netsh winsock reset',
           'netsh int ip reset'
       ]
   elif os_type == 'Darwin': # MacOS
       commands = [
           'sudo killall -HUP mDNSResponder',
           'sudo dscacheutil -flushcache'
       ]
   elif os_type == 'Linux':
       commands = [
           'sudo systemd-resolve --flush-caches',
           'sudo /etc/init.d/nscd restart'
       ]
   else:
       printb(f"Unsupported OS: {os_type}")
       return

   for command in commands:
       subprocess.call(command, shell=True)
       
def static_ip_getter():
    get_network_info()  
    interface = input(''' 
          
          
░▄▀▀░▀█▀▒▄▀▄░▀█▀░█░▄▀▀░░░█▒█▀▄░░
▒▄██░▒█▒░█▀█░▒█▒░█░▀▄▄▒░░█░█▀▒▒░

The main purpose of this function is to provide a way to manually set a static IP address for a network interface. \nThis can be useful in situations where you want to have a consistent IP address for a device, \nsuch as a server or a device that hosts a service that needs to be accessible from a specific IP address.

Pros and Cons:

Pros:

Ease of Access: \nHaving a static IP address means that you can always access your device from the same IP address. \nThis can be particularly useful if you are hosting a service that needs to be accessible from a specific IP address.
Troubleshooting: \nStatic IP addresses can make it easier to troubleshoot network issues. Since the IP address does not change, \nyou can always connect to the device using the same IP address.
\n\nCons:

Security: Static IP addresses can potentially expose your device to security risks. \nSince the IP address does not change, it can be easier for attackers to target your device.
Flexibility: Static IP addresses are less flexible than dynamic IP addresses. \nIf you need to move your device to a different network or location, you will need to manually change the IP address

Note: If you don't know the interface name, you can find it by scrolling up.
 
                  
.------------------------------------------------------------------------------------------------------------------------.
| Enter the interface of the devices Static IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'------------------------------------------------------------------------------------------------------------------------'      ''')
    if interface == 'q' or ips == 'q':
       printr("Returning to Menu")
       main()
    ips = input('''
.-----------------------------------------------------------------------------------------------.
| Enter the Static IPV6 Address you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------------'      ''')

  
    if interface == 'q' or ips == 'q':
       printr("Returning to Menu")
       main()
    set_static_ip(interface,ips)

         
    
    
    
def set_static_ip(interface, ip):
   os_type = platform.system()

   if os_type == 'Windows':
       command = f'netsh interface ip set address name="{interface}" static {ips} '
       subprocess.call(command, shell=True)
   elif os_type == 'Darwin': # MacOS
       command = f'sudo ifconfig {interface} {ips} '
       subprocess.call(command, shell=True)
   elif os_type == 'Linux':
       command = f'sudo ifconfig {interface} {ips} '
       subprocess.call(command, shell=True)
   else:
       printr(f"Unsupported OS: {os_type}")


def subgate_getter():
    get_network_info()
    printb(''' 
          
          
░▄▀▀░█▒█░██▄░█▄░█▒██▀░▀█▀░█▄▒▄█▒▄▀▄░▄▀▀░█▄▀░░░
▒▄██░▀▄█▒█▄█░█▒▀█░█▄▄░▒█▒░█▒▀▒█░█▀█▒▄██░█▒█▒░░
    ''')
    prnt_clr('''

Subnet Mask:

Network Size: \nThe subnet mask determines the size of the network. A smaller subnet mask results in a smaller network, which can limit the number of devices that can connect to the network. Conversely, \na larger subnet mask results in a larger network, which can accommodate more devices.
\nIP Address Usage: \nChanging the subnet mask can affect the way IP addresses are used within the network. If you increase the subnet mask, you may be able to use a larger share of host addresses, \nbut this requires reconfiguring all routers and other statically assigned computers and renewing all DHCP clients.


          
Note: If you don't know the interface name, you can find it by scrolling up.
''', 'cyan')
    interface = (''' 
 
                  
.-----------------------------------------------------------------------------------------------------------.
| Enter the interface of the interface name you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------------------------'     ''')
    if interface == 'q':
       printr("Returning to Menu")
       main()
    ips = input('''
.-----------------------------------------------------------------------------------------------.
| Enter the SubnetMask Address you are trying to change or Enter q to return to the main Menu:  |
'-----------------------------------------------------------------------------------------------'     ''')

  
    if subnet_mask == 'q' or subnet_mask == 'q':
       printr("Returning to Menu")
       main()
    
    
    
    
    set_subgate(interface,subnet_mask)
def set_subgate(interface, subnet_mask):
   os_type = platform.system()

   if os_type == 'Windows':
       command = f'netsh interface ip set address name="{interface}" {subnet_mask}'
       subprocess.call(command, shell=True)
   elif os_type == 'Darwin': # MacOS
       command = f'sudo ifconfig {interface}  netmask {subnet_mask} up'
       subprocess.call(command, shell=True)
   elif os_type == 'Linux':
       command = f'sudo ifconfig {interface}  netmask {subnet_mask} up'
       subprocess.call(command, shell=True)
   else:
       printr(f"Unsupported OS: {os_type}")

def default_gateway_setter():
   get_network_info()
   printb(''' 
         
░▄▀▒▒▄▀▄░▀█▀▒██▀░█░░▒█▒▄▀▄░▀▄▀
░▀▄█░█▀█░▒█▒░█▄▄░▀▄▀▄▀░█▀█░▒█▒
    ''')

   prnt_clr('''

Default Gateway:

Network Routing: \nThe default gateway is the IP address of the router that a device uses to access the internet or other networks. Changing the default gateway can affect how a device routes its network traffic. \nIf the new default gateway is not reachable or is not configured correctly, it can cause network connectivity issues.
\nNetwork Security: \nThe default gateway is a potential entry point for external traffic to enter your network. If the default gateway is compromised, it can potentially expose your network to security risks. \nTherefore, it's important to ensure that the default gateway is secure and is not an easy target for attackers.

Network Routing: \nThe gateway is the IP address of the router that a device uses to access the internet or other networks. Changing the gateway can affect how a device routes its network traffic. \nIf the new gateway is not reachable or is not configured correctly, it can cause network connectivity issues.
\nNetwork Security: \nThe gateway is a potential entry point for external traffic to enter your network. If the gateway is compromised, it can potentially expose your network to security risks. \nTherefore, it's important to ensure that the gateway is secure and is not an easy target for attackers.
         
Note: If you don't know the interface name, you can find it by scrolling up.
''', 'yellow')
   interface = (''' 
 
                
.-----------------------------------------------------------------------------------------------------------.
| Enter the interface of the interface name you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------------------------'    ''')
   if interface == 'q':
      printr("Returning to Menu")
      main()
   default_gateway = input('''
.-----------------------------------------------------------------------------------------------.
| Enter the Default Gateway Address you are trying to change or Enter q to return to the main Menu: |
'-----------------------------------------------------------------------------------------------'    ''')

 
   if default_gateway == 'q' or default_gateway == 'q':
      printr("Returning to Menu")
      main()
   
   
   
   
   set_default_gateway(interface,default_gateway)
def set_default_gateway(interface, default_gateway):
  os_type = platform.system()

  if os_type == 'Windows':
      command = f'netsh interface ip set address name="{interface}" gateway={default_gateway}'
      subprocess.call(command, shell=True)
  elif os_type == 'Darwin': # MacOS
      command = f'sudo route -n delete default && sudo route -n add default {default_gateway}'
      subprocess.call(command, shell=True)
  elif os_type == 'Linux':
      command = f'sudo route del default && sudo route add default gw {default_gateway}'
      subprocess.call(command, shell=True)
  else:
      printr(f"Unsupported OS: {os_type}")


def about():
    printb('''\n
▒▄▀▄░██▄░▄▀▄░█▒█░▀█▀
░█▀█▒█▄█░▀▄▀░▀▄█░▒█▒


    ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    ''')
          
    prnt_clr('''
PREDATOR AI TOKEN
░▄▀▀░▄▀▄░█▄░█░▀█▀▒█▀▄▒▄▀▄░▄▀▀░▀█▀ :
░▀▄▄░▀▄▀░█▒▀█░▒█▒░█▀▄░█▀█░▀▄▄░▒█▒ :     0x000000000000000000000000
    ''', 'cyan')
    
    prnt_clr('''

                             mm                  mm                  
                            m@@                  @@    @@            
                             @@                        @@            
*@@*    m@    *@@*  mm@*@@   @@m@@@@m   m@@*@@@*@@@  @@@@@@   mm@*@@ 
  @@   m@@@   m@   m@*   @@  @@    *@@  @@   **  @@    @@    m@*   @@
   @@ m@  @@ m@    !@******  !@     @@  *@@@@@m  !@    @@    !@******
    @@@    @!!     !@m    m  !!!   m@!       @@  !@    @!    !@m    m
    !@!!   !:!     !!******  !!     !!  *!   @!  !!    !!    !!******
    !!!    !:!     :!!       :!!   !!!  !!   !!  !!    !!    :!!            :
     :      :       : : ::   : : : ::   : :!:  : : :   ::: :  : : ::        :     https://predator-ai.net
     ''', 'green')
     
    prnt_clr('''

Our script boasts a set of network scripts that can automate tasks which can be advantageous in many ways:

Network Security: \nThe script can change the IP address of a given network interface, \nwhich can help protect against IP-based attacks. \nBy changing the IP address, the system becomes harder to locate and target, enhancing its security.
\nMAC Address Changing: \nThe script can change the MAC address of a given network interface. \nThis can help protect against MAC-based attacks, \nas the MAC address is a unique identifier for network interfaces.
\nDNS Changing: \nThe script can change the DNS settings of the system. \nThis can help protect against DNS-based attacks, \nas it can prevent attackers from using DNS to redirect traffic to malicious servers.
\nEncryption Checking: \nThe script can check if a given IP address is using encrypted traffic. \nThis can help protect against traffic interception and eavesdropping attacks.    
          ''', 'yellow')

def quit():
    prnt_clr(''' 
                 ,-----------------------------------o
                (_    Terminating the programme..._   /~ 
                                    
                  ''', 'green')
    printr('''   
                    
    ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    
    ''') 
    exit()
    sys.exit(0)
  
  
async def check_encryption():
  printb('''
        
▒▄▀▄▒██▀░▄▀▀░░░░░░░░░▄▀▀░█▄█▒██▀░▄▀▀░█▄▀▒██▀▒█▀▄
░█▀█░█▄▄▒▄██▒░▒░▀▀▒░░▀▄▄▒█▒█░█▄▄░▀▄▄░█▒█░█▄▄░█▀▄
        
        
        
        ''')
  server = input('Enter the server you wish to check: ')
  await get_server(server)
#   await check_connectivity(server)
#   await get_ip_for_server(server)
async def get_server(server):
  # Resolve the DNS name to an IP address
  ip_address = socket.gethostbyname(server)


  # Check if the server has an SSL certificate
  is_ssl_certificate = False
  ssl_certificate_details = None
  try:
      ssl_certificate = ssl.get_server_certificate((server, 443))
      is_ssl_certificate = True
      ssl_certificate_details = ssl.X509(ssl_certificate)
  except Exception as e:
      printr(f"Unable to ascertain if server has an SSL certificate:\n {e}\n\n")

  # Check if the server is using AES encryption
  is_aes_encryption = False
  try:
      context = ssl.create_default_context()
      with context.wrap_socket(socket.socket(), server_hostname=server) as s:
          s.connect((ip_address, 443))
          cipher = s.cipher()
          is_aes_encryption = cipher[0] == 'AES'
  except Exception as e:
      printr(f"Unable to ascertain if server is using AES encryption:\n {e}\n\n")

  # Check the HTTP status code
  try:
      response = requests.get(f'https://{server}')
      is_accessible = response.status_code == 200
  except Exception as e:
      printr(f"Unable to ascertain if server is accessible:\n {e}\n\n")

  # Check the website's connectivity
async def check_connectivity():
  printb('''
        
        
░▄▀▀▒██▀▒█▀▄░█▒█▒██▀▒█▀▄░░░▄▀▀░█▄█▒██▀░▄▀▀░█▄▀▒██▀▒█▀▄
▒▄██░█▄▄░█▀▄░▀▄▀░█▄▄░█▀▄▒░░▀▄▄▒█▒█░█▄▄░▀▄▄░█▒█░█▄▄░█▀▄
        
        
        ''')
  server = input('Enter the server you wish to check: ')
  await get_ip_for_server(server)
async def get_ip_for_server(server):
    try:
        response = await requests.get(f'https://{server}')
        is_connected = response.status_code == 200
    except Exception as e:
        printr(f"Unable to ascertain if server is connected:\n {e}\n\n")
        is_connected = False
    return is_connected
    is_connected = await check_connectivity()

    # is_connected = asyncio.run(check_connectivity(server))

  # Check the server's hosting provider
#   try:
#       w = whois.whois(server)
#       is_hosting_provider = w.registrar is not None
#   except Exception as e:
#       printb(f"Unable to ascertain if server has a hosting provider: {e}")

  # Check the server's nameservers
    try:
        dns_records = socket.getaddrinfo(server, None)
        is_nameservers = len(dns_records) > 0
    except Exception as e:
        printr(f"Unable to ascertain if server has nameservers:\n {e}\n\n")

    # Check the server's web server
    try:
        response = requests.get(f'https://{server}')
        server_header = response.headers.get('Server')
        is_web_server = server_header is not None
    except Exception as e:
        printr(f"Unable to ascertain if server has a web server:\n {e}\n\n")

    # Check the server's DNS provider
    try:
        dns_records = socket.getaddrinfo(server, None)
        dns_provider = dns_records[0][2]
        is_dns_provider = dns_provider is not None
    except Exception as e:
        printr(f"Unable to ascertain if server has a DNS provider:\n {e}\n\n")

    # Check the server's HTTP response headers
    try:
        response = requests.get(f'https://{server}')
        headers = response.headers
    except Exception as e:
        printr(f"Unable to ascertain server's HTTP response headers:\n {e}\n\n")
        headers = None

    # Check the server's IP reputation
    try:
        # This requires a third-party service like VirusTotal
        printb(f"IP address of server: {ip_address}")
    except Exception as e:
        printr(f"Unable to ascertain server's IP reputation: {e}")

    return is_ssl_certificate,+'\n'+is_aes_encryption,+'\n'+is_accessible,+'\n'+is_connected,+'\n'+is_hosting_provider,+'\n'+is_nameservers,+'\n'+is_web_server,+'\n'+is_dns_provider,+'\n'+headers,+'\n'+ssl_certificate_details

    
options = {
     '''
     
     System
     
     ''' : None,
     "Key: A tool auto starts on selection has the '-A' sign":None,
     "-1: Information about this script" : about,
     " 0: Terminate the program" : quit,
     '''
     
     White Hat
     
     ''' : None,
     "1:  Get Proxies -A" : get_proxies,
     "2:  Get Network Information" : get_network_info,
     "3:  Get GeoInfof from IP Address" : get_geo_info,
     "4:  Change IPV4 Address" : change_ip,
     "5:  Change IPV6 Address" : get_ipv6,
     "6:  Change Local IPV6 Address" : get_local_ipv6,
     "7:  Change Temporary IPV6 Address Interval Change" : get_temp_ipv6,
     "8:  Change MAC Address" : change_mac,
     "9:  Change Static IP" : static_ip_getter,
     "10: Change SubnetMask" : subgate_getter,
     "11: Change Default Gateway" : default_gateway_setter,
     "12: Change DNS" : change_DNS,
     "13: Reset DNS and IP Address -A" : reset_dns,
     '''
     
     Grey Hat
     
     ''' : None,
     "G1: Check Encrypted Traffic - Coming soon current version prone to bugging -" : check_encryption,
     "G2: Check Website / Server - Coming soon current version prone to bugging -" : check_connectivity,
     "G3: Clear CMD History -A" : None,
     "G4: Traceroute" : None,
     "G5: Wireshark" : None,
     "G6: Ping" : None,
     '''
     
     Black Hat
     
     ''' : None,
     "B1: Bettercap" : None,
     "B2: Malware Key Logger" : None,
     "B3: Self Replicating Virus" : None,
     "B4: Trojan Horse Remote Connection" : None,
     "B5: Zip Cracker" : None,
     "B6: Password Hash Cracker" : None,
}





def menu(options):
    
    printb('''
.------------------.
| Choose an option |
'------------------'
          ''')
    for key, value in options.items():
        printb(f"{key}")


   
def main():
    printr('Version.0.0.08')
    printr('''

                                ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗
                                ║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝
                                ║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ 
                                ║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ 
                                ║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗
                            lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝
    ''')
    time.sleep(1)

    prnt_clr('''PREDATOR AI TOKEN
░▄▀▀░▄▀▄░█▄░█░▀█▀▒█▀▄▒▄▀▄░▄▀▀░▀█▀ :
░▀▄▄░▀▄▀░█▒▀█░▒█▒░█▀▄░█▀█░▀▄▄░▒█▒ :     0x000000000000000000000000
          ''', 'yellow')
    time.sleep(1)
   

    while True:
        
        menu(options)
        choice = input( ''' 
 .-------------------.  (-1/13):
(| enter your choice |) (G1/G6):
 '-------------------'  (B1/B6):       ... ? ''')

        # if choice in options:
        #     options[choice]()
        
        if choice == "1":
            proxies = get_proxies()
            printr(f"\nComplete\n")
        elif choice == "2":
            network_info = get_network_info()
            printr(f"\nComplete\n")
            
        elif choice == "3":
            geo_info = get_geo_info()
            print(geo_info)
        elif choice == "4":
            new_ip = change_ip()
            print(new_ip)
        elif choice == "5":
            new_ip = get_ipv6()
            print('Changing IPV6 check your network information.')
        elif choice == "6":
            new_ip = get_local_ipv6()
            print('Changing Local IPV6 check your network information.')
        elif choice == "7":
            new_ip = get_temp_ipv6()
            print('Changing Temporary IPV6 Interval check your network information.')
        
        elif choice == "8":
            new_mac = change_mac()
            print(new_mac)
        elif choice == "9":
            static_ip_getter()
            print('Check your network configuration to see if the effects have taken place.')
        elif choice == "10":
            subgate_getter()
            print('Check your network configuration to see if the effects have taken place.')
        elif choice == "11":
            change_DNS()
            print('Check your network configuration')
        elif choice == "12":
            default_gateway_setter()
            print('Check your network configuration')
        elif choice == "13":
            reset_dns()
            print('DNS Reset')
        elif choice.lower == "g1":
            encrypted_website = asyncio.run(check_encryption())
            print(encrypted_website)
        elif choice.lower == "g2":
            get_connectivity = asyncio.run(check_connectivity())
            print(get_connectivity)
        elif choice == "-1":
            about()
        elif choice == '0' :
            printr('''
                                ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗
                                ║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝
                                ║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ 
                                ║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ 
                                ║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗
                            lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝
            ''')
            quit()
            sys.exit(0)
        else:
            printb('''
                                          ░█░█▄░█░█▒█▒▄▀▄░█▒░░█░█▀▄
                                          ░█░█▒▀█░▀▄▀░█▀█▒█▄▄░█▒█▄▀
                  ''')

        continue_choice = input('''
                                
.--------------------------------------------.
| Press the Enter key or Return 'no' to quit |
'--------------------------------------------'        ...?    ''')
        if continue_choice.lower() == 'yes' or continue_choice.lower() == 'y':
            main()
        elif continue_choice.lower() == 'no' or continue_choice.lower() == 'n':
            printr('''
                                                   
                                  ,-----------------------------------o
                                 (_    Terminating the programme..._   /~ 
                                   
                                   
                                   
     ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
 lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    
                  ''')
            exit()
            sys.exit(0)
            break
        else:
            printb('''
                      
                     _____________ 
                    |  _________  |
                    | | Loading | |
                    | |_________| |
                    |_____________|
                    
                    
                    
                    
     ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
 lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
 
 匚ㄖ几ㄒ尺卂匚ㄒ :     0x0000000000000
 
 山乇乃丂丨ㄒ乇   :     https://Predator-AI.net                   ''')           
main()
if __name__ == "__main__":
    app.run(debug=True)