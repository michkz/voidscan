from commands.host import hostTool                        # Command to run host
from commands.curl import curlTool                        # Command to run curl
from commands.nmap import nmapTool                        # Command to run nmap
from modules.classes import Template
from modules.prepareScope import create_original_asset_list
from modules.validateScope import validateScopeObjects
import argparse


logo = """
     ▌ ▐·      ▪  ·▄▄▄▄  .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄
    ▪█·█▌▪     ██ ██▪ ██ ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
    ▐█▐█• ▄█▀▄ ▐█·▐█· ▐█▌▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
     ███ ▐█▌.▐▌▐█▌██. ██ ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
    . ▀   ▀█▄▀▪▀▀▀▀▀▀▀▀•  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪
                                    v0.0.1
"""


def main():
    print(logo)
    # Argparse code that reads the input file
    parser = argparse.ArgumentParser(
                        description="""
                         This is a reconnaissance program that gathers useful
                         information about the given scope
                         """)

    parser.add_argument('-f', '--filename',
                        help="""Provide the program with a scope. example
                        main.py -f [file.txt]""", type=argparse.FileType('r'))
    args = parser.parse_args()
    complete_scope = []
    complete_scope = create_original_asset_list(args.filename)
    print("[*] Validating scope...")
    try:
        validated_scope = []
        # Validate the given scope
        validated_scope = validateScopeObjects(complete_scope)
    except Exception as e:
        print("[!] Something went wrong during the validation, aborting. {}"
              .format(e))
    print("[*] Scope successfully validated.")
    for asset in validated_scope:
        if asset.host_uri:
            try:
                # Run the host_uri of the current main_asset through Host
                print("[*] Executing host tool for: {}".format(asset.host_uri))
                hostTool(asset)
            except Exception as e:
                print("[!] Something went wrong during the host scan")
            print("[*] Host tool completed")
        if asset.curl_uri:
            try:
                # Run the curl_uri of the current main_asset through Curl
                print("[*] Executing curl tool for: {}".format(asset.curl_uri))
                curlTool(asset)
            except Exception as e:
                print("[!] Something went wrong during the curl scan")
            print("[*] Curl tool completed")
        if asset.nmap_uri:
            try:
                print("[*] Executing nmap tool for: {}".format(asset.nmap_uri))
                nmapTool(asset)
            except Exception as e:
                print("[!] Something went wrong during the nmap scan")
            print("[*] Nmap tool completed")
    print("[*] Creating report...")
    template_out = Template('PentestReport.jinja').render(validated_scope)
    with open('PentestReport.md', 'w') as output:
        output.write(template_out)
    print("[*] Report created successfully")


if __name__ == '__main__':
    main()
