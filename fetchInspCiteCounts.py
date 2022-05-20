#!/usr/bin/env python3

import json, urllib.request

url = ("https://inspirehep.net/api/literature?size=1000&sort=mostrecent&q="
       "a%20L.C.Stein.2%20and%20-collaboration%3A%22LIGO%20Scientific%22%20"
       "and%20-collaboration%3AVIRGO%20and%20-collaboration%3ALISA")

data = json.loads(urllib.request.urlopen(url).read())

for hit in data['hits']['hits']:
    texkey = hit['metadata']['texkeys'][0]
    try:
        eprint = hit['metadata']['arxiv_eprints'][0]['value']
    except:
        eprint = '?'
    print(f"{texkey} ({eprint}): {hit['metadata']['citation_count']}")
