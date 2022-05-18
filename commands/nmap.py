import subprocess                   ## subprocess library
import argparse                     ## argparse library
import re                           ## regex library
from modules import validateScope   ## custom scope validation script

#TODO - validate if code is conform PEP8
#TODO - check if all requirements are in code

def nmapCommand(assets):
    current_tool = "nmap"           ## Define tool name for validation
    scope = []                      ## Creation of var scope

    ## validate the given scope and make sure it's right for the program
    for line in assets.filename:
        scope = validateScope.validateScopeAddresses(current_tool,
                                                     line.strip("\n"), scope)
    print(scope)

    open_ports = []                 ## Creation of var for found open ports
    open_services = []              ## Creation of var for found services

    ## run nmap scan for every asset in var scope
    try:
        for host in scope:
            print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Results for {}".format(host))
            nmap_cmd = subprocess.Popen(('nmap {}'.format(host)), shell=True,
                                         stdout=subprocess.PIPE)
            ## Write to terminal
            for line in nmap_cmd.stdout:
                line = line.decode('utf-8').strip("\n")

                ## Cut and store found open port to var open_ports
                if "open" in line:
                    ip_port, *_ = line.split(' ')
                    open_ports.append(ip_port)

                ## Cut and store found service to var open_services
                if "open" in line:
                    *_, ip_serv = line.split(' ')
                    open_services.append(ip_serv)
            
            ## Check if open ports were found and continue to show those
            if open_ports:
                print("| The following open ports were found")
                for port, service in zip(open_ports, open_services):
                    print("""|- Port {} was found with {} service running behind
                     it.""".format(port,service))
            print("⌊________________⌋")
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))
