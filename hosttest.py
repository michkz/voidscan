import subprocess   #* subprocess library
import argparse
from sys import stderr     #* argparse library
from modules import validateScope #* custom scope validation script

#* Define file argument
parser = argparse.ArgumentParser(
    description="This program gives IP information about the scope")
parser.add_argument('-f', '--filename',
help="Give the scope.txt to the program", 
type=argparse.FileType('r'))
args = parser.parse_args()

#* validate scope and keep only those that host can use
scope = []
original_scope = []
for line in args.filename:
    if len(line) > 1:
        original_scope.append(line.strip("\n"))
        scope = validateScope.validateScopeAddresses("host",line.strip("\n"), scope)

#* show user what changes were made

print("The following changes have been made:")
for old, new in zip(original_scope, scope):
    if old != new:
        print("-",old,"is now",new)

#* start host command with given scope
try:
 for host in scope:
    try:
        host_cmd = subprocess.Popen(('host {}'.format(host)), shell=True, stdout=subprocess.PIPE)
        # loop through each address of the scope
        print("\nResults found for",host)
        for line in host_cmd.stdout:
            line = line.decode('utf-8').strip("\n")
            if "has address" in line:
                *_, ip = line.split(' ')
                print("| Address found:", ip)
            elif "mail is" in line:
                *_, mail = line.split(' ')
                print("| Mail handled by:", mail)
            elif "IPv6" in line:
                *_, ipv6 = line.split(' ')
                print("| IPv6 address:", ipv6)
    except:
        print("Something went wrong while running the scan, please refer to")

    # host_cmd = subprocess.Popen(('host -t ns {}'.format(host)), shell=True, stdout=subprocess.PIPE)
    # print("\nThe following name servers have been found:")
    # for line in host_cmd.stdout:
    #     line = line.decode('utf-8').strip("\n")
    #     if "name server" in line:
    #         *_, nameserver = line.split(" ")
    #         print("|- Nameserver: {}".format(nameserver))
    
    # host_cmd = subprocess.Popen(('host -t axfr {} {}'.format(host, nameserver)), shell=True, stdout=subprocess.PIPE)
    # print("\nThe following DNS zone transfer information has been found:")
    # for line in host_cmd.stdout:
    #     line = line.decode('utf-8').strip("\n")
    #     print("|=",line)



except host_cmd.stderr as e:
    print("Something went wrong while running the scan, please refer to: {}".format(e))
