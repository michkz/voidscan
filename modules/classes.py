class Asset():
    def __init__(self, uri):
        self.uri = uri
        self.ip = None
        self.hostname = None
        self.results = []
        self.vulnerabilities = []

    def has_IP(self, ip):
        self.ip = ip
    
    def has_hostname(self, hostname):
        self.hostname = hostname

    ## Must be a dictionary
    def add_findings(self, finding):
        self.results.append(finding)

    def get_results(self):
        return self.results
    
    def __str__(self):
        return "Uri: {}\nIP: {}\nHostname: {}\nResults: {}".format(self.uri,self.ip, self.hostname, self.results)

class Customer():
    def __init__(self, name):
        self.name = name
        self.address = ''
        self.phonenumber = ''

#TODO - Create the scanner class to start scans from
class Scanner():
    def __init__(self, uri):
        self.uri = uri
        self.type = ''
        self.host = None                #TODO - start host from scanner class
        self.curl = None                #TODO - start curl from scanner class
        self.nmap = None                #TODO - start nmap from scanner class
    
# data = {}
# data['Customer'] = 'Customer One'
# data['Assets'] = []

# input_text = ['192.168.1.109', 'localhost']
# asset_list = []

# for line in input_text:
#     asset = Asset(line)
#     asset.has_IP(line)
#     asset_list.append(asset)

# for asset in asset_list:
#     data['Assets'].append(asset)

# for entry in data['Assets']:
#     print(entry.uri, entry.results)


