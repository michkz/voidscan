import subprocess                                         ## subprocess library

def hostCommand(assets):
    try:
        if assets:
            for hostname in assets:
                try:
                    ## Run the host command through subprocess
                    host_cmd = subprocess.Popen(('host {}'.format(hostname)),
                                                shell=True,stdout=subprocess.
                                                                    PIPE)
                    ## loop through each address of the scope
                    print("\nResults found for",hostname)
                    for line in host_cmd.stdout:
                        line = line.decode('utf-8').strip("\n")
                        ## Grab IP from line, store in var ip
                        if "has address" in line:
                            *_, ip = line.split(' ')
                            print("| Address found:", ip)
                        ## Grab mail from line, store in var mail
                        elif "mail is" in line:
                            *_, mail = line.split(' ')
                            print("| Mail handled by:", mail)
                        ## Grab IPv6 from line, store in var ipv6
                        elif "IPv6" in line:
                            *_, ipv6 = line.split(' ')
                            print("| IPv6 address:", ipv6)
                except TypeError as e:
                    print(e)
                except Exception as e:
                    print("This went wrong: {}".format(e))
            
                try:
                    ## Run host command for nameserver information
                    host_cmd = subprocess.Popen(('host -t ns {}'
                                                .format(hostname)),shell=True,
                                                stdout=subprocess.PIPE)
                    print("\nThe following name servers have been found:")
                    for line in host_cmd.stdout:
                        line = line.decode('utf-8').strip("\n")
                        ## Grab name server from line, store in var nameserver
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
                                                .format(hostname, nameserver)),
                                                shell=True, stdout=subprocess.
                                                                    PIPE)
                    print("""\nThe following DNS zone transfer information has 
                            been found:""")
                    for line in host_cmd.stdout:
                        line = line.decode('utf-8').strip("\n")
                        print("|=",line)
                except TypeError as e:
                    print(e)
                except Exception as e:
                    print("This went wrong: {}".format(e))    
        else:
            print("Skipping, no assets found")

    except TypeError as e:
        print("Something went wrong while running the scan, please refer to: {}"
        .format(e))
    except Exception as e:
                print("This went wrong: {}".format(e))
