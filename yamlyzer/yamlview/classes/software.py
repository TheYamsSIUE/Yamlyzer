class Software:

    def render(docs):
        charts = []
        manifests = []
        chartGroups = []
        software = []
        fullsite = {}

        for doc in docs:
            for (k, v) in doc.items():
                if k == "schema" and v == "armada/Chart/v1":
                    charts.append(doc)
                if k == "schema" and v == "armada/Manifest/v1":
                    manifests.append(doc)
                if k == "schema" and v == "armada/ChartGroup/v1":
                    chartGroups.append(doc)

        # Get full-site manifest
        for manifest in manifests:
            if(manifest["metadata"]["name"] == "full-site"):
                fullsite = manifest
        
        

        for chart in charts:
            
            # get chart name
            chartName = chart["data"]["chart_name"]

            # Data wait timeout
            try:
                dataWaitTimeout = chart["data"]["wait"]["timeout"]
            except KeyError:
                dataWaitTimeout = ""

            # Data Wait Labels
            try:
                dataWaitLabels = chart["data"]["wait"]["labels"]["release_group"]
            except KeyError:
                dataWaitLabels = ""

            # Get Group name
            chartGroup = ""
            sequenced = ""
            for val in chartGroups:
                if chartName in val["data"]["chart_group"]:
                    chartGroup = val["metadata"]["name"]
                    try:
                        sequenced = val["data"]["sequenced"]
                    except KeyError:
                        sequenced = ""

            # Find order in manifest
            try:
                order = fullsite["data"]["chart_groups"].index(chartGroup)
            except ValueError:
                order = ""

            # Add data to new entry in
            software.append({
                "chart": chartName,
                "timeout": dataWaitTimeout,
                "labels": dataWaitLabels,
                "name": chartGroup, 
                "seq": sequenced,
                "order": order
            })


        return software