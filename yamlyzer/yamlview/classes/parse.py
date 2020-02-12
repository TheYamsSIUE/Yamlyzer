from .hosts import Hosts

class Parse:

    def __init__(self, filename, yamlDocs):
        self.filename = filename
        self.yamlDocs = yamlDocs
        self.network = []
        self.hosts = []
        self.software = []

    def getData(self):
        # self.network = Network.render(yamlDocs)
        self.hosts = Hosts.render(self.yamlDocs)
        # self.software = Software.render(yamlDocs)

        # Temp hardcoded data
        self.network = [{
            "name": "oam",
            "MTU": "9100",
            "VLAN": "21",
            "CIDR": "10.23.21.0/24",
            "ranges": [{
                "type": "reserved",
                "start": "10.23.21.1",
                "end": "10.23.21.10"
            },
            {
                "type": "static",
                "start": "10.23.21.11",
                "end": "10.23.21.21"
            }],
            "dns": [{
                "domain": "atlantafoundry.com",
                "servers": ["8.8.8.8", "1.1.1.1", "8.8.4.4"]
            }]
        }, {
            "name": "pxe",
            "MTU": "5200",
            "VLAN": "",
            "CIDR": "10.23.21.2/24",
            "ranges": [],
            "dns": []
        }]

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
