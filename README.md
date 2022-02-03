# Webcheck SDK

This SDK injects monitoring capabilities to a web application.
It wraps GET calls from 'requests' API with a 'Monkey patching' function
and reports details from each of the GET calls to a server

##Usage example

Import the webcheck package in your file
```
import requests
import webcheck

res1 = requests.get('https://www.ynet.com')
res2 = requests.get('https://www.google.com')
res3 = requests.get('https://www.bing.com')
```

Now each one of the calls will be reported and stored