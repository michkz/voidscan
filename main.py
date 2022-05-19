
from commands.host import hostCommand                 ## command to run host
from commands.curl import curlCommand                 ## command to run curl
from commands.nmap import nmapCommand                 ## command to run nmap
from modules.prepareScope import prepareScopeForTool  ## script to prepare scope

import subprocess                                     ## subprocess library
import argparse                                       ## argparse library


logo ="""
     ▌ ▐·      ▪  ·▄▄▄▄  .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
    ▪█·█▌▪     ██ ██▪ ██ ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
    ▐█▐█• ▄█▀▄ ▐█·▐█· ▐█▌▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
     ███ ▐█▌.▐▌▐█▌██. ██ ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
    . ▀   ▀█▄▀▪▀▀▀▀▀▀▀▀•  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪
                                    v0.0.1
"""

def main():
     #// - prepare scope
     #// - run tools: nmap, curl, host
     #TODO gather results
     #TODO sendToTemplate
     print(logo)

     ## Argparse code that reads the input file
     parser = argparse.ArgumentParser(
                         description="""
                         This is a reconnaissance program that gathers useful 
                         information about the given scope
                         """)
                         
     parser.add_argument('-f', '--filename',
                         help="""Provide the program with a scope. f.e. 
                         main.py -f [file.txt]""", 
                         type=argparse.FileType('r'))
                         
     args = parser.parse_args()

     hostAssets, curlAssets, nmapAssets = prepareScopeForTool(args.filename)


     ## Sending file contents to host command
     print("-=- Commencing host command -=-")
     hostCommand(hostAssets)
     print("-=- Now exiting host command -=-")

     ## Sending file contents to cURL command
     print("-=- Commencing cURL command -=-")
     curlCommand(curlAssets)
     print("-=- Now exiting cURL command -=-")

     #? - do not uncomment unless on own network due scanning
     # #* Sending file contents to nmap command
     print("-=- Commencing nmap command -=-")
     nmapCommand(nmapAssets)
     print("-=- Now exiting nmap command -=-")

     print("Job's done")

if __name__ == '__main__':
     main()

