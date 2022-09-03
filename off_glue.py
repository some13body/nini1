import time
import concurrent.futures
import requests
import time
from bs4 import BeautifulSoup
fi = open('naw.txt','w')
f = 8000000
while f < 8010000:
    fi.write(str(f)+'\r')
    f += 1
fi.close()
out = []
CONNECTIONS = 5
tlds = open('naw.txt').read().splitlines()
urls = ['http://ninisite.com/discussion/topic/{}'.format(x) for x in tlds]
def load_url(url):
    try:
        ans = requests.get(url)
        if ans.status_code==200:
            ans = ans.text
            soup = BeautifulSoup(ans, "html.parser")
            res_top = soup.find("div",class_="col-xl-9 col-lg-8 col-md-12 pull-xs-none pull-md-right")
            test = res_top.find_all('p')
            f = 0
            fi = open('no.txt','a')
            li = []
            for i in test:
                fi.write(i.text+'\r')
            print(url+' done \r')
        elif ans.status_code==404:
            pass
        elif ans.status_code==500:
            print(url + 'server error \r')
            time.sleep(10)
        elif ans.status_code==403:
            print('u banned by server')
            time.sleep(10)
    except requests.exceptions.ConnectionError:
        sleep(10)
        pass
    except AttributeError:
        print('IDK what happend but it was '+ url+' \r')
executor = concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS)
future_to_url = (executor.submit(load_url, url) for url in urls)
time1 = time.time()
for i in concurrent.futures.as_completed(future_to_url):
        data = i.result()
        out.append(data)
        print(str(len(out)),end="\r")
time2 = time.time()
print(f'Took {time2-time1:.2f} s')
#parse
