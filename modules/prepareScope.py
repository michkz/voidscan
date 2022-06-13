from modules.old_validateScope import validateScopeAddresses    ## Custom validation
from modules.classes import Asset

## Function to prepare the scope for the different tools within the program
def prepareScopeForTool(assets):
    tool_list = ["host", "curl", "nmap"]           ## List of tools in program
    scope_list = []                                ## Creation of var scope_list
    hostAssets, curlAssets, nmapAssets = [],[],[]  ## Creation of scope per tool

    ## Save scope to new var scope_list
    for line in assets:
        scope_list.append(line)


    ## Assign the right assets to the right tools
    for tool in tool_list:
        current_tool = tool
        if current_tool == "host":
            for line in scope_list:
                main_asset = line.main_asset.strip("\n")
                hostAssets = validateScopeAddresses(tool, main_asset,
                                                     hostAssets)
                print("hostassets:{}\ncurrent line: {}\n".format(hostAssets, line))
        elif current_tool == "curl":
            for line in scope_list:
                line = line.main_asset.strip("\n")
                curlAssets = validateScopeAddresses(tool, line,
                                                     curlAssets)
        elif current_tool == "nmap":
            for line in scope_list:
                line = line.main_asset.strip("\n")
                nmapAssets = validateScopeAddresses(tool, line,
                                                     nmapAssets)

    return hostAssets, curlAssets, nmapAssets

def create_original_asset_list(original_scope):
    # add og scope to main_asset property from class
    # figure out how to add validated to same asset
    # validate the main_asset and change to liking 
    scope_list_of_objects = []
    for asset in original_scope:
        asset.strip("\n")
        a = Asset(asset)
        a.add_customer_contact("Bedrijf X","+31 6 13243546")
        scope_list_of_objects.append(a)
    # return list of objects
    return scope_list_of_objects