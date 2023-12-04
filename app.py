# from ip2location import IP2Location
import ssl
import socket

import asyncio
# import whois
import requests
from bs4 import BeautifulSoup
import subprocess
import platform
import random
import concurrent.futures
import os




def get_proxies():
 r = requests.get('https://free-proxy-list.net/')
 soup = BeautifulSoup(r.content, 'html.parser')
 table = soup.find('tbody')
 proxies = []
 print(f'\n\nThe proxies are currently being scraped from the internet and subsquently checked.\nScraping and testing of proxies may take a few moments...\n')
 for row in table:
    if row.find_all('td')[4].text =='elite proxy':
        proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
        try:
               proxies.append(proxy)
               extract(proxy)
        except requests.ConnectionError as err:
            pass
#  print(f'{proxies} \n')
 print(f'The proxies above are all working when checked against https://httpbin.org/ip hence the 200 HTTP response code.\n Use # 5. on the Main Menu the IP checker to get further information on the proxies found.\nFound {len(proxies)} proxies alltogether.\n')
 print('''   
    / \-----------------------------------------------------------------, 
    \_,|                                                                | 
       |       Below is a list of all the proxies that where scraped.   | 
       |  ,--------------------------------------------------------------
       \_/______________________________________________________________/ 
       
       ''')
 return f'''
            {proxies} \n
                              ▒█▀▄▒█▀▄░▄▀▄░▀▄▀░█▒██▀░▄▀▀
            above are all the ░█▀▒░█▀▄░▀▄▀░█▒█░█░█▄▄▒▄██ found. \n
         '''

def extract(proxy):
 headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
 try:
    r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
    print(r.json(), str(r.status_code)+ '\n')
 except requests.ConnectionError as err:
    pass

def ip_changer(interface_name, new_ip):
    if os.name == 'nt': # Windows
        # subnet_mask = f'{subnet_mask}.0.0.0' 
        command = f'netsh interface ip set address name="{interface_name}" static {new_ip}'
    else: # Linux
        command = f'sudo ip addr add {new_ip} dev {interface_name};'
    subprocess.run(command, shell=True)
    print('Command ran check your network info')
 
def change_ip():
    print('''

          
░█▄░█▒██▀░▀█▀░█░░▒█░▄▀▄▒█▀▄░█▄▀░░░█░█▀▄░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
░█▒▀█░█▄▄░▒█▒░▀▄▀▄▀░▀▄▀░█▀▄░█▒█▒░░█▒█▄▀▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄

          
          ''')
    interface_name = input('Input the Interface name of the device you wish to change: ')
    new_ip = input('Input the new IP Address: ')
    
    # default_gateway = input('Input new default gateway which is an IP you would want to change to: ')
    # subnet_mask = input('Linux and MAC e.g 24\nWindows e.g 255.255.255.0\n Input new Subnet Mask Gateway: ')
    ip_changer(interface_name, new_ip)
   
     

def get_network_info():
   print('''
         
         
         ░█▄░█▒██▀░▀█▀░█░░▒█░▄▀▄▒█▀▄░█▄▀░░░█░█▄░█▒█▀░▄▀▄▒█▀▄░█▄▒▄█▒▄▀▄░▀█▀░█░▄▀▄░█▄░█
         ░█▒▀█░█▄▄░▒█▒░▀▄▀▄▀░▀▄▀░█▀▄░█▒█▒░░█░█▒▀█░█▀░▀▄▀░█▀▄░█▒▀▒█░█▀█░▒█▒░█░▀▄▀░█▒▀█

         ''')
   if os.name == 'nt': # Windows
       command = 'ipconfig'
   else: # Linux
       command = 'ip a'
   result = subprocess.run(command, shell=True, capture_output=True, text=True)
   print(result.stdout)
   return result.stdout

def mac_change(interface_name, new_mac):
    if os.name.lower() == 'nt': # Windows
        print("Changing MAC address is only supported on Mac and Linux at this moment.  📼\n ")
    else:
        subprocess.run(f'sudo ifconfig {interface_name} down', shell=True)
        subprocess.run(f'sudo ifconfig {interface_name} hw ether {new_mac}', shell=True)
        subprocess.run(f'sudo ifconfig {interface_name} up', shell=True)
       
