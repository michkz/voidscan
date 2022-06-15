import re                                        ## Regex library
from modules.classes import Asset                ## Import Asset class

def validateIPAddress(address):
    ## define what a valid IP should match to
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    ## return false if IP does not match
    if bool(match) is False:
        # print("IP address {} is not valid".format(address))
        return False
    
    ## check if IP meets requirements of what it should look like
    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            # print("IP address {} is not valid".format(address))
            return False

    ## show if IP is valid
    # print("IP address {} is valid".format(address))
    return True

#TODO add nmap_uri to hostname because it can scan too but is not allowed
def validateScopeObjects(list_of_objects):
    # Check if the scope matches one of these to filter out IP addresses.
    ipAddressFilter = '0', '1', '2', '3', '4', '5', '6', '7', '8','9'
    uriStartFilter = 'http', 'https', '//'
    for object in list_of_objects:
        # remove the https://www from the input_file if found
        if object.main_asset.startswith("https://www"):
            modified_asset = object.main_asset[12:].strip("\n")
            object.used_tool("host")
            object.has_hostname(modified_asset)
            object.has_host_uri(modified_asset)
        # remove the https:// from the input_file if found        
        elif object.main_asset.startswith("https://"):
            modified_asset = object.main_asset[8:].strip("\n")
            object.used_tool("host")
            object.has_hostname(modified_asset)
            object.has_host_uri(modified_asset)
        ## remove the http://www from the input_file if found
        elif object.main_asset.startswith("http://www"):
            modified_asset = object.main_asset[11:].strip("\n")
            object.used_tool("host")
            object.has_hostname(modified_asset)
            object.has_host_uri(modified_asset)
        ## remove the http:// from the input_file if found
        elif object.main_asset.startswith("http://"):
            modified_asset = object.main_asset[7:].strip("\n")
            object.used_tool("host")
            object.has_hostname(modified_asset)
            object.has_host_uri(modified_asset)
        ## remove the www from the input_file if found
        elif object.main_asset.startswith("www"):
            modified_asset = object.main_asset[4:].strip("\n")
            object.used_tool("host")
            object.has_hostname(modified_asset)
            object.has_host_uri(modified_asset)
        ## make sure IP addresses won't be added to modified_scope
        elif object.main_asset.startswith(ipAddressFilter):
            pass
        ## if none of the above is found, write input_file to modified_scope
        elif len(object.main_asset) > 1:
            if not object.main_asset.startswith(uriStartFilter):
                if "." in object.main_asset:
                    modified_asset = object.main_asset.strip("\n")
                    object.used_tool("host")
                    object.has_hostname(modified_asset)
                    object.has_host_uri(modified_asset)
        else:
            print("{} is invalid".format(object.main_asset))

        if object.main_asset.startswith("https://"):
            modified_asset = object.main_asset.strip("\n")
            object.used_tool("curl")
            object.has_hostname(modified_asset)
            object.has_curl_uri(modified_asset)
        ## check if input_file starts with http://
        elif object.main_asset.startswith("http://"):
            modified_asset = object.main_asset.strip("\n")
            object.used_tool("curl")
            object.has_hostname(modified_asset)
            object.has_curl_uri(modified_asset)
        
        if validateIPAddress(object.main_asset):
            modified_asset = object.main_asset.strip("\n")
            object.used_tool("nmap")
            object.has_IP(modified_asset)
            object.has_nmap_uri(modified_asset)

    return list_of_objects