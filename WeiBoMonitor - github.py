#!/usr/bin/python3
# -*- coding: utf8 -*-

import smtplib
import re
import requests
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from lxml import etree


monitor_url = "https://weibo.cn/u/1678105910"  # 监控微博Host 孙俪URL
headers = {

    "Host": "weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Cookie": "***"  # 将your cookie替换成自己的cookie
    
        }

def mail_163():
    msg_from = '***' #填写163邮箱账号
    passward = '***' #注：填写邮箱授权码，不是密码
    msg_to = '***' #填写需要推送到的邮箱，不建议使用qq邮箱
    subject = wei_bo(headers, monitor_url)[0]+'已更新'
    content = wei_bo(headers, monitor_url)[1]
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP('smtp.163.com', 25)
        s.login(msg_from, passward)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print('发送成功,已邮件推送')
    except smtplib.SMTPException as e:
        print('发送失败' + format(e))
    finally:
        s.quit()

def wei_bo(headers, monitor_usr):
    girl_url = monitor_usr
    r_url = requests.get(girl_url, headers=headers)
    title = re.findall(r'<title>(.*?)</title>',r_url.text,re.S)[0] #获取微博ID
    newest = re.findall(r'<span class="ctt">(.*?)</span>',r_url.text)[1] #获取最新的一条微博
    soup = BeautifulSoup(r_url.text, "html.parser")
    first = soup.find_all('div', attrs={"id": True})[0]
    id = first.get('id')
    return (title,newest,id)


if __name__ == "__main__":
    with open("new_id.txt", "r+") as f:
        old_id = f.read()
        new_id = wei_bo(headers, monitor_url)[2]
    if new_id != old_id:
        #mail_163()
        weibo_picture(headers,monitor_url)
        print('有更新')
        print(wei_bo(headers, monitor_url)[0]) #打印微博ID
        print(wei_bo(headers, monitor_url)[1]) #打印最新微博
        """
        更新
        """
        with open("new_id.txt", "w+") as f:
            f.write(new_id)
    else:
        print(wei_bo(headers, monitor_url)[0] + '无更新')
        exit()