def change_mac():
    print('''
          
          
░█▄▒▄█▒▄▀▄░▄▀▀░░▒▄▀▄░█▀▄░█▀▄▒█▀▄▒██▀░▄▀▀░▄▀▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
░█▒▀▒█░█▀█░▀▄▄▒░░█▀█▒█▄▀▒█▄▀░█▀▄░█▄▄▒▄██▒▄██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄
          
          
          ''')
    if os.name.lower() == 'nt': # Windows
        print("Changing MAC address is only supported on Mac and Linux at this moment.\n\n To change your MAC on a Windows computer, open the Device Manager, expand the list of Network adapters,\n right-click or press and hold the network card for which you intend to change the MAC address,\n and select Properties in the contextual menu from there you will be able to change your MAC address on windows.\n")
    else:
        interface_name = input('Input the Interface name of the device you wish to change the MAC address of\n')
        new_mac = input("Enter the new MAC address: \n example: 00:11:22:33:44:55\n Enter:  ")
        mac_change(interface_name, new_mac)
    # change_mac_choice = input("Do you want to change the MAC address? (yes/no): ")
    # if change_mac_choice.lower() == 'no' or change_mac_choice.lower() == 'n':
    #     print('''
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
    print('''
          
          
░█▒█▀▄░░░▀█▀▒█▀▄▒▄▀▄░▄▀▀░█▄▀▒██▀▒█▀▄
░█░█▀▒▒░░▒█▒░█▀▄░█▀█░▀▄▄░█▒█░█▄▄░█▀▄

          
        ''')
    ip_address = input("Enter the IP address: ")
    # Check if the user has encrypted traffic
    check_encrypted_traffic = is_encrypted_traffic(ip_address)
    print(f"\n The likelyhood user has Encrypted Traffic: {check_encrypted_traffic}")
    
#     is_vpn_or_proxy = ip_address in known_vpn_or_proxy_ips
#     print(f"Is VPN or Proxy: {is_vpn_or_proxy}")

    

#     # Check if the user is using a proxy
#     is_proxy = ip_address in known_proxy_ips
#    print(f"Is Proxy: {is_proxy}")
   
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
    print('''
          
          
░█▀▄░█▄░█░▄▀▀░░░▄▀▀░█▄█▒▄▀▄░█▄░█░▄▀▒▒██▀▒█▀▄
▒█▄▀░█▒▀█▒▄██▒░░▀▄▄▒█▒█░█▀█░█▒▀█░▀▄█░█▄▄░█▀▄

           
          ''')
    dns = input('Examples DNS: google 8.8.8.8 - 8.8.4.4\n cloudfare 1.1.1.1 - 1.0.0.1 \n openDNS 208.67.222.222 - 208.67.220.220 \nInput DNS:  ')
    DNS_changer(dns)
def DNS_changer(dns):
   os_type = platform.system()
   print('Changing DNS now.. Check your configurations after.')
   if os_type == 'Windows':
       # For Windows, you can use the `netsh` command to change the DNS settings
       os.system(f'netsh interface ip set dns name="Local Area Connection" static {dns}')
   elif os_type == 'Linux':
       # For Linux, you can use the `resolv.conf` file to change the DNS settings
       with open('/etc/resolv.conf', 'w') as f:
           f.write(f'nameserver {dns}\n')
   elif os_type == 'Darwin':
       # For MacOS, you can use the `networksetup` command to change the DNS settings
       os.system(f'networksetup -setdnsservers Wi-Fi {dns}')
   else:
       print('Unsupported OS')

