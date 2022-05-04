import re

def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        return False
    
    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False
    
    print("IP address {} is valid".format(address))
    return True
