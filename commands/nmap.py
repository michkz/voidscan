import subprocess                   ## subprocess library

def nmapCommand(assets):
    current_tool = "nmap"           ## Define tool name for validation
    open_ports = []                 ## Creation of var for found open ports
    open_services = []              ## Creation of var for found services

    try:
        if assets:
            for host in assets:
                print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Results for {}".format(host))
                ## run nmap scan for every asset in var scope
                nmap_cmd = subprocess.Popen(('nmap {}'.format(host)), 
                                            shell=True, stdout=subprocess.PIPE)
                                            
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
                        print("""|- Port {} was found with {} service running 
                                 behind it.""".format(port,service))
                print("⌊________________⌋")
        else:
            print("Skipping, no assets found")
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))