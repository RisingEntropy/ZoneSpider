# ZoneSpider

空间说说爬虫，爬点赞人员并统计点赞次数，评论次数，id，名字

因为空间不把点赞人数显示完，所以只能算是半成品

使用QT5.14 进行界面编写，由于使用了`QWebEngineView`,windows 下编译请使用MSVC2017 或者 MSVC2015 ，不要使用MinGW

# 依赖

request 2.23.0

demjson 2.24

lxml 4.5.0

xlutils 2.0.0

python >=3.5

QT>=5

# 使用方法

请把安装好所有依赖的的Python放于同一目录下。或者更改源代码MainWindow中MainWindow::on_pushButton_2_clicked()函数相关内容

# 开发博客

[day0](https://www.cnblogs.com/BeyondStars/p/12380913.html)

[day1](https://www.cnblogs.com/BeyondStars/p/12386857.html)

[day2](https://www.cnblogs.com/BeyondStars/p/12392049.html)