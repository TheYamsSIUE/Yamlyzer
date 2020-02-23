from .hosts import Hosts
from .networks import Networks
from .software import Software

class Parse:

    def __init__(self, filename, yamlDocs):
        self.filename = filename
        self.yamlDocs = yamlDocs
        self.network = []
        self.hosts = []
        self.software = []

    def getData(self):
        docs = list(self.yamlDocs)
        self.network = Networks.render(docs)
        self.hosts = Hosts.render(docs)
        self.software = Software.render(docs)

        # Sort networks by name
        self.network = sorted(self.network, key = lambda i: [i['name']])

        # Sort hosts by Node
        self.hosts = sorted(self.hosts, key = lambda i: [i['name']])

        # Sort software by Chart
        self.software = sorted(self.software, key = lambda i: [i['chart']])

        return {"uploaded_file_url": self.filename, "network": self.network, "hosts": self.hosts, "software": self.software}
