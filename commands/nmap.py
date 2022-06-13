import socket
import subprocess
import threading
from modules.classes import Asset


def nmapTool(asset):


    scan_results = {}
    # Creation of the data dictionary to save results to.
    
    try:
        nmap_cmd = subprocess.Popen(('nmap {}'.format(asset.nmap_uri)), shell=True, stdout=subprocess.PIPE)
        for line in nmap_cmd.stdout:
            line = line.decode('utf-8').strip("\n")
            if "report for" in line:
                *_, host = line.split(' ')

            if "open" in line:
                org_line = line
                ip_port, *_ = line.split(' ')
                *_, ip_serv = org_line.split(' ')
                scan_results = {"Port":ip_port.strip("\n"),"Service":ip_serv.strip("\n")}
                asset.add_nmap_findings(scan_results)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("This went wrong: {}".format(e))