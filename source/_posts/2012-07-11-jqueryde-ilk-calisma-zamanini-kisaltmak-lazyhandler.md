---
layout: post
title: "jQuery'de ilk çalışma zamanını kısaltmak: lazyHandler"
date: 2012-07-11 23:21
comments: true
categories: turkish
tags: [javascript, jquery, tuning]
---

Javascript frameworkleri arasında neredeyse alternatifsiz kalan [jQuery](http://jquery.com) frameworkünü kullanmayan-bilmeyen web geliştirici yoktur sanırım. jQuery'i bu kadar popüler yapan şey sanırım herşeyden önce çok başarılı olan CSS seçicisi([Sizzle](http://sizzlejs.com/)). Ancak oldukça eğlenceli olan CSS seçicisi kullanmak, fazla bonkör davranınca pek hoş sonuçlar doğurmuyor. Çok fazla etkileşim barındıran günümüz web sayfalarında, sayfa yüklenirken bir çok elemanın tıklama olayına Javascript metodlarımız bağlıyoruz(event handling). İşte bu durumlarda dikkatli olunmazsa, sayfamızın yüklenme süreleri uzayabiliyor, kullanıcıların sabrı zorlanabiliyor.

## Sorun nedir?

Olaylara fonksiyon atama işlemlerinde önemli bir süreyi CSS seçicileri çalıştırırken geçirebiliyoruz. Zira aşağıdaki tarzda bir seçiciden sayfa yükleme anında 10 tane çalıştırsak -HTML dokümanının büyüklüğüne ve tarayıcıya göre değişmekle birlikte- 200-300 milisaniye gibi bir süreyi sadece bu tarz olay dinleme atamaları ile geçirebiliriz:

{% gist 3092755 default.js %}

Burada her seçicide sadece ID kullanmak bir çözüm olabilir, zira ID ile eleman seçmek oldukça hızlı. Ancak karmaşıklaşan dokümanlarımızda ve artan etkileşim sayılarında, her elemana ID üretmek de başka dezavantajlara sebep olacaktır.

<!--more-->

## Seçiciyi sayfa yüklenirken değil, tıklama anında çalıştırsak?

Aynı problemi [sahibinden.com](http://www.sahibinden.com)'da geliştirme yaparken de yaşadık. Bir sayfada 8-10 tane elementin tıklamasına fonksiyon atadığımızda, eğer dokümanımız da biraz karmaşık ise, sayfanın ilk çalışma hızını(DOMReady) gözle görülür şekilde azaltıyorduk. Ve düşündüm ki, bu atadığımız 8-10 tıklama olayı, belki de çoğunlukla hiç kullanılmadan sayfadan çıkılıyordu. Yani, kullanılacağı garanti olmayan bir tıklama için kullanıcıyı sayfayı açarken fazladan 200 milisaniye daha bekletiyorduk.

Bu sıralarda okuduğum kullanıcı tecrübesi(user experience) ile ilgili bir kitapta şunlar yazıyordu:

> Araştırmalara göre, internette gezinen bir kullanıcı, bir linke tıkladığında 500 milisaniye ve altındaki beklemelere tepki vermiyor. Bu kadarlık bir süreyi "işlem yapma süresi" olarak görüyor ve bekliyor. Eğer 500 milisaniye ile 1 sn arasında herhangi bir tepki gelmezse, tıklamanın algılanmadığı tereddütü hasıl oluyor ve tekrar tıklıyor. 1 sn'yi geçen işlemlerde ise bir hata olduğuna hükmediyor. Bu yüzden 500 milisaniyeden daha uzun sürecek işlemlerde kullanıcıya işlemin devam ettiğiyle ilgili mutlaka bir bilgi verilmeli. Bu bir "yükleniyor" yazısı veya bunu ifade eden hareketli bir resim de olabilir.

Bu bilgilerden de kuvvet alarak, sayfa yüklenirkenki bu süreyi, tıklama anına aktarmak için denemelere başladım ve ortaya paket haline getirdiğim [lazyHandler eklentisi](https://github.com/muratcorlu/lazyHandler) çıktı.

## lazyHandler ne yapıyor?

lazyHandler ile olay atamanın kullanımı alışılagelmiş jQuery olay atamasına benzer:

{% gist 3092755 lazyhandler.js %}

Görüldüğü üzere sadece 3 karakterlik bir eklemeyle alışılagelmiş bir jQuery olay atamasını, lazyHandler yöntemine çevirmiş olduk. Peki böyle yapınca ne değişti?:

Normal yöntemde bu kod çalıştığı anda "#header li a.clickable" CSS seçicisi çalışır, kurala uygun elementler dokümanda aranır ve bunların tıklama olaylarına bu fonksiyon atanırdı. lazyHandler yönteminde ise bu kodun çalışması sadece bir diziye(array) bu CSS seçicisinin ve fonksiyonun atanmasından ibaret oluyor(lazyHandler dokümanda ilk kez çağrılıyorsa dokümanın tıklama olayına da bir fonksiyon atanıyor). Daha sonra dokümanın herhangi bir yerine tıklandığında, bu dizideki CSS seçicilerin tıklanan bölgedeki eleman(lar)a uyup uymadığı kontrol ediliyor ve uyan durumlarda karşılığındaki fonksiyon çağrılıyor.

## Ne faydası var?

Olay atamalarının bu yöntemle yapılması sayfa yüklenirken çalıştırdığınız olay ataması sayısı arttıkça faydasını daha çok gösteriyor. Çünkü bir CSS seçicinin çalışması 10 ms sürüyorsa ve bu şekilde 10 CSS seçici çalıştırıyorsanız, bu işlemleri lazyHandler ile yaptığınızda 99 ms kâra geçiyorsunuz, zira lazyHandler ile bu işlemi yapmak -yaklaşık- 1 ms sürüyor.

Aradaki farkı daha belirgin şekilde göstermek için hazırladığım bir [benchmark](http://jsperf.com/jquery-lazyhandler-performance-comparison)ı da inceleyebilirsiniz.

## Dezavantajı yok mu?

* lazyHandler ile atanan olaylar, dokümana her tıklamada -atanan olay sayısına bağlı olmakla birlikte- 50-60 milisaniyeye kadar ek süre getiriyor. Bunu şu ana kadarki kullanımlarımızda hiç problem etmedik.
* lazyHandler olayları dokümana atanarak dinlendiği için, mouseover, mouseenter vb. fare hareketlerini dinlemek için uygun bir yöntem değil. Belki klavye tuşlarını dinlemek için de kullanılabilir.
* lazyHandler [bubbling](http://www.quirksmode.org/js/events_order.html)'i desteklemiyor. Dolayısıyla aynı kurala uyan iki elemanın içiçe olduğu durumlarda, fonksiyon sadece içteki element için çalıştırılıyor.
* Bunların yanında lazyHandler seçicilerde [context](http://api.jquery.com/jQuery/#selector-context) verilmesini de şu anda desteklemiyor.

## Sonuç

Bu kodu sahibinden.com'un bazı bölgelerinde 2 yıldır kullanıyoruz. Bu kadar zamandır lazyHandler'dan bahsetmeyi önce erteledim, sonrasında da unuttum veya vakit bulamadım. Bu yazıya gelen geri dönüşlerle bu konuda daha faydalı şeylerin ortaya çıkacağını umuyorum. Yorumlarınızı bekliyorum.