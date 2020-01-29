from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Tabs
    network = [{
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

    hosts = [{
        "name": "cab23-r720-12",
        "profile": "cp_r270-primary",
        "addresses": [{
            "network": "oob",
            "ip": "20.23.104.12"
        }, {
            "network": "pxe",
            "ip": "20.23.20.12"
        }, {
            "network": "oam",
            "ip": "20.23.21.12"
        }, {
            "network": "storage",
            "ip": "20.23.23.12"
        }]
    }, {
        "name": "cab23-r720-13",
        "profile": "cp_r270",
        "addresses": [{
            "network": "oob",
            "ip": "21.23.104.12"
        }, {
            "network": "pxe",
            "ip": "21.23.20.12"
        }, {
            "network": "oam",
            "ip": "21.23.21.12"
        }, {
            "network": "storage",
            "ip": "21.23.23.12"
        }]
    }]

    software = [{
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
    
    # Combine all tabs data here
    context = {"network": network, "hosts": hosts, "software": software}
    return render(request, "yamlview/index.html", context)
