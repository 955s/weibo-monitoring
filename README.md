# weibo-monitoring
用python脚本实现通过监控微博，一旦用户有更新就通过163邮箱推送微博内容
使用方法：
1:获取cookie
2：设置一个用来发送邮箱的账号，建议使用163邮箱，接收邮箱不推荐QQ邮箱，因为我这边测试多次后发现容易出现邮件发送邮件失败的情况。
3：把new_id.txt的路径写死，记得给权限不然无法把id写入此文件
4.使用crontab来定时执行脚本，我这边建议5分钟执行一次，