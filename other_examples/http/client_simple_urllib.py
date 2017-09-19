import urllib.request

with urllib.request.urlopen('http://localhost:8081/') as response:
    html = response.read()
    print(html)
