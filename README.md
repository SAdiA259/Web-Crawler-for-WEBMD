# Web-Crawler
Crawling WEBMD to create knowledge base of medicines with their side effects

TASK NO:01
crawl WebMD and make a knowledge base of medicines and their side effects.

Web crawling:
The general thought behind web scratching is to gather information that exists on a website, and change it into a format that is usable for examination.

OVERVIEW:
1.	Download the webMD page.
2.	Create a BeautifulSoup class to parse the page.
3.	Find the divs and the relative classes required.
4.	Split medicine name from the link.
5.	Get side-effects of every medicine.
6.	Print medicine names along with their side-effects in csv file.

PROCEDURE DETAILS:

1.	I am interested in finding the names of all drugs from ‘A-Z’ and I'd like to know what are the side effects of those drugs from “webmd.com”.  
2.	We begin by reading in the source code for WebMD and creating a Beautiful Soup object with the BeautifulSoup function. 
3.	Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF. Beautiful Soup is essentially a set of wrapper functions that make it simple to select common HTML elements.
4.	The soup object contains all of the HTML in the original document. we can use the find_all method, which will find all the instances of a tag on a page.
5.	 Classes and ids are used by CSS to determine which HTML elements to apply certain styles to. We can also use them when scraping to specify specific elements we want to scrape
6.	By looking at the source code, I found that all the links of the letters from “A-Z” , are in a single div element of class "drugs-browse-box", and that links for each individual letter is a member of “div” element of class "drugs-browse-subbox". I found that the the links of drugs are a member of “div” element of class “drug-list-container”.
7.	To find all the lists of drugs we have to iterate through all letters from “A-Z” and then to subletters.
8.	I have created a root link which is 'http://www.webmd.com'
9.	url path is the link of the WebMD containg drugs. This is our starting point to get all the names of drugs and their relative side effects.
10.	I noticed that while iterating through links from letters “A-z” to the subletters “aa-zz” , a special pattern is followed which is root link+ sub letter and then when iterating through sub letters to the name of drugs another pattern is followed which is root link +link attributes.
11.	I created a get_links function that takes the url and div class , reads the link, Beautiful soup selects the html elements and soup consist of html elements while links consist of all anchor tags in the html.
12.	Then I have used for loop to iterate through WebMD , starting from link http://www.webmd.com/drugs/2/index then i chose div class” drug-browse-box” to select all the letters from “A-Z”, then I chose div class “ drug-browse-subbox” to select all the sub letters inside letters, then finally I used div class “ drug-list-container” which consist of all the names of drugs inside sub letters.
13.	Link_url consist of the root link in addition with link attributes of that div class which is used to iterate through WebMD and its sub links.
14.	Link_url obtained after the last div class “drug list container” consist of the links of drugs. I have used split function here to split the “link_url” at this”/” and then I stored 6th index of link url in” drug_name” which is the “drug name”.
15.	Then I am using div class “side effects” to extract side effects of drugs, I have stored side effects in “name1”.
16.	I am creating a csv file named as “index file” and printing the name of drugs in first column and their side effects in the second column.
HURDLES:
•	While I was iterating through the links I found that some drug did not had any side effects so I received an error on “name1” that object has no attribute of text, I managed that error by adding try and except in the code. 

TASK # 02
crawl WebMD and make a knowledge base of medical conditions with their respective medicines.

OVERVIEW:
1.	Download the webMD page.
2.	Create a BeautifulSoup class to parse the page.
3.	Find the divs and the relative classes required.
4.	Get medical conditions name from the link.
5.	Get relative medicines of every Condition.
6.	Print Condition names along with their medicines in csv file.

PROCEDURE:
1.	I am interested in finding the names of all MEDICAL CONDITIONS from ‘A-Z’ and I'd like to know what are the relative medicines for every condition from “webmd.com”.  
2.	I begin by reading in the source code for WebMD and creating a Beautiful Soup object with the BeautifulSoup function. 
3.	Most of the code is similar to the first code as By looking at the source code, I found that all the links of the letters from “A-Z” , are in the same div element of class "drugs-browse-box", and as there are no sub letters , I have not used  “div” element of class "drugs-browse-subbox". I found that the the links of conditions are the member of “div” element of class “drug-list-container”. The only difference was that the name of drugs inside every condition were in a “table” of class” drugs-treatments-table” 
4.	To find all the lists of conditions we have to iterate through all letters from “A-Z” and then to the conditions.
5.	I have created a root link which is 'http://www.webmd.com'
6.	url path is the link of the WebMD containg conditions. This is our starting point to get all the names of conditions and their relative drugs.
7.	I noticed that while iterating through links from letters “A-z” to the conditions , a special pattern is followed which is root link+ link attributes of conditions.
8.	I created a get_links function that takes the url and div class , reads the link, Beautiful soup selects the html elements and soup consist of html elements while links consist of all anchor tags in the html.
9.	Then I have used for loop to iterate through WebMD , starting from link http://www.webmd.com/drugs/2/conditions/index then i chose div class” drug-browse-box” to select all the letters from “A-Z”, then I chose div class “ drug-list-container” which consist of all the names of conditions inside sub letters and then I finally chose table class” drugs-treatment-table” to get all the relative drugs
10.	Link_url consist of the root link in addition with link attributes of that div class which is used to iterate through WebMD and its sub links.
11.	Link_url obtained after the last div class “drug list container” consist of the links of conditions. I have used split function here to split the “link_url” at this”/” and then I stored 6th index of link url in” cond_name” which is the “condition name”.
12.	Inside table “drugs-treatments-table” I have used “findAll(“td”), where “td” is the columns of the table. Then I have used for loop to find all the “a” tags inside td and finally I stored the text of those a tags in name1
13.	I am creating a csv file named as “index file1” and printing the name of conditions in first column and their drugs in the second column.


