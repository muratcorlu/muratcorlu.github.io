title: "Disqus yorumlarının görünür olduklarında yüklenmesi"
date: 2012-04-03 11:26
categories: turkish
tags: disqus, javascript, octopress, jquery

[Disqus](http://disqus.com), artık bir çok blogda kullanılan çok başarılı bir yorumlama hizmeti. Özellikle statik blogların yaygınlaştığı günümüzde, dinamik üretilmeyen sayfalarda bile yorum yazılabilmesi imkanı verdiği için hayat kurtarıcı bir çözüm.

Disqus'ın sunduğu javascript kodunu kullandığınızda sayfa yüklenirken yorumların olacağı yere gelindiğinde Disqus tarafından sunulan javascript dosyası yükleniyor ve bu dosya ihtiyaç duyduğu dosyaları da yükletip, yorumları sayfaya ekliyor. Bloglarda genelde bir yazı açıldığında yazının uzunluğundan dolayı yorumlar ilk anda görüntüde olmuyorlar. Ancak bu geleneksel yöntemimizde birşeyi değiştirmiyor ve görüntüde olmamasına rağmen yorumlar sayfa açılırken yükleniyor. İçinde başka öğelerin de bulunduğu(videolar, resimler ve başka javascriptler) uzun yazılı blog sayfalarını açarken, görüntüde olmadığı halde Disqus yorumlarının da ilk açılışta yükleniyor olması hissedilir bir yük oluşturuyor. İşte buna çözüm olarak, [jQuery](http://jquery.com) kütüphanesinden ve Mike Green'in [bir yazısı](http://www.myatus.com/2011/03/20/lazy-loading-disqus-in-wordpress/)ndan faydalanarak yazdığım aşağıdaki javascript dosyası ve HTML5'in data attribute özelliğinden faydalandığım aşağıdaki gibi bir HTML yazımı ile Disqus yorumlarını kullanıcı sayfayı yorumların olduğu bölümlere kaydırdığı anda yükletebilirsiniz:

{% gist 2290198 %}

HTML5 ile gelen data attribute'ları bu tür ihtiyaçlar için biçilmiş kaftan. Ancak eğer HTML dokümanlarınızı HTML5 tipinde deklare etmiyorsanız bu attribute'ları kullanmak dosyanızın validasyonunu bozacaktır. Bunun yanında normalde IE7'nin data attribute desteği olmamasına rağmen jQuery bu problemi çözmektedir.

Bu çözümü şu anki blog üretme motorum olan [Octopress](http://octopress.org)'de nasıl uyguladığımı görmek isterseniz Github'daki bu iş için yaptığım değişikliklerden ibaret olan [commitimi](https://github.com/muratcorlu/muratcorlu.github.com/commit/381b1eb24292db1436d83deeeacdceca836e901c) inceleyebilirsiniz.
