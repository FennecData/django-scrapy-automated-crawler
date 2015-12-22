import os
import time
import threading
import simplejson
from subprocess import call

from django.http import HttpResponse
from django.views.generic import View

class ParseUrls(View):
    def post(self,request,spidername):
        try:
            os.remove(self.scrapdir()+"/results/"+spidername+'.json')
        except OSError:
            pass
        
        f = open(self.scrapdir()+"/running/"+spidername+'.json', 'w')
        simplejson.dump({
            "urls" : request.POST.get("urls"),
            "xpath" : request.POST.get("xpath"),
            "clean" : request.POST.get("clean"),
        },f)
        f.close()
        
        t = threading.Thread(target=self.background_process, kwargs={'spidername':spidername})
        t.setDaemon(True)
        t.start()
        
        return HttpResponse(t.name)
    
    def background_process(self,spidername):
        call([
            "scrapy crawl "+spidername+
            " -o scrapping/results/"+spidername+".json "+
            "--loglevel INFO "+
            "--logfile=scrapping/logs/"+spidername+'_'+time.strftime("%Y%m%d-%H%M%S")+".log"
        ],shell=True,cwd=os.path.dirname(self.scrapdir()))
        
    def scrapdir(self):
        return os.path.dirname(os.path.realpath(__file__))