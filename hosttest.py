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


# #* Define and refine address list, removing what we don't need
# new_scope = []      #* var for appended scope
# old_scope = []      #* var for old scope to see changes
# for line in args.filename:
#     old_scope.append(line.strip('\n'))
#     #* remove the https://www from the scope if found
#     if line.startswith("https://www"):
#         new_url = line[12:]
#         new_url.strip('\n')
#     #* remove the https:// from the scope if found        
#     elif line.startswith("https://"):
#         new_url = line[8:]
#         new_url.strip('\n')
#     #* remove the http://www from the scope if found
#     elif line.startswith("http://www"):
#         new_url = line[11:]
#         new_url.strip('\n')
#     #* remove the http:// from the scope if found
#     elif line.startswith("http://"):
#         new_url = line[7:]
#         new_url.strip('\n')
#     #* remove the www from the scope if found
#     elif line.startswith("www"):
#         new_url = line[4:]
#         new_url.strip('\n')
#     #* if none of the above is found, write current scope to var new_url
#     else:
#         new_url = line
#     new_scope.append(new_url.strip('\n'))


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

#// host [domain]
#// host -t ns [domain]
#// add zonetransfer 

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
