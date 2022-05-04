import subprocess                            #* subprocess library
import argparse                              #* argparse library
from modules import validateScope            #* custom scope validation script

#* Define file argument
parser = argparse.ArgumentParser(
    description="This program gives IP information about the scope")
parser.add_argument('filename',
help="Give a file to the program to scan", 
type=argparse.FileType('r'))
#> test argument to do all asked prompts
parser.add_argument('-y','--yes-to-all',action="store_true", 
help="Yes to all prompts")
args = parser.parse_args()


#* validate scope and keep only those that curl can use
scope = []
for line in args.filename:
    scope = validateScope.validateScopeAddresses("curl",line.strip("\n"), scope)

#* loop through the scope and print the results that are found for "curl -I"

for host in scope:
    print("\n⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉ %s" % host)
    new_location = ""
    moved_host = ""
    curl_cmd = subprocess.Popen("curl -I {}".format(host), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    for line in curl_cmd.stdout:
        line = line.decode('utf-8').strip("\n\r")
        #* show if host has moved and the new location
        if line.startswith("Location:") or line.startswith("location:"):
            *_, new_location = line.split(" ")
            moved_host = host
        if len(line) > 0:
            print("|",line)
    #* if a new host is found, show at the end of the results
    if moved_host and new_location:
        print("\n[!] I noticed that: %s has been moved and found:\n|- %s" % (moved_host, new_location))
        user_answer = input("Would you like to scan this one too? [Y/n]\n> ")
        if user_answer.startswith("y"):
            print("Now scanning %s" % new_location)
            curl_cmd = subprocess.Popen("curl -I {}".format(new_location), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            for line in curl_cmd.stdout:
                line = line.decode('utf-8').strip("\n\r")
                if len(line) > 0:
                    print("|-",line)

    print("⌊________________")

    


