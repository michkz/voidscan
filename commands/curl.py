import subprocess                                   # subprocess library

def curlTool(asset):
    # Command to eliminate duplicate code and fire off the curl command.
    def curlCommand(asset):
        curl_cmd = subprocess.Popen("curl -I {}".format(asset),
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        return curl_cmd.stdout

    # Creating the data dictionary with the fields needed for the report.
    curl_result = {}
    hsts = 'Niet gevonden'
    x_frame_options = 'Niet gevonden'
    x_xxs_protection = 'Niet gevonden'

    try:
        new_location = ""							# Variable for location
        moved_host = ""								# Variable for current host

        for line in curlCommand(asset.curl_uri):
            line = line.decode('utf-8').strip("\n\r")
            # show if host has moved and the new location
            if (line.startswith("Location:") or line.startswith("location:")):
                *_, new_location = line.split(" ")
                moved_host = asset.hostname
        # if a new host is found, scan new location
        if moved_host and new_location:
            for line in curlCommand(new_location):
                line = line.decode('utf-8').strip("\n\r")
                if len(line) > 0:
                    # Grab information if found in line
                    #TODO - grab HOST header and CSP header. omit xssheader
                    if "x-frame-options" in line:
                      *_, x_frame_options = line.split(" ", 1)
                    if "x-xss-protection" in line:
                        *_, x_xxs_protection = line.split(" ", 1)
                    if "strict-transport-security" in line:
                        *_, hsts = line.split(" ", 1)

            
            curl_result = {"Location":new_location,"HSTS":hsts,"XFrameOptions":x_frame_options,"XSSProtection":x_xxs_protection}
        else:
            print("Skipping, no assets found")
        asset.add_curl_findings(curl_result)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))
