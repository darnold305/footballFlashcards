########### Python 2.7 #############
import httplib, urllib, base64

playerArray = []

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f3d646fb0e7d4d3ab88810cd9a487b68',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.fantasydata.net')
    conn.request("GET", "https://api.fantasydata.net/nfl/v2/JSON/Players" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f3d646fb0e7d4d3ab88810cd9a487b68',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.fantasydata.net')
    conn.request("GET", "https://api.fantasydata.net/nfl/v2/JSON/Players" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    playerArray = data
    print(playerArray)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################