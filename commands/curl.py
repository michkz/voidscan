import subprocess                           ## subprocess library

def curlCommand(assets):
    current_tool = "curl"                   ## Define tool name for validation
    
    ## loop through the scope and print the results that are found for "curl -I"
    try:
        if assets:
            for hostname in assets:
                print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ {}".format(hostname))
                new_location = ""
                moved_host = ""
                curl_cmd = subprocess.Popen("curl -I {}".format(hostname),
                                            shell=True,stdout = subprocess.PIPE,
                                            stderr = subprocess.PIPE)

                for line in curl_cmd.stdout:
                    line = line.decode('utf-8').strip("\n\r")
                    ## show if host has moved and the new location
                    if (line.startswith("Location:") or 
                        line.startswith("location:")):
                        *_, new_location = line.split(" ")
                        moved_host = hostname
                    if len(line) > 0:
                        print("|",line)
                ## if a new host is found, scan new location
                if moved_host and new_location:
                    print("""\n[!] I noticed that: {} has been moved and 
                    found:\n|- {}\n"""
                    .format(moved_host, new_location))
                    print("Now scanning {}".format(new_location))
                    curl_cmd = subprocess.Popen("curl -I {}".
                                        format(new_location),
                                        shell=True, stdout = subprocess.PIPE, 
                                        stderr = subprocess.PIPE)
                    for line in curl_cmd.stdout:
                        line = line.decode('utf-8').strip("\n\r")
                        if len(line) > 0:
                            print("|-",line)

                print("⌊________________")
        else:
            print("Skipping, no assets found")
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))
    


