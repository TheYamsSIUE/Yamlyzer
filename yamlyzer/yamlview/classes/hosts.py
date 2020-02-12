class Hosts:

    def render(yaml):
        docs = list(yaml)
        matches = []
        hosts = []
        keys = [ "addressing", "host_profile" ]

        for doc in docs:
            for (k, v) in doc.items():
                if k == "schema" and v == "drydock/BaremetalNode/v1":
                    matches.append(doc)

        for match in matches:
            host = dict.fromkeys(keys)
            host["name"] = match["metadata"]["name"]
            for k in keys:
                host[k] = match["data"][k]

            hosts.append(host)

        return hosts
