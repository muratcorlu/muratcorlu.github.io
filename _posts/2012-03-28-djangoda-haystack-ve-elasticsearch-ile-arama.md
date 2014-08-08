---
layout: post
title: Django'da Haystack ve Elasticsearch ile arama
categories: turkish
tags: django, python, haystack, elasticsearch, fulltextsearch, arama
---

Django, verilere hızlıca erişim ve düzenleme için çok güzel bir model katmanına sahip. Her ne kadar bu modellerde filtreleme imkanları oldukça kullanışlı görünse de, büyük veri ve yoğun kullanımlarda veritabanından sorgular yaparak arama yapma devri geçmişte kaldı. Çünkü artık küçük verilere çok daha hızlı erişebilen ve arama konusu üzerine uzmanlaşmış bir çok başarılı uygulama var. Bunlara en bilinen örnekler olarak [Solr](http://lucene.apache.org/solr/), [Sphinx](http://sphinxsearch.com) ve henüz bunlara göre toy olmasına rağmen performansı ve kullanım kolaylığıyla bir çok yazılımcıyı büyüleyen [Elasticsearch](http://elasticsearch.org) uygulamalarını verebiliriz. Ben bu yazımda yakın zamanda kullanmaya başladığım Elasticsearch'den ve Elasticsearch'ü Django'da nasıl kullanabileceğimizden bahsedeceğim.

<!--more-->

Elasticsearch, [Apache Lucene](http://lucene.apache.org) projesinin üzerine bina edilmiş, kendini arama konusuna adamış, açık kaynak, REST arayüzlü, dağıtık çalışabilen, şema bağımsız veri taşıyabilen, Java tabanlı oldukça başarılı bir arama motoru. Elasticsearch REST tabanlı olduğu için, herhangi bir programlama diliyle kolayca entegre edilebiliyor. Python için yazılmış istemcilere verilecek ilk örnekler [pyes](http://github.com/aparo/pyes) ve [pyelasticsearch](http://github.com/rhec/pyelasticsearch).[*][1]

[Django-Haystack](http://haystacksearch.org/) uygulaması ise, Django'da Elasticsearch ve benzeri bir çok arama motorunu kolayca kullanabilmek için oluşturulmuş bir ara katman. Haystack uygulamasını kullanarak seçtiğimiz veya ileride seçeceğimiz arama motorumuz ne olursa olsun, aynı metodları kullanarak işimizi görebiliyoruz. Aynı anda birden fazla arama motorunu kullanmaya imkan vermesi sayesinde de, uygulamamızın bir kısmında Solr kullanırken, diğer bölümünde Elasticsearch kullanabiliyoruz ve bunun için atılması düşünülen bir çok takladan kurtulmuş oluyoruz.

Şimdi kolları sıvayıp, django-haystack ve elasticsearch ile küçük bir arama uygulaması yapalım.

## Kurulum

Django-haystack uygulamasını `pip install django-haystack` komutu ile kolayca kurabiliyoruz. Ancak, haystack uygulamasının şu anki(Mart 2012) son kararlı sürümü olan 1.2.6 sürümünün içinde elasticsearch arayüzü hazır olarak gelmediğinden ben burada şu an beta sürümünde olan 2.0 sürümü üzerinden anlatacağım. 2.0 sürümünü de haystack'in github deposundan, yine pip ile `pip install -e git+https://github.com/toastdriven/django-haystack.git@master#egg=django-haystack` komutu ile kurabiliriz.

Elasticsearch Java ortamı gerektirmektedir ancak kendi içinde işini görebilecek boyutta bir Java ortamı ile beraber geliyor. Elasticsearch'ün dilediğiniz versiyonunun sıkıştırılmış dosyasını [indirme sayfasından](http://www.elasticsearch.org/download/) edinip, bilgisayarınızda herhangi bir yere açtıktan sonra, açılan dosyalardan bin klasöründeki elasticsearch uygulamasını çalıştırarak kolayca başlatmış olursunuz.[*][2] Kurulu versiyon için MacOSX'de brew (`brew install elasticsearch`), Ubuntu'da da aptitude (`apt-get install elasticsearch`) kullanabilirsiniz. Elasticsearch'ü  kurduktan sonra python ile kullanabilmek için pyelasticsearch modülüne de ihtiyacımız olacak. Onun haystack uyumlu versiyonunu da aşağıdaki komutlarla kurabilirsiniz:

    :::bash
    git clone https://github.com/toastdriven/pyelasticsearch
    cd pyelasticsearch
    python setup.py install

## Ayarlar

Haystack uygulamasını settings.py dosyasımızdaki INSTALLED_APPS listemize ekliyoruz. Buna ek olarak bir de HAYSTACK_CONNECTIONS değişkeni ile Elasticsearch bağlantı bilgilerimizi vermemiz gerekiyor:

    :::python
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',

        'haystack',
    )

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'blog',
        },
    }

