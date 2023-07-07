import requests
from bs4 import BeautifulSoup
def content_scrap(url=0,*kwargs):
    if url==0:
        val=content_scrap("https://www.wikihow.com/Make-Guacamole","div","class","headline_info")
        print(""" 
You havent given any args. so here's an exmaple
-----------------------------------------------

code :
-----------------------------------------------------------------------------------------------
content_scrap("https://www.wikihow.com/Make-Guacamole","div","class","headline_info")
-----------------------------------------------------------------------------------------------

Result : 
-----------------------------------------------------------------------------------------------

 """)
        print(repr(val))
        print("\n-----------------------------------------------------------------------------------------------\n")
        val=content_scrap("https://www.wikihow.com/Make-Guacamole","p")
        print(""" 
Another Example
-----------------------------------------------

code :
-----------------------------------------------------------------------------------------------
content_scrap("https://www.wikihow.com/Make-Guacamole","p")
-----------------------------------------------------------------------------------------------

Result : 
-----------------------------------------------------------------------------------------------

 """)
        print(repr(val))
        print("\n-----------------------------------------------------------------------------------------------\n")
        return 0
    Data=[]
    # url is the target we want to open
    
    #open with GET method
    resp=requests.get(url)
    
    
    
    #http_respone 200 means OK status
    if resp.status_code==200:
    
        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')	
    
        # l is the list which contains all the text i.e news
        if len(kwargs)==3:
            l=soup.find_all(kwargs[0],{kwargs[1]:kwargs[2]})
        else:
            l=soup.find_all(kwargs[0])
        for i in range(len(l)):
          Data.append((l[i].text))
        return Data
    else:
        return "Status code return : ",str(resp.status_code)
