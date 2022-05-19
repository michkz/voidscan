import subprocess
# define variable
addr = []
addr.append("nu.nl")
addr.append("nos.nl")
print(addr)

# loop through addr var
for line in addr:
    host_cmd = subprocess.Popen(('host -t ns {}'.format(line)), shell=True, stdout=subprocess.PIPE)

    for line in host_cmd.stdout:
        line = line.decode('utf-8').strip("\n")
        print(line)
        