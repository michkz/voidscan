from unicodedata import name
from jinja2 import FileSystemLoader
from jinja2 import Environment


class Asset():
    def __init__(self, main_asset):
        self.main_asset = main_asset
        self.host_uri = ''
        self.curl_uri = ''
        self.nmap_uri = ''
        self.ip = None
        self.hostname = None
        self.tool = None
        self.customer_name = ''
        self.customer_phone = ''
        self.host_results = []
        self.host_zonetransfer_results = []
        self.curl_results = []
        self.nmap_results = []

    def set_ip(self, ip):
        self.ip = ip
    
    def get_ip(self):
        return self.ip

    def set_hostname(self, hostname):
        self.hostname = hostname
    
    def get_hostname(self):
        return self.hostname

    def add_customer_contact(self, name, phone):
        self.customer_name = name
        self.customer_phone = phone

    def has_host_uri(self, uri):
        self.host_uri = uri

    def has_curl_uri(self, uri):
        self.curl_uri = uri

    def has_nmap_uri(self, uri):
        self.nmap_uri = uri

    # Must be a dictionary
    def add_host_findings(self, findings):
        self.host_results.append(findings)

    def add_host_zonetransfer_results(self, findings):
        self.host_zonetransfer_results.append(findings)

    def add_curl_findings(self, findings):
        self.curl_results.append(findings)

    def add_nmap_findings(self, findings):
        self.nmap_results.append(findings)


class Customer():
    def __init__(self, name):
        self.name = name
        self.address = ''
        self.phonenumber = ''

    def add_customer_contact(self, address, phone):
        self.address = address
        self.phonenumber = phone


class Template:

    def __init__(self, filename):
        # templates will be loaded from templates directory
        self.file_loader = FileSystemLoader('./app/templates')
        self.env = Environment(loader=self.file_loader)
        self.filename = filename

    def render(self, data):
        return self.env.get_template(self.filename).render(data=data)

    def show_output(self, data):
        print(self.render(data))
