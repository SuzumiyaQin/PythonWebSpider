import re
import os
import time
import datetime
import requests

localtime=time.strftime('%Y%m%d',time.localtime(time.time()))#获取系统时间(即今日时间)

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer':'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
}

def input_date():
    begin_date = input("Please input the begin_date, like (20180125) :")
    end_date = input("Please input the end_date, like (20180325) :")
    if int(end_date) > int(localtime) or int(begin_date) > int(end_date):
        print("输入错误")
        return input_date()
    else:
        return begin_date,end_date

def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date,"%Y%m%d")
    end_date = datetime.datetime.strptime(end_date,"%Y%m%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days = 1)
    return date_list

begin_date,end_date = input_date()
dates = getEveryDay(begin_date, end_date)
name = input('文件夹名称: ')
curpath=os.getcwd() #得到当前目录地址
targetpath = curpath + os.path.sep + name

if not os.path.exists(targetpath):
    os.makedirs(targetpath)
    print('文件夹创建完成！')
else:
    print('文件已存在')
os.chdir(targetpath)

for date in dates:
    if date == localtime:
        url = 'https://www.pixiv.net/ranking.php?mode=daily'
    else:
        url = 'https://www.pixiv.net/ranking.php?mode=daily&date=' + str(date)
    page = requests.get(url,headers=headers).text
    pic_path = re.compile(r'data-filter="thumbnail-filter lazy-image"data-src="(.+?.jpg)"')
    urlList = pic_path.findall(page)
    top = urlList[0]
    topper = top.replace("c/240x480/", "")
    print(topper)
    path = re.search(r'.*?/(\d{8})_p0_master1200.jpg',topper).group(1) + '.jpg'
    r = requests.get(topper,headers=headers)
    with open(path,'wb')as f:
        f.write(r.content)
        print('ok')
print('任务完成')

