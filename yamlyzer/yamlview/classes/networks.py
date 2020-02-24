class Networks:

    def render(data):
        # To find the yaml doc that contains network information
        # look for schema: drydock/Network/v1
        gooddoc = []
        d = []
        keys = ["mtu","vlan","cidr","ranges","dns"]
        for dic in data:
            for(key,value) in dic.items():
                #  "schema": "drydock/Network/v1"
                if key == 'schema' and value == 'drydock/Network/v1' :
                    gooddoc.append(dic)

        for x in range(len(gooddoc)):
            empty_dict = dict.fromkeys(keys)
            empty_dict["name"]=gooddoc[x]["metadata"]["name"]
            for k in keys:
                try:
                    # Reform the servers for formatting
                    if k == "dns":
                        temp = gooddoc[x]["data"][k]
                        temp["servers"] = gooddoc[x]["data"][k]["servers"].split(",")
                        empty_dict[k] = temp
                    else:
                        empty_dict[k] = gooddoc[x]["data"][k]
                except KeyError:
                    empty_dict[k] = ""
                    if k == "ranges":
                        empty_dict[k] = []
            d.append(empty_dict)

        return d