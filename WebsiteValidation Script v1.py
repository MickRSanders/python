import httplib
conn = httplib.HTTPConnection("https://scientel.sentrich.com")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print (r1.status, r1.reason)
