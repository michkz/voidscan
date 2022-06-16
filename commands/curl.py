import subprocess            # subprocess library


def curlTool(asset):
    # Function to eliminate duplicate code and fire off the curl command.
    def curlCommand(asset):
        curl_cmd = subprocess.Popen("curl -I {}".format(asset),
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        return curl_cmd.stdout

    # Creating the result dictionary with the fields needed for the report.
    curl_result = {}
    hsts = 'Niet gevonden'
    x_frame_options = 'Niet gevonden'
    x_xxs_protection = 'Niet gevonden'
    new_location = ""							# Variable for location
    moved_host = ""								# Variable for current uri

    try:

        for line in curlCommand(asset.curl_uri):
            line = line.decode('utf-8').strip("\n\r")
            # Save new location to var if found
            if (line.startswith("Location:") or line.startswith("location:")):
                *_, new_location = line.split(" ")
                moved_host = asset.hostname
        # If a new location is found, scan new location
        if moved_host and new_location:
            for line in curlCommand(new_location):
                line = line.decode('utf-8').strip("\n\r")
                if len(line) > 0:
                    # Grab x-frame-options if found in line
                    if "x-frame-options" in line:
                        *_, x_frame_options = line.split(" ", 1)
                    # Grab x-xss-protection if found in line
                    if "x-xss-protection" in line:
                        *_, x_xxs_protection = line.split(" ", 1)
                    # Grab strict-transport-security if found in line
                    if "strict-transport-security" in line:
                        *_, hsts = line.split(" ", 1)
        else:
            print("[!] No new location found")
        # Save found results to dictionary
        curl_result = {"Location": new_location, "HSTS": hsts,
                       "XFrameOptions": x_frame_options,
                       "XSSProtection": x_xxs_protection}
        # Add dictionary with results to asset
        asset.add_curl_findings(curl_result)
    except TypeError as e:
        print("[!] The following TypeError occurred: {}".format(e))
    except Exception as e:
        print("[!] This went wrong during the scan: {}".format(e))
