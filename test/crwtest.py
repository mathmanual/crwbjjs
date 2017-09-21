import urllib.request as ur
from bs4 import BeautifulSoup
import sys
import html

if __name__=='__main__':
    url0 = 'http://www.bjjs.gov.cn/eportal/ui?pageId=393547&systemId=2&categoryId=1&salePermitId=5957669&buildingId=477864'
    try:
        html0 = ur.urlopen(url0)
    except ur.URLError as e:
        print(e)
        sys.exit(0)
    except ur.HTTPError:
        print(ur.HTTPError)
        sys.exit(0)
    bsObj0 = BeautifulSoup(html0, 'lxml')
    namelist = bsObj0.findAll(id="3")
    print(namelist)