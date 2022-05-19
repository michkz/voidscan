
# TODO create option to remove path from URL if opted into / doesn't work if IP
#+ has domain
# for line in scope:
#     trimpos = line.find("/")
#     if trimpos > -1:
#         new_url = line[:trimpos]
#         print(line,"has been changed to: ",new_url)
#     else:
#         print("nothing found")
#     scope.append(new_url.strip("\n"))
# print(scope)



# TODO create option to validate subnets and parse them for nmap
# def validate_ip_address_subnet(ip, subnet, scope):
#     if validate_ip_address(ip):
#         address = ip+"/"+subnet
#         if "/" in address:
#             scope.append(address.strip("\n"))
#     return scope
#> Continues in nmap.py
# subnet_scope = []       #* var for when subnet is found in scope
# for line in assets.filename:
#         if "/24" in line:
#             ip, subnet = line.split('/')
#             validateScope.validate_ip_address_subnet(ip, subnet, subnet_scope)

## check if subnets were found in scope
#     if subnet_scope:
#         open_ports = []         #* var for found open ports
#         open_services = []      #* var for found services
#         #* simple check to determine the text for 1 or more subnets
#         if len(subnet_scope) <= 1:
#             print(len(subnet_scope),"subnet has been found, commencing scan now")
#         else:
#             print(len(subnet_scope),"subnets have been found, commencing scan now")
#         #* loop through all subnets that were found in scope
#         for address in subnet_scope:
#             print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ Now scanning subnet {}".format(address))
#             nmap_cmd = subprocess.Popen(('nmap {}'.format(address)), shell=True, stdout=subprocess.PIPE)
#             for line in nmap_cmd.stdout:
#                 line = line.decode('utf-8').strip("\n")
#                 # print(line)
#                 #- find a way to show results per scanned host when scanning a 
#                 #- subnet instead of showing all at the end of the scan. Currently
#                 #- it prints the host found at the end
#                 if "report for" in line:
#                     print("|")
#                     *_, host = line.split(' ')
#                     print("| Results for host {}".format(host))
#                 if "open" in line:
#                     org_line = line
#                     ip_prot, *_ = line.split(' ')
#                     *_, ip_serv = org_line.split(' ')
#                     open_ports.append(ip_prot)
#                     open_services.append(ip_serv)
#                     if ip_prot and ip_serv:
#                         print("|- Port {} was found with {} service running behind it.".format(ip_prot,ip_serv))
#                 elif "ignored" in line: print("|- No open ports found")
#         print("⌊________________⌋")