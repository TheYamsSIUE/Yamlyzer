class Site:

    def render(docs):
        matches = []

        for doc in docs:
            for (k, v) in doc.items():
                if k == "schema" and v == "pegleg/SiteDefinition/v1":
                    return dict.fromkeys(["name"], doc["metadata"]["name"])
