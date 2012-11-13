title: "Dropbox'ı FTP gibi kullanmak"
date: 2012-01-26 10:43
categor: turkish

[Dropbox](http://db.tt/1ImfZir) birden fazla bilgisayar, telefon veya tablet üzerinde senkronize bir klasör sahibi olmanızı sağlayan, bu klasörden istediklerinizi başkalarıyla paylaşarak, üzerinde ortak çalışma şansı sunan, son zamanların en güzel yazılım çözümlerinden biri. Biraz daha açmak gerekirse; Dropbox'a ücretsiz üye olup, bilgisayarınıza kurduğunuzda, Belgelerim altında bir klasörünüz artık devamlı Dropbox sunucularına yedeklenmeye başlanıyor. Aynı üyelikle başka bir bilgisayara daha(mesela iş bilgisayarınıza) Dropbox kurduğunuzda, aynı dosyalar otomatik olarak buraya da kopyalanıyor. Herhangi bir bilgisayarda bu dosyalarda bir değişiklik yapıldığında, diğer bağlantılı bilgisayarlara da otomatik yansıtılıyor.

Bu tür teknoloji aslında yeni sayılmaz. Uzak disklerin bilgisayara bağlanması ve bu disk üzerinde çalışmak daha önce de kullanılan bir yöntemdi ancak Dropbox işi oldukça kolaylaştırdı. Aynı dosyalara web tarayıcısı üzerinden, [iPhone](http://itunes.apple.com/us/app/dropbox/id327630330?mt=8) ve [Android](https://market.android.com/details?id=com.dropbox.android) uygulamaları sayesinde mobilden de erişebilmek de Dropbox'ı temel ihtiyaç maddesine dönüştürebiliyor.

Bense bu yazıda size Dropbox'ın [komut satırı istemcisi](http://www.dropboxwiki.com/Using_Dropbox_CLI)nin sağladığı bir nimetten bahsetmek istiyorum.
<!--more-->

## Ne gerek var?

Kişisel sanal sunucu ihtiyacım için yıllardır [Linode](http://www.linode.com/?r=c2c44c598b1a93f61a9aadc7eb9c1396b8456d08)'u kullanıyorum. Sunucunun sistemini kendim yönetebilmek adına herhangi bir sunucu yönetim uygulaması(Plesk vs.) da kullanmıyorum. Sunucumdan yer verdiğim birkaç kişiye sitelerinin dosyalarını değiştirebilme imkanı vermem gerekiyor. FTP kurmak ve bunun güvenliğini sağlamak meşakkatli bir iş. Her FTP kullanıcısı için bir sistem kullanıcısı açmak falan... İşte bu konuda imdadıma Dropbox CLI yetişiyor.

[Dropbox CLI](http://www.dropboxwiki.com/Using_Dropbox_CLI) sayesinde sunucuma da Dropbox kurabiliyorum. Arkadaşıma dosyalarını değiştirme imkanı vereceğim sitenin dosyalarını Dropbox klasörüne sembolik link yaparak ekliyorum. Sonra Dropbox yönetim panelinden arkadaşım ile bu klasörü paylaşıyorum(onun da Dropbox hesabı olması gerekiyor). Bu andan itibaren arkadaşımın bilgisayarında da sitenin dosyalarının bir kopyası oluyor. Her iki tarafta yapılan değişiklikler senkronize ediliyor. Böylece kişi siteyi kendi bilgisayarında düzenliyor, dosyayı kaydettikten sonra saniyeler içerisinde site de güncellenmiş oluyor.

Bu kullanımın bir diğer avantajı da Dropbox'ın dosyalarınızı versiyonlaması. Dropbox'da bulunan dosyalarınızın ilk oluşturulduğu tarihe kadar bütün versiyonlarına Dropbox yönetici panelinden erişebiliyorsunuz. Bu da yanlışlıkla silinebilecek veya bozulacak dosyalar için büyük bir güven kaynağı oluyor.

Aynı klasör aynı anda birçok dropbox kullanıcısıyla paylaşılabiliyor. Böylece bir ekipte sitede herhangi bir değişiklik yapıldığında ekipteki herkes haberdar olabiliyor.

## Avantajlar

FTP yerine Dropbox kullanmanın sağlayacağı avantajları maddelersek:

1. FTP'den çok daha basit bir kullanım şansı veriyor.
2. Dosyalar otomatik olarak versiyonlanıyor ve yedekleniyor.
3. Birden fazla kullanıcı ortak kullanabiliyor.

## Dezavantajlar

FTP yerine Dropbox kullanmanın dezavantajları da yok değil:

1. Dropbox CLI sistemde hatırı sayılır bir hafıza tüketiyor. İhtiyaç olmadığında uygulama durdurulabilir.
2. Dosya izinleri taşınmıyor. Dolayısıyla bir dosyaya örneğin 777 izni vermek gerekirse, bunu elle sunucuya girip yapmak gerekir.
3. Dropbox klasörlerine şifre koyma şansı yok. Dolayısıyla sitenin dosyaları bilgisayarda açıkda duruyor olacaklar. Ortak kullanılan bilgisayarlarda riskli olabilir.

## Sonuç

FTP olarak kullanmak elbette ki Dropbox'ın temel amacı değil ve Dropbox, bu amaç için kullanılmasa da oldukça faydalı. Ben bir özellik olarak sunulmayan ancak şartların kendiliğinden doğurduğu ve benim de faydalandığım böyle bir imkandan haberdar etmek istedim.

Dropbox'a üye olmayanlar için de aşağıdaki referans bağlantımla üye olmalarını tavsiye ederim. Referansım ile 250MB fazladan alan kazanacaksınız.

[http://db.tt/1ImfZir](http://db.tt/1ImfZir)
