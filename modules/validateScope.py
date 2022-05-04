import re
from modules import validateIPAddress

def validateScopeAddresses(tool, scope, current_list):
    if tool == "host":
        #* remove the https://www from the scope if found
        if scope.startswith("https://www"):
            current_list.append(scope[12:])
        #* remove the https:// from the scope if found        
        elif scope.startswith("https://"):
            current_list.append(scope[8:])
        #* remove the http://www from the scope if found
        elif scope.startswith("http://www"):
            current_list.append(scope[11:])
        #* remove the http:// from the scope if found
        elif scope.startswith("http://"):
            current_list.append(scope[7:])
        #* remove the www from the scope if found
        elif scope.startswith("www"):
            current_list.append(scope[4:])
        #* if none of the above is found, write current scope to var current_list
        elif len(scope) > 1:
            if "." in scope:
                current_list.append(scope)
        return current_list

    
    elif tool == "curl":
        if scope.startswith("https://"):
            current_list.append(scope)
        elif scope.startswith("http://"):
            current_list.append(scope)
        return current_list
    # elif tool == "nmap":
    #     for line in scope:
    #         return validateIPAddress(line)


def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        return False
    
    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False

    #> psuedo code
    #> if right end has 2 numbers after / then add to var to scan whole subnet

    print("IP address {} is valid".format(address))
    return True

def validate_ip_address_subnet(ip, subnet, scope):
    if validate_ip_address(ip):
        address = ip+"/"+subnet
        if "/" in address:
            scope.append(address.strip("\n"))
    return scope