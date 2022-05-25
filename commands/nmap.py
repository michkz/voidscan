from socketserver import TCPServer
import subprocess                   ## subprocess library

import socket
import threading
from modules.classes import Asset

from black import out

def nmapCommand(assets):
    open_ports = []                 ## Creation of var for found open ports
    open_services = []              ## Creation of var for found services

    def TCP_connect(ip, port_number, delay, output):
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(delay)
        try:
            TCPsock.connect((ip, port_number))
            output[port_number] = 'Listening'
        except:
            output[port_number] = ''

    def scan_ports(host_ip, delay):
        threads = []
        output = {}
        open_ports = []
        
        amount = 10000
        ## Spawn threads to scan ports
        for i in range(amount):
            t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, 
                                output))
            threads.append(t)

        ## Start threads
        for i in range(amount):
            threads[i].start()
            
        ## Lock the main thread until all threads are completed
        for i in range(amount):
            threads[i].join()
        
        ## Print listening ports from small to large
        for i in range(amount):
            if output[i] == 'Listening':
                open_ports.append(i)

        return open_ports
    try:
        for host in assets:
            data = {}
            data['Tool'] = "nmap"
            data["Asset"] = []
            data["OpenPortsFound"] = []
            a = Asset(host)
            a.has_IP(host)
            data['Asset'].append(host)


            data['OpenPortsFound'].append(scan_ports(host, 1))
            a.add_findings(data)
            print(a,"\n")
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))


    # try:
    #     if assets:
    #         for host in assets:
    #             print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Results for {}".format(host))
    #             ## run nmap scan for every asset in var scope
    #             nmap_cmd = subprocess.Popen(('nmap {}'.format(host)), 
    #                                         shell=True, stdout=subprocess.PIPE)
                                            
    #             for line in nmap_cmd.stdout:
    #                 line = line.decode('utf-8').strip("\n")
    #                 ## Cut and store found open port to var open_ports
    #                 if "open" in line:
    #                     ip_port, *_ = line.split(' ')
    #                     open_ports.append(ip_port)
    #                 ## Cut and store found service to var open_services
    #                 if "open" in line:
    #                     *_, ip_serv = line.split(' ')
    #                     open_services.append(ip_serv)
                
    #             ## Check if open ports were found and continue to show those
    #             if open_ports:
    #                 print("| The following open ports were found")
    #                 for port, service in zip(open_ports, open_services):
    #                     print("""|- Port {} was found with {} service running 
    #                              behind it.""".format(port,service))
    #             print("⌊________________⌋")
    #     else:
    #         print("Skipping, no assets found")
    # except TypeError as e:
    #     print(e)
    # except Exception as e:
    #     print("This went wrong: {}".format(e))