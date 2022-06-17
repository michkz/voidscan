import subprocess


def nmapTool(asset):
    scan_results = {}
    try:
        nmap_cmd = subprocess.Popen(('nmap {}'.format(asset.nmap_uri)),
                                    shell=True, stdout=subprocess.PIPE)
        for line in nmap_cmd.stdout:
            line = line.decode('utf-8').strip("\n")
            # Save the open port and service to variables
            if "open" in line:
                org_line = line
                ip_port, *_ = line.split(' ')
                *_, ip_serv = org_line.split(' ')
                # Save the results to scan_results
                scan_results = {"Port": ip_port.strip("\n"),
                                "Service": ip_serv.strip("\n")}
                # Add the scan_results to the asset results
                asset.add_nmap_findings(scan_results)
    except TypeError as e:
        print("[!] The following TypeError occurred: {}".format(e))
    except Exception as e:
        print("[!] The following went wrong: {}".format(e))