Elasticsearch varsayılan olarak 9200 portundan çalışıyor. INDEX_NAME değeri de veritabanı adı gibi düşünülebilir. Elasticsearch'ün varsayılan ayarlarında çalışması deneme yapabilmemiz için yeterli.

Haystack uygulamasının vereceğimiz index tanımlarını otomatik tanıması için, Django uygulamamızın ana klasörüne(settings.py ile aynı yere) aşağıdaki içerikte search_sites.py adlı dosyamızı oluşturalım:

    :::python
    import haystack

    haystack.autodiscover()

## Verilerin indekslenmesi

Örneğimizde bir blog uygulamamız olacak ve blog yazılarının başlıklarında bir arama yapacağız. Yazımız için modelimiz aşağıdaki gibi olsun:

    :::python
    from django.db import models
    from django.contrib.auth.models import User

    class BlogPost(models.Model):
        title = models.CharField(max_length=200)
        author = models.ForeignKey(User)
        content = models.TextField()
        create_date = models.DateTimeField(auto_now_add=True)
        modified_date = models.DateTimeField(auto_now=True)

Modelimizi oluşturduktan sonra syncdb komutuyla veritabanını senkronize edip yönetici panelinden de deneme için birkaç yazı ekleyebilirsiniz.

Arama motorları aramada kullanılacak verileri kendi içine, belirledikleri algoritmalarla alırlar ve bu veriler üzerinde arama yapma imkanı verirler. Bu işleme indeksleme denir. Biz de şimdi BlogPost modelimizden hangi verileri indeksimize alacağımızı belirteceğiz. Bu işlemi uygulama klasörünün içine search_indexes.py adlı bir dosya açarak yapıyoruz:

    :::python
    from haystack import indexes
    from blog.models import BlogPost

    class PostIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
        text = indexes.CharField(document=True, use_template=True)
        title = indexes.CharField(model_attr='title')

        def get_model(self):
            return BlogPost

Örneğimizde PostIndex adlı bir indeks oluşturduk. Bunu haystack'in RealTimeSearchIndex sınıfını miras alarak oluşturduğumuz için modelimizdeki değişikliklerde(yazı eklenmesi, silinmesi gibi) Elasticsearch indeksimiz otomatik olarak güncellenecek. Haystack indeks tanımlamalarında get_model metodu yazılarak ilgili modelin belirtilmesi ve mutlaka bir adet text adlı alan bulunması zorunludur. Bu alan varsayılan olarak üzerinde arama yapılacak alandır. Bu alana verdiğimiz use_template parametresi bu alan için oluşturacağımız bir template dosyamızın var olduğunu belirtiyor. Bu dosyamızı da templates klasörümüzün içinde search/indexes/[uygulama adı]/[model adı]_[alan adı].txt yoluna(bu örneğimiz için: templates/search/indexes/blog/blogpost_text.txt) koymamız gerekiyor:

    {{ object.title }}
    {{ object.author }}

Bu şekilde text alanına modelimizden başlık ve yazar bilgilerini ekleyerek indeksletmiş olduk. Bu sayede yazılarımızda hem yazar adı hem de yazı başlığı ile arama yapma imkanına sahip olacağız.

