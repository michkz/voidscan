import subprocess                   #* subprocess library
import argparse                     #* argparse library
import re                           #* regex library
from modules import validateScope   #* custom scope validation script

#* Define file argument
parser = argparse.ArgumentParser(
    description="This program gives IP information about the scope")
parser.add_argument('filename',
help="Give the scope.txt to the program", 
type=argparse.FileType('r'))
args = parser.parse_args()

#* additional vars for within program
scope = []              #* var for the scope
subnet_scope = []       #* var for when subnet is found in scope

#* validate the given scope and make sure it's right for the program
#todo create validation for different types of subnets
for line in args.filename:
    if "/24" in line:
        ip, subnet = line.split('/')
        validateScope.validate_ip_address_subnet(ip, subnet, subnet_scope)
    elif validateScope.validate_ip_address(line):
        scope.append(line.strip('\n'))
print(subnet_scope)

#* check if subnets were found in scope
if subnet_scope:
    open_ports = []         #* var for found open ports
    open_services = []      #* var for found services
    #* simple check to determine the text for 1 or more subnets
    if len(subnet_scope) <= 1:
        print(len(subnet_scope),"subnet has been found, commencing scan now")
    else:
        print(len(subnet_scope),"subnets have been found, commencing scan now")
    #* loop through all subnets that were found in scope
    for address in subnet_scope:
        print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Now scanning subnet {}".format(address))
        nmap_cmd = subprocess.Popen(('nmap {}'.format(address)), shell=True, stdout=subprocess.PIPE)
        for line in nmap_cmd.stdout:
            line = line.decode('utf-8').strip("\n")
            # print(line)
            #- find a way to show results per scanned host when scanning a 
            #- subnet instead of showing all at the end of the scan. Currently
            #- it prints the host found at the end
            if "report for" in line:
                print("|")
                *_, host = line.split(' ')
                print("| Results for host {}".format(host))
            if "open" in line:
                org_line = line
                ip_prot, *_ = line.split(' ')
                *_, ip_serv = org_line.split(' ')
                open_ports.append(ip_prot)
                open_services.append(ip_serv)
                if ip_prot and ip_serv:
                    print("|- Port {} was found with {} service running behind it.".format(ip_prot,ip_serv))
            elif "ignored" in line: print("|- No open ports found")
    print("⌊________________⌋")

#* check if addresses were found in scope
if scope:
    open_ports = []         #* var for found open ports
    open_services = []      #* var for found services
    if len(scope) <= 1:
        print(len(scope),"address has been found, commencing scan now")
    else:
        print(len(scope),"addresses have been found, commencing scan now")
    for address in scope:
        print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Results for {}".format(address))
        nmap_cmd = subprocess.Popen(('nmap {}'.format(address)), shell=True, stdout=subprocess.PIPE)
        # Write to terminal
        for line in nmap_cmd.stdout:
            line = line.decode('utf-8').strip("\n")
            if "open" in line:
                ip_prot, *_ = line.split(' ')
                open_ports.append(ip_prot)
            if "open" in line:
                *_, ip_serv = line.split(' ')
                open_services.append(ip_serv)
        
        #* check if open ports were found and continue to show those
        if open_ports:
            print("| The following open ports were found")
            for port, service in zip(open_ports, open_services):
                print("|- Port {} was found with {} service running behind it.".format(port,service))
        #* if no open ports were found, it will say it has found none
        else:
            print("| No open ports found")
        print("⌊________________⌋")
