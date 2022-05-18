import subprocess                       ## subprocess library
from modules import validateScope       ## custom scope validation script

def hostCommand(assets):
    current_tool = "host"               ## Define tool name for validation
    scope = []                          ## Creation of var scope
    original_scope = []                 ## Creation of var original_scope


    ## Loop through the entries in the file and send them to validation
    for line in assets:
        if len(line) > 1:               ## Check if line has value or not
            original_scope.append(line.strip("\n"))
            scope = validateScope.validateScopeAddresses(current_tool, 
                                                        line.strip("\n"), scope)

    ## Show user what changes were made to the scope
    print("The following changes have been made:")
    for old, new in zip(original_scope, scope):
        if old != new:
            print("-",old,"is now",new)

    ## Start host command with given scope
    try:
        for host in scope:
            try:
                ## Run the host command through subprocess
                host_cmd = subprocess.Popen(('host {}'.format(host)),shell=True,
                                            stdout=subprocess.PIPE)
                ## loop through each address of the scope
                print("\nResults found for",host)
                for line in host_cmd.stdout:
                    line = line.decode('utf-8').strip("\n")
                    ## Grab IP from line and store in var ip
                    if "has address" in line:
                        *_, ip = line.split(' ')
                        print("| Address found:", ip)
                    ## Grab mail from line and store in var mail
                    elif "mail is" in line:
                        *_, mail = line.split(' ')
                        print("| Mail handled by:", mail)
                    ## Grab IPv6 from line and store in var ipv6
                    elif "IPv6" in line:
                        *_, ipv6 = line.split(' ')
                        print("| IPv6 address:", ipv6)
            except TypeError as e:
                print(e)
            except Exception as e:
                print("This went wrong: {}".format(e))
        
            try:
                ## Run host command for nameserver information
                host_cmd = subprocess.Popen(('host -t ns {}'.format(host)),
                                            shell=True, stdout=subprocess.PIPE)
                print("\nThe following name servers have been found:")
                for line in host_cmd.stdout:
                    line = line.decode('utf-8').strip("\n")
                    ## Grab name server from line and store in var nameserver
                    if "name server" in line:
                        *_, nameserver = line.split(" ")
                        print("|- Nameserver: {}".format(nameserver))
            except TypeError as e:
                print(e)
            except Exception as e:
                print("This went wrong: {}".format(e))

            try:        
                ## Run host command for dns zone transfer information
                host_cmd = subprocess.Popen(('host -t axfr {} {}'
                                            .format(host, nameserver)),
                                            shell=True, stdout=subprocess.PIPE)
                print("""\nThe following DNS zone transfer information has been 
                         found:""")
                for line in host_cmd.stdout:
                    line = line.decode('utf-8').strip("\n")
                    print("|=",line)
            except TypeError as e:
                print(e)
            except Exception as e:
                print("This went wrong: {}".format(e))    


    except TypeError as e:
        print("Something went wrong while running the scan, please refer to: {}"
        .format(e))
    except Exception as e:
                print("This went wrong: {}".format(e))
