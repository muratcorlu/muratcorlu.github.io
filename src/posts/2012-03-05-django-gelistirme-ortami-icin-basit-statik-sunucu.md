title: Django geliştirme ortamı için basit statik sunucu
date: 2012-03-05 00:06
categoy: turkish
tags: django, python, server

[Django](http://www.djangoproject.com)'da web uygulamaları geliştirirken, geliştirme ortamında her seferinde beni en çok sıkıntıya sokan mevzu css ve js dosyaları gibi statik dosyaların sunulması işiydi. Böyle bir iş için bilgisayarıma http sunucusu kurmaktan ve bunu konfigüre etmekten hep kaçtım. Ancak bugün tam da aradığım basitlikte bir çözüme ulaştım. Python'un imdadımıza yetişen [SimpleHTTPServer modülü](http://docs.python.org/library/simplehttpserver.html) ile yazdığımız aşağıdaki tek satırlık komut, bulunduğum klasörü http üzerinden sunma imkanı veriyor:

    :::bash
    django-project/static$ > python -m SimpleHTTPServer $portnum

Django projemde, statik dosyalarımın bulunduğu klasörde yukarıdaki komutu $portnum yerine herhangi bir port numarası yazarak çalıştırıyorum. Django projemin settings.py dosyasında da aşağıdaki şekilde statik dosyalarımın yerini ve sunucu adresini bildiriyorum:

    :::python
    import os
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
    STATIC_URL = 'http://127.0.0.1:9876/'

Dilerseniz komutu django projesinin kök dizininde çalıştırarak birden fazla klasör için tek bir portu kullanabilirsiniz de:

    django-project$ > python -m SimpleHTTPServer 9876

    STATIC_URL = 'http://127.0.0.1:9876/static/'
    MEDIA_URL = 'http://127.0.0.1:9876/media/'

Sunucunun loglarını bir dosyaya yazarak arka planda çalıştırmayı dilerseniz, komutu aşağıdaki şekilde de çalıştırabilirsiniz:

    :::bash
    django-project/static$ > python -m SimpleHTTPServer $portnum > ~/temp/static-server.log 2>&1 &

Hatta yapılabilecek bir diğer güzellik de, django-admin.py'ın runserver komutunu genişleterek, django geliştirme sunucusuyla beraber konfigürasyondaki bilgilere göre statik sunucuların da çalıştırılması olabilir.

Son olarak, bu yöntemi ağ üzerinden [dosya paylaşımı yapmak için](http://www.harunseker.org/2011/12/python-simple-http-server-ile-dosya.html) de kullanabileceğinizi hatırlatmak isterim. Ağ üzerinde paylaşmak istediğiniz dizinde bu komutu çalıştırdığınızda ağdaki bir diğer bilgisayardan bilgisayarınızın ip adresi ve belirttiğiniz port numarası ile dizininizde gezilebilir ve dosyalar çekilebilir.
