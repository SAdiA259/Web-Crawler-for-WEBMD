
import csv
import re
import os
from urllib2 import urlopen
from bs4 import BeautifulSoup
import lxml

def get_links(div_class, url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html,"lxml")
    links = bsObj.find("div", {"class":div_class}).findAll("a")
    return links

def get_data(div_class, url):
    html=urlopen(url)
    bsobj=BeautifulSoup(html,"lxml")
    links=bsobj.find("div", {"class":div_class})
    name1=links.text
    print name1
    return links

root_web = 'http://www.webmd.com'
urlpath = 'http://www.webmd.com/drugs/2/index'


for link in get_links("drugs-browse-box", urlpath):
    if 'href' in link.attrs:
        link_url = root_web + link.attrs['href']
        if "offmarket" in link_url:
            print "ignored"
        else:
            print link_url
            for link in get_links("drugs-browse-subbox", link_url):
                if 'href' in link.attrs:
                    link_url = root_web + link.attrs['href']
                    print link_url
                    drug = ''
                    for link in get_links("drug-list-container",link_url):
                        if 'href' in link.attrs:
                            link_url = root_web + link.attrs['href']
                            print link_url
                            y=link_url.split('/',7)
                            for thing in y:
                                drug_name=y[6]
                                print drug_name
                                break
                            try:
                                html=urlopen(link_url)
                                bsobj=BeautifulSoup(html,"lxml")
                                links=bsobj.find("div", {"class":"side-effects"})        
                                name1=links.text
                                print name1     
                            except:
                                pass
                            with open('index.csv', 'a') as csv_file:
                                writer=csv.writer(csv_file)
                                writer.writerow([drug_name,name1])
    
