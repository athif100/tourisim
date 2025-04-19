from django.urls import reverse
from django.contrib.sitemaps import Sitemap
class Web(Sitemap):
    priority=1 
    changefreq="weekly"
    def items ():
        return ["home","culture","signup","loginpage","logout","destinations","About"]   
    def location(self, obj):
        return reverse (obj) 
mysitemap={"web":Web}