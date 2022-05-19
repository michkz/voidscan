from modules.validateScope import validateScopeAddresses    ## Custom validation

## Function to prepare the scope for the different tools within the program
def prepareScopeForTool(assets):
    tool_list = ["host", "curl", "nmap"]           ## List of tools in program
    scope_list = []                                ## Creation of var scope_list
    hostAssets, curlAssets, nmapAssets = [],[],[]  ## Creation of scope per tool

    ## Save scope to new var scope_list
    for line in assets:
        scope_list.append(line.strip("\n"))

    ## Assign the right assets to the right tools
    for tool in tool_list:
        current_tool = tool
        if current_tool == "host":
            for line in scope_list:
                hostAssets = validateScopeAddresses(tool, line.strip("\n"),
                                                     hostAssets)
        elif current_tool == "curl":
            for line in scope_list:
                curlAssets = validateScopeAddresses(tool, line.strip("\n"),
                                                     curlAssets)
        elif current_tool == "nmap":
            for line in scope_list:
                nmapAssets = validateScopeAddresses(tool, line.strip("\n"),
                                                     nmapAssets)

    return hostAssets, curlAssets, nmapAssets