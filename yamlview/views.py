from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = make()
    context = {
        'data': data,
    }
    return render(request, "yamlview/index.html", context)

def make():
    data = {
        'network': {
            'header': [
                "Network",
                "MTU",
                "VLAN",
                "CIDR",
                "Ranges",
                "DNS"
            ],
            'body': [
                {
                    'name': "oob",
                    'body': [
                        {
                            'value': "1500"
                        },
                        {
                            'value': ""
                        },
                        {
                            'value': "10.23.104.0/24"
                        },
                        {
                            'table': "true",
                            'value': {
                                'header': [
                                    "type",
                                    "start",
                                    "end"
                                ],
                                'body': [
                                    "static",
                                    "10.23.104.11",
                                    "10.23.104.21"
                                ]
                            }
                        },
                        {
                            'value': ""
                        }
                    ]
                },
                {
                    'name': "pxe",
                    'body': [
                        {
                            'value': "1500"
                        },
                        {
                            'value': "none"
                        },
                        {
                            'value': "10.23.104.0/24"
                        },
                        {
                            'table': "true",
                            'value': {
                                'header': [
                                    "type",
                                    "start",
                                    "end"
                                ],
                                'body': [
                                    "static",
                                    "10.23.104.11",
                                    "10.23.104.21"
                                ]
                            }
                        },
                        {
                            'value': "none"
                        }
                    ]
                }
            ]
        }
    }

    return data