def reset_dns():
   print('''

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
           'netsh winsock reset'
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
       print(f"Unsupported OS: {os_type}")
       return

   for command in commands:
       subprocess.call(command, shell=True)
       
def static_ip_getter():
    print(''' 
          
          
░▄▀▀░▀█▀▒▄▀▄░▀█▀░█░▄▀▀░░░█▒█▀▄░░░▒░░░▄▀▀░█▒█░██▄░█▄░█▒██▀░▀█▀░█▄▒▄█▒▄▀▄░▄▀▀░█▄▀░░░▒░░░▄▀▒▒▄▀▄░▀█▀▒██▀░█░░▒█▒▄▀▄░▀▄▀░░
▒▄██░▒█▒░█▀█░▒█▒░█░▀▄▄▒░░█░█▀▒▒░░█▒░▒▄██░▀▄█▒█▄█░█▒▀█░█▄▄░▒█▒░█▒▀▒█░█▀█▒▄██░█▒█▒░░█▒░░▀▄█░█▀█░▒█▒░█▄▄░▀▄▀▄▀░█▀█░▒█▒▒░

          
          ''' )
    os_type = platform.system()
    interface = input('Input Interface Name:  ')
    ip = input('Enter IP Address e.g 192.168.1.2:  ')
    subnetmask = input('Enter subnetmask e.g 192.168.1.1:  ')
    if os_type == 'Windows':
        geteway = input('Enter a gateway e.g 255.255.255.0:  ')
def set_static_ip(interface, ip, subnet_mask, gateway='24'):
   os_type = platform.system()

   if os_type == 'Windows':
       command = f'netsh interface ip set address name="{interface}" static {ip} {subnet_mask} {gateway}'
       subprocess.call(command, shell=True)
   elif os_type == 'Darwin': # MacOS
       command = f'sudo ifconfig {interface} {ip} netmask {subnet_mask} up'
       subprocess.call(command, shell=True)
   elif os_type == 'Linux':
       command = f'sudo ifconfig {interface} {ip} netmask {subnet_mask} up'
       subprocess.call(command, shell=True)
   else:
       print(f"Unsupported OS: {os_type}")

def quit():
    print(''' 
                                  ,-----------------------------------o
                                 (_    Terminating the programme..._   /~" 
                                    
                  ''')
    print('''   
                    
▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    
    ''') 
    exit()
    sys.exit(0)
  
  
async def check_encryption():
  print('''
        
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
      print(f"Unable to ascertain if server has an SSL certificate:\n {e}\n\n")

  # Check if the server is using AES encryption
  is_aes_encryption = False
  try:
      context = ssl.create_default_context()
      with context.wrap_socket(socket.socket(), server_hostname=server) as s:
          s.connect((ip_address, 443))
          cipher = s.cipher()
          is_aes_encryption = cipher[0] == 'AES'
  except Exception as e:
      print(f"Unable to ascertain if server is using AES encryption:\n {e}\n\n")

  # Check the HTTP status code
  try:
      response = requests.get(f'https://{server}')
      is_accessible = response.status_code == 200
  except Exception as e:
      print(f"Unable to ascertain if server is accessible:\n {e}\n\n")

  # Check the website's connectivity
async def check_connectivity():
  print('''
        
        
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
        print(f"Unable to ascertain if server is connected:\n {e}\n\n")
        is_connected = False
    return is_connected
    is_connected = await check_connectivity()

    # is_connected = asyncio.run(check_connectivity(server))

  # Check the server's hosting provider
#   try:
#       w = whois.whois(server)
#       is_hosting_provider = w.registrar is not None
#   except Exception as e:
#       print(f"Unable to ascertain if server has a hosting provider: {e}")

  # Check the server's nameservers
    try:
        dns_records = socket.getaddrinfo(server, None)
        is_nameservers = len(dns_records) > 0
    except Exception as e:
        print(f"Unable to ascertain if server has nameservers:\n {e}\n\n")

    # Check the server's web server
    try:
        response = requests.get(f'https://{server}')
        server_header = response.headers.get('Server')
        is_web_server = server_header is not None
    except Exception as e:
        print(f"Unable to ascertain if server has a web server:\n {e}\n\n")

    # Check the server's DNS provider
    try:
        dns_records = socket.getaddrinfo(server, None)
        dns_provider = dns_records[0][2]
        is_dns_provider = dns_provider is not None
    except Exception as e:
        print(f"Unable to ascertain if server has a DNS provider:\n {e}\n\n")

    # Check the server's HTTP response headers
    try:
        response = requests.get(f'https://{server}')
        headers = response.headers
    except Exception as e:
        print(f"Unable to ascertain server's HTTP response headers:\n {e}\n\n")
        headers = None

    # Check the server's IP reputation
    try:
        # This requires a third-party service like VirusTotal
        print(f"IP address of server: {ip_address}")
    except Exception as e:
        print(f"Unable to ascertain server's IP reputation: {e}")

    return is_ssl_certificate,+'\n'+is_aes_encryption,+'\n'+is_accessible,+'\n'+is_connected,+'\n'+is_hosting_provider,+'\n'+is_nameservers,+'\n'+is_web_server,+'\n'+is_dns_provider,+'\n'+headers,+'\n'+ssl_certificate_details

    
options = {
     "1: Get Proxies" : get_proxies,
     "2: Get Network Information" : get_network_info,
     "3: Change IP Address" : change_ip,
     "4: Change MAC Address" : change_mac,
     "5: Get GeoInfo from IP Address" : get_geo_info,
     '6: Check Encrypted Traffic' : check_encryption,
     '7: Check Website / Server' : check_connectivity,
     '8: Reset DNS and IP Address' : reset_dns,
     '9: DNS Changer' : change_DNS,
     '10: Static IP - SubnetMask - Gateway Setter' : static_ip_getter,
     "11: Terminate the program" : quit
}



def menu(options):
    print('''
.------------------.
| Choose an option |
'------------------'
          ''')
    for key, value in options.items():
        print(f"{key}")


   
def main():
    print('''
    ==+===+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==+===
    ==+===+++++++++++++++++++╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗++++++++++++++++==+===
    ==+===+++++++++++++++++++║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝++++++++++++++++==+===
    ==+===+++++++++++++++++++║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ ++++++++++++++++==+===
    ==+===+++++++++++++++++++║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ ++++++++++++++++==+===
    ==+===+++++++++++++++++++║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗++++++++++++++++==+===
    ==+===+++++++++++++++lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝++++++++++++++++==+===
    ==+===++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=++++++++++++++++++++==+===
    ''')

    print('PREDATOR AI TOKEN')
   
   

    while True:
        menu(options)
        choice = input( ''' 
 .-------------------. 
(| enter your choice |) (1/8):
 '-------------------'         ... ? ''')

        # if choice in options:
        #     options[choice]()
        
        if choice == "1":
            proxies = get_proxies()
            print(f"\nProxies:\n{proxies}\n")
        elif choice == "2":
            network_info = get_network_info()
            print(network_info)
        elif choice == "3":
            new_ip = change_ip()
            print(new_ip)
        elif choice == "4":
            new_mac = change_mac()
            print(new_mac)
        elif choice == "5":
            geo_info = get_geo_info()
            print(geo_info)
        elif choice == "6":
            encrypted_website = asyncio.run(check_encryption())
            print(encrypted_website)
        elif choice == "7":
            get_connectivity = asyncio.run(check_connectivity())
            print(get_connectivity)
        elif choice == "8":
            reset_dns()
            print('DNS Reset')
        elif choice == "9":
            change_DNS()
            print('Check your network configuration')
        elif choice == "10":
            static_ip_getter()
            print('Check your network configuration to see if the effects have taken place.')
        elif choice.lower() == '11' :
            print('''
==+===+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==+===
==+===+++++++++++++++++++╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗++++++++++++++++==+===
==+===+++++++++++++++++++║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝++++++++++++++++==+===
==+===+++++++++++++++++++║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ ++++++++++++++++==+===
==+===+++++++++++++++++++║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ ++++++++++++++++==+===
==+===+++++++++++++++++++║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗++++++++++++++++==+===
==+===+++++++++++++++lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝++++++++++++++++==+===
==+===++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=++++++++++++++++++++==+===
            ''')
            quit()
            sys.exit(0)
        else:
            print('''
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
            print('''
                                                   
                                  ,-----------------------------------o
                                 (_    Terminating the programme..._   /~" 
                                   
                                   
                                   
     ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
 lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    
                  ''')
            exit()
            sys.exit(0)
            break
        else:
            print('''
                      
                     _____________ 
                    |  _________  |
                    | | Loading | |
                    | |_________| |
                    |_____________|
                    
                    
                    
                    
     ▒█▀▄▒█▀▄▒██▀░█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄░░▒▄▀▄░█
 lil ░█▀▒░█▀▄░█▄▄▒█▄▀░█▀█░▒█▒░▀▄▀░█▀▄▒░░█▀█░█
    
                  ''')           
main()
if __name__ == "__main__":
    app.run(debug=True)