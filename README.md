# Celebrity_Vitalita
Uses Python Scraping libraries to get information from IMDB about celebrities born on a particular date.

IMDB provides a list of celebrities born on a particular date. Here is the IMDB link :  http://m.imdb.com/feature/bornondate.
The project implements to get the list of all celebrities born on a particular date, by using "Web Scraping" of Pyhton libraries.

The following information will be extracted from the webpage, and displayed on a website:

1. Name of the celebrity
2. Celebrity Image
3. Profession
4. Best Work 

Then we run a sentiment analysis on twitter for each celebrity and finally the output should be in the below format :

5. Name of the celebrity
6. Celebrity Image
7. Profession
8. Best Work
9. Overall Sentiment on Twitter: Positive, Negative or Neutral.

Tools Used -

1. Python 2.7 Tools and Packages Used. (A Python 3.6 version will be updated.)
2. Tweepy: An easy-to-use Python library for accessing the Twitter API.

3. Text Blob: Text Blob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

4. Beautiful Soup :  Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree using Python parsers like lxml and html5lib. Here we will be using the tree traversal method for parsing the scraped html tree.It automatically converts incoming documents to Unicode and outgoing documents to UTF-8.

5. Selenium : The web driver kit emulates a web-browser (I chose Chrome driver) and executes the JS scripts to load the dynamic content.
