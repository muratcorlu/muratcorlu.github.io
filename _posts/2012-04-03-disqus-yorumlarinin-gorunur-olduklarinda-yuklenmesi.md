---
title: Disqus yorumlarının görünür olduklarında yüklenmesi
categories: turkish
tags: disqus, javascript, octopress, jquery
---

[Disqus](http://disqus.com), artık bir çok blogda kullanılan çok başarılı bir yorumlama hizmeti. Özellikle statik blogların yaygınlaştığı günümüzde, dinamik üretilmeyen sayfalarda bile yorum yazılabilmesi imkanı verdiği için hayat kurtarıcı bir çözüm.

Disqus'ın sunduğu javascript kodunu kullandığınızda sayfa yüklenirken yorumların olacağı yere gelindiğinde Disqus tarafından sunulan javascript dosyası yükleniyor ve bu dosya ihtiyaç duyduğu dosyaları da yükletip, yorumları sayfaya ekliyor. Bloglarda genelde bir yazı açıldığında yazının uzunluğundan dolayı yorumlar ilk anda görüntüde olmuyorlar. Ancak bu geleneksel yöntemimizde birşeyi değiştirmiyor ve görüntüde olmamasına rağmen yorumlar sayfa açılırken yükleniyor. İçinde başka öğelerin de bulunduğu(videolar, resimler ve başka javascriptler) uzun yazılı blog sayfalarını açarken, görüntüde olmadığı halde Disqus yorumlarının da ilk açılışta yükleniyor olması hissedilir bir yük oluşturuyor. İşte buna çözüm olarak, [jQuery](http://jquery.com) kütüphanesinden ve Mike Green'in [bir yazısı](http://www.myatus.com/2011/03/20/lazy-loading-disqus-in-wordpress/)ndan faydalanarak yazdığım aşağıdaki javascript dosyası ve HTML5'in data attribute özelliğinden faydalandığım aşağıdaki gibi bir HTML yazımı ile Disqus yorumlarını kullanıcı sayfayı yorumların olduğu bölümlere kaydırdığı anda yükletebilirsiniz:

{% highlight javascript %}
/**
* Load disqus comments when visitor scroll down page to comments
*
* Usage:
* Add a div with id "disqus_thread" and data attributes for every disqus parameter:
*
* <div id="disqus_thread" data-disqus-shortname="username" data-disqus-url="http://example.com/post/post-name/"></div>
*
* @author: Murat Corlu
* @link: https://gist.github.com/gists/2290198
*/
$(function(){
    var disqus_div = $("#disqus_thread");
    if (disqus_div.size() > 0 ) {
        var ds_loaded = false,
            top = disqus_div.offset().top, // WHERE TO START LOADING
            disqus_data = disqus_div.data(),
            check = function(){
                if ( !ds_loaded && $(window).scrollTop() + $(window).height() > top ) {
                    ds_loaded = true;
                    for (var key in disqus_data) {
                        if (key.substr(0,6) == 'disqus') {
                            window['disqus_' + key.replace('disqus','').toLowerCase()] = disqus_data[key];
                        }
                    }

                    var dsq = document.createElement('script');
                    dsq.type = 'text/javascript';
                    dsq.async = true;
                    dsq.src = 'http://' + window.disqus_shortname + '.disqus.com/embed.js';
                    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                }
            };

        $(window).scroll(check);
        check();
    }
});
{% endhighlight %}

Bu da html tarafı:

{% highlight html %}
<div id="disqus_thread" data-disqus-shortname="muratcorlu" data-disqus-url="http://muratcorlu.com/post/post-name/"></div>
{% endhighlight %}

HTML5 ile gelen data attribute'ları bu tür ihtiyaçlar için biçilmiş kaftan. Ancak eğer HTML dokümanlarınızı HTML5 tipinde deklare etmiyorsanız bu attribute'ları kullanmak dosyanızın validasyonunu bozacaktır. Bunun yanında normalde IE7'nin data attribute desteği olmamasına rağmen jQuery bu problemi çözmektedir.

Bu çözümü <del>şu anki blog üretme motorum olan</del> [Octopress](http://octopress.org)'de nasıl uyguladığımı görmek isterseniz Github'daki bu iş için yaptığım değişikliklerden ibaret olan [commitimi](https://github.com/muratcorlu/muratcorlu.github.com/commit/381b1eb24292db1436d83deeeacdceca836e901c) inceleyebilirsiniz.