"Yazı başlığını text alanına eklediysek, title alanını indekse eklemeye ne gerek var?" sorusu aklınıza gelmiş olabilir. text alanında sadece birebir yazı başlığını kullansak, tekrar title alanını eklemeye gerek kalmazdı, ancak, şu durumda arama yaptıktan sonra, arama sonucu olarak başlıkları listelerken yazı başlıklarına ihtiyaç olacağı için, text alanından yazı başlığını çıkartmaya çalışmak veya her sonuç satırı için veritabanına gidip yazı başlığını alma külfetine girmemek için yazı başlığını ayrıca indekse ekledik. Unutmayalım ki, aramayı elasticsearch gibi bir ortama almaktaki en önemli amaçlarımızdan biri arama işlerini veritabanının üzerinde alarak gereksiz yük oluşturmamak.

İndeksleme bilgilerini girerken burada hepsine değinemeyeceğim daha bir çok imkan var. Bunları [ilgili doküman](http://django-haystack.readthedocs.org/en/latest/searchindex_api.html)dan inceleyebilir veya özellikle merak ettiğiniz bir konu olursa bu yazıya yorum girerek sorabilirsiniz.

Verilerimizin ilk kez indekslenmesi için aşağıdaki komutu çalıştırmamız gerekiyor:

    python manage.py update_index blog.BlogPost

Sonda verdiğimiz model parametresi opsiyoneldir. Eğer yazmazsanız varolan bütün indeksler güncellenir. Bu komutu çalıştırmadan önce elasticsearch'ün çalıştığından emin olun.

## Arama sorgusu

Verilerimiz indekslendiğine göre artık ilk sorgumuzu yapabiliriz. Bunun için önce bir url tanımlayalım:

    urlpatterns = patterns('',
        url(r'^blog/search/$', 'blog.search'),
    )

Bu adrese gelecek talepleri alacak view metodumuzu da uygulama klasöründeki views.py dosyamıza ekliyoruz:

    :::python
    from django.http import HttpResponse
    from haystack.query import SearchQuerySet

    def search(request):
        results = SearchQuerySet().filter(content__startswith=request.GET.get('q'))[:10]
        results_text = '\n'.join([row.title for row in results])
        return HttpResponse(results_text, content_type="text/plain")

Sorgular için haystack'in SearchQuerySet'ini kullanıyoruz. Kullanımı Django'nun model query'sine oldukça benziyor. Çok benzer şekilde çalışan filter metodunu kullanarak q querystringi ile gelen metinle başlayan kelimelerin bulunduğu 10 adet kaydı çekiyoruz. Burada text__startswith yazmak yerine content ismini kullanmamız dikkatinizi çekmiştir. content ismi, haystack tarafından sunulmuş özel bir alan adı ve tüm dokümanda arama yapma imkanı veriyor. filter'da Django'da olduğu gibi indeksteki diğer alanlara özgü filtrelemeler yapmamız da mümkün. Örneğin indeksimize user alanı da eklediğimizi varsayarsak:

    :::python
    SearchQuerySet().filter(user__iexact="murat").filter(content__startswith=request.GET.get('q'))[:10]

gibi zincirleme sorgular yapabiliriz.

Tüm bu işlemleri başarıyla tamamladığınızda, django uygulamamızı çalıştırıp http://127.0.0.1:8000/blog/arama/?q=django gibi arama yaptığımızda başlığında veya yazar adında django ile başlayan kelimeler bulunan yazılardan ilk 10'unun başlıklarının listelendiğini göreceksiniz.

## Sonuç

Benim de yeni tecrübe ettiğim ve çok sevdiğim bir alanda sizinle tecrübelerimi paylaşmak istedim. Umarım faydalı olmuştur. Konuyla ilgili soru veya katkılarınızla bu yazıyı daha da faydalı bir kaynağa dönüştürebiliriz.

[1]: http://www.elasticsearch.org/guide/appendix/clients.html "Diğer diller için liste [İngilizce]"
[2]: http://www.elasticsearch.org/guide/reference/setup/installation.html "Ayrıntılı bilgi [İngilizce]"
