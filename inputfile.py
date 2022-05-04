import subprocess

# Define command and options wanted
command = "cat"
options = ""
# Ask user for file name
filename = input("Please type in the name of the file you want to see: \n")
# Create list with arguments for subprocess.run
args=[]
args.append(command)
args.append(options)
for i in filename.split():
    args.append(i)
# Run subprocess.run and save output object
try:
    output = subprocess.run(args, capture_output=True)
    print('The following entries have been found')
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    # use decode function to convert to string
    for line in output:
        print('> ', line.stdout.decode('utf-8'))
except subprocess.CalledProcessError as error:
    print("Error code: ", error.returncode, '. Output: ', error.output.decode('utf-8'))