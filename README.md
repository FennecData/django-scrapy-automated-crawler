# Django Scrapy - simple automated processing

Post any request to /{spider_name}/parse with a few parameters and get scrapy 
to automatically crawl and output the result and log in a simple file hierarchy

This example is meant to work with a simple spider which only retrieve a 
specific value on a webpage. It could easily be extended with a few fields 
but any extra effort should be put in a better task management and complete 
solutions like https://github.com/holgerd77/django-dynamic-scraper

# API
/simplespider/parse  POST parameters :
'''javascript
{
    urls : ["http://google.fr","http://yahoo.fr"]
    xpath : "//body/p[1]/text()"
}
'''

Three files will then be generated : 
* scrapping/logs/{spider_name}_{date}.log
* scrapping/results/{spider_name}.json
* scrapping/running/{spider_name}.json

The running/{spider_name}.json file will be deleted as soon as the crawl has ended. 
It contains all the post data sent, and is just used to transmit data between scripts
as well as being aware of the state of the crawling at any moment.