import subprocess
from xml.etree.ElementInclude import include				# Subprocess library
from modules.classes import Asset							# Import Asset class
def hostTool(asset):
	host_dict = {}
	found_ipv4 = []
	found_mail = []
	found_ipv6 = []
	found_nameserver = []
	zonetransfer_results = []
	zonetransfer_dict = {}
	debug_list = []
	error_count = 0
	uri = ''
	ttl = ''
	inc = ''
	axfr = '' 
	result = ''

	try:
		try:
			# Run the host command through subprocess
			host_cmd = subprocess.Popen(('host {}'.format(asset.host_uri)),shell=True,
										stdout=subprocess.PIPE)
			# loop through each address of the scope
			for line in host_cmd.stdout:
				line = line.decode('utf-8').strip("\n")
				# Grab IP from line, store in var ip
				if "has address" in line:
					*_, ip = line.split(' ')
					found_ipv4.append(ip)
				# Grab mail from line, store in var mail
				elif "mail is" in line:
					*_, mail = line.split(' ')
					found_mail.append(mail)
				# Grab IPv6 from line, store in var ipv6
				elif "IPv6" in line:
					*_, ipv6 = line.split(' ')
					found_ipv6.append(ipv6)
				
				host_dict = {"IPv4": found_ipv4,"Mail":found_mail,"IPv6":found_ipv6}
		except TypeError as e:
			print(e)
		except Exception as e:
			print("This went wrong: {}".format(e))

		try:
			# Run host command for nameserver information
			host_cmd = subprocess.Popen(('host -t ns {}'
										.format(asset.host_uri)),shell=True,
										stdout=subprocess.PIPE)
			for line in host_cmd.stdout:
				line = line.decode('utf-8').strip("\n")
				# Grab name server from line, store in var nameserver
				if "name server" in line:
					*_, nameserver = line.split(" ")
					found_nameserver.append(nameserver)
				
		except TypeError as e:
			print(e)
		except Exception as e:
			print("This went wrong: {}".format(e))
		
		host_dict = {"IPv4": found_ipv4,"Mail":found_mail,"IPv6":found_ipv6,"NameServer": found_nameserver}
		asset.add_host_findings(host_dict)

		# This is where the DNS Zonetransfer happens
		try:
			# Boolean to start grabbing useful dns info from host cmd
			gatherIntel = False
			for ns in found_nameserver:
				# Run host command for dns zone transfer information
				host_cmd = subprocess.Popen(('host -t axfr {} {}'.format
											(asset.host_uri,ns)),shell=True,
											stdout=subprocess.PIPE)
				for line in host_cmd.stdout:
					line = line.decode('utf-8').strip("\n")
					if "ANSWER SECTION" in line:
						# Start capturing results for data dict
						gatherIntel = True
						continue
					if gatherIntel:
						zonetransfer_results = line.rsplit("\t", 1)
						debug_list.append(zonetransfer_results)
						# Stop capturing results for data dict
						if len(line) < 2:
							gatherIntel = False
		except TypeError as e:
			print(e)
		except Exception as e:
			print("This went wrong: {}".format(e))

		#  The list with fetched results from the DNS Zonestransfer ANSWERS 
		#  section
		for line in debug_list:
			try: 
				# If line is not empty, move on to process through split
				if len(line[0]) >= 2 and len(line[1]) >= 2:
					if "\t" in line[0]:
						try:
							# Split line[0] into 4 on \t
							uri, ttl, inc, axfr = line[0].split("\t")
						except Exception as e:
							# Add one error if it goes wrong to print out at the
							# end.
							error_count += 0
						try:
							# Split line[0] first into 2 parts then split on \t
							first, second = line[0].split(" ")
							uri = first
							ttl, inc, axfr = second.split("\t")
						except Exception as e:
							# Add one error if it goes wrong to print out at the
							# end.
							error_count += 0
					# If line has no \t, split on space once to process
					elif "\t" not in line[0]:
						first, second = line[0].split(" ", 1)
						uri = first
						ttl, inc, axfr = second.split(" ")
					result = line[1]
					
					zonetransfer_dict = {"URI": uri, "TTL":ttl,"IN":inc,"AXFR":axfr,"Result":result}
					asset.add_host_zonetransfer_results(zonetransfer_dict)

			except Exception as e: 
				# Throw an exception when the splitting goes wrong.
				pass
		
	except TypeError as e:
		print("Something went wrong while running the scan, please refer to: {}"
			.format(e))
	except Exception as e:
			print("This went wrong: {}".format(e))