from .hosts import Hosts
from .networks import Networks

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
        # self.software = Software.render(docs)

        # Temp hardcoded data
        self.software = [{
            "chart":"contenttest",
            "timeout": "content",
            "labels":"othercontent",
            "name": "name", "seq":
            "true",
            "order":""
            }, {
            "chart":"contenttest2",
            "timeout": "content2",
            "labels":"othercontent2",
            "name": "name2", "seq":
            "false", "order":""
        }]


        return {"uploaded_file_url": self.filename, "network": self.network, "hosts": self.hosts, "software": self.software}
