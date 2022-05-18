import re                                   #* regex library
from modules import validateIPAddress       #* custom module to validate IP

def validate_ip_address(address):
    #* define what a valid IP should match to
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    #* return false if IP does not match
    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        return False
    
    #* check if IP meets requirements of what it should look like
    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False

    #* show if IP is valid
    print("IP address {} is valid".format(address))
    return True

    
#* A function to validate the scope from the given textfile 
def validateScopeAddresses(tool, input_file, modified_scope):
    #* check if scope matches one of these to filter out IP addresses
    ipAddressFilter = '0', '1', '2', '3', '4', '5', '6', '7', '8','9'
    
    if tool == "host":
        #* remove the https://www from the input_file if found
        if input_file.startswith("https://www"):
            modified_scope.append(input_file[12:])
        #* remove the https:// from the input_file if found        
        elif input_file.startswith("https://"):
            modified_scope.append(input_file[8:])
        #* remove the http://www from the input_file if found
        elif input_file.startswith("http://www"):
            modified_scope.append(input_file[11:])
        #* remove the http:// from the input_file if found
        elif input_file.startswith("http://"):
            modified_scope.append(input_file[7:])
        #* remove the www from the input_file if found
        elif input_file.startswith("www"):
            modified_scope.append(input_file[4:])
        #* make sure IP addresses won't be added to modified_scope
        elif input_file.startswith(ipAddressFilter):
            pass
        #* if none of the above is found, write input_file to modified_scope
        elif len(input_file) > 1:
            if "." in input_file:
                modified_scope.append(input_file)
        return modified_scope

    elif tool == "curl":
        #* check if input_file starts with https://
        if input_file.startswith("https://"):
            modified_scope.append(input_file)
        #* check if input_file starts with http://
        elif input_file.startswith("http://"):
            modified_scope.append(input_file)
        return modified_scope

    elif tool == "nmap":
        #* validate the input_file to see if it is a valid IP
        if validate_ip_address(input_file):
            modified_scope.append(input_file)
        return modified_scope