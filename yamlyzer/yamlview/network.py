# the list that will be returned when filter is done
d = []

# The load_all returns a generator that is a stream of dictionaries
# so it needs to be converted into a list
def networkinfo(loaded):
    data = list(loaded)
    # To find the yaml doc that contains network information
    # look for schema: drydock/Network/v1
    gooddoc = []   
    keys = ["name","mtu","vlan","vidr","ranges","dns"]
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
                empty_dict[k]=gooddoc[x]["data"][k]
            except KeyError:
                empty_dict[k] = ""
        d.append(empty_dict)  
    return d
        
