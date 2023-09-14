import requests,time
url = 'http://anketa.rosminzdrav.ru/home/justank/111/86/10872?v=3#'
headers = {'Host':'anketa.rosminzdrav.ru','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3','Accept-Encoding':'gzip, deflate','Referer':'http://anketa.rosminzdrav.ru/home/justank/111/86/10872?v=3','Content-Type':'application/x-www-form-urlencoded','Content-Length':'328','Connection':'keep-alive','Cookie':'_ym_uid=15341683771018578715;_ym_d=1534168378;_ym_isad=1','Upgrade-Insecure-Requests':'1','Pragma':'no-cache','Cache-Control':'no-cache'}
data = 'FormTypeId=111&SubjectId=86&mo_id=10872&questions1=4&questions25=30&questions31=31&questions33=34&questions38=38&questions44=44&questions46=46&questions48=48&questions50=51&questions52=52&questions54=54&questions56=56&questions66=67&questions85=86&questions114=114&questions116=116&questions118=118&questions120=120&UserReviews.Message=&UserReviews.Status=0'
for i in range(50):
	res = requests.post(url, data=data, headers=headers)
	print (res.text)
	time.sleep(1)