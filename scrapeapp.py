from webscrape import webscrape
from urllib.parse import urlparse
from pushbullet import PushBullet

pb = PushBullet(api_key='')
pushString = ""



class Item():
    
    itemsList = []
    
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.website = domainLocator(url)
        self.xpath = xpathLocator(self.website)
        self.price = webscrape(url, self.xpath, self.website)
        self.__class__.itemsList.append(self)
def domainLocator(url):
    return urlparse(url).netloc

def xpathLocator(website):
    
    if website == "www.amazon.ae":
        xpath = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]'
        return xpath
    
    if website == "www.farfetch.com":
        xpath = ""
        return xpath
    
    
kindle = Item('Kindle', 'https://www.amazon.ae/dp/B09SWSX7FW?ref=MarsFS_ERDR_cav')
smartwatch = Item('watch', 'https://www.amazon.ae/accessoryME-Replacement-Compatible-Samsung-Silicone/dp/B08GFTWWL7/ref=pd_bxgy_img_sccl_1/258-3021939-5935567?pd_rd_w=y5gCy&content-id=amzn1.sym.fd8928ec-6f6a-4922-b310-600b659150f6&pf_rd_p=fd8928ec-6f6a-4922-b310-600b659150f6&pf_rd_r=Y56GP1K27BKA1282WKAD&pd_rd_wg=pTteu&pd_rd_r=04f5de36-c120-4756-8e28-33dedc2bdfa8&pd_rd_i=B08GFTWWL7&psc=1')




for i in Item.itemsList:
    pushString = pushString + i.name + ': ' + i.price + '\n'
    
push = pb.push_note('Prices', pushString)