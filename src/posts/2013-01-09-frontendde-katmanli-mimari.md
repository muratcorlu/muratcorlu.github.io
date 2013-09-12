title: Önyüz kodlamasında katmanlı mimari ve önemi
date: 2013-01-09 09:00
categories: turkish
tags: html, css, javascript
status: draft

Katmanlı mimari, bir yazılım projesinin farklı görevlerini(katman) üstlenen teknolojilerin, bu görevlerine sadık kalması ve diğerinin alanlarına da bulaşmaması, tabiri caizse "haddini bilmesi" olarak tanımlanabilir. Bariz olan konulardan örnek verirsek, çatalla çorba içmek, ütü ile mangal yapmak, java ile web sitesi yapmak, bazı güzelliklerin asıl görevlerinin dışında kullanımına örneklerdendir.

Web önyüz(front-end) kodlamasında, elimizdeki 3 ana dil olan HTML, CSS ve Javascript'i, yerinde ve sınırında kullanmak, aslında çok zor gözükmese de başarabilenin az olduğu bir maharet halini almış durumda. HTML'de tablo ile tasarım yaptığımız yıllardan bu yana kurtulamadığımız bu hastalıkla ilgili düşüncelerimi paylaşmak istiyorum.

Öncelikle önyüz kodlamasındaki bu 3 ana dilin temel görevlerini özetle belirtmek isterim:

Katman       | Görevi
-------------|--------------
HTML         | Veri
CSS          | Sunum
Javascript   | İnteraktivite ve işlevsellik

## HTML - Veri katmanımız

HTML, bir web sayfasının veri sunma katmanıdır. Bu "sadece"dir ve ama "mutlaka"dır da[^1]. Yani, sayfada bir veri sunulacaksa, bu mutlaka HTML içerisinde bulunmalı ve HTML'de veri sunumu dışında birşey olmamalı.

Tablo ile tasarım yapmak, amacı tabular veri sunmak olan bir elementin kötüye kullanılması ve HTML'in işi olmamasına rağmen görsel bir unsur kazandırma çalışmasıdır. Oysa daha sonra değineceğim gibi, sayfadaki verinin nasıl görüneceği işi HTML'e değil, CSS'e ait bir görevdir. Görsel etkiyi artırmak için kullanılan tasarıma ait resimlerin de HTML içinde img etiketiyle belirtilmesi yine yanlıştır.

Bununla birlikte, sayfanın içeriği olduğu halde bir verinin HTML'de belirtilmemesi de hatadır. Bir kullanıcının paylaştığı fotoğrafın sayfada javascript veya css ile değil, direkt olarak img etiketiyle sunulması gerekir.

Bu kurallar, geliştirme ortamımıza düzen getirmek gibi birlikte, insanların hayatına daha somut faydalar da sağlamaktadır. Örneğin kör bir internet kullanıcısı için HTML kodunun standartlara uygun yazılması, onun web sitesinden faydalanabilmesi için neredeyse şarttır. Ayrıca sayfanızın içeriğini javascript ve css kodlarınızdan çıkarıp bulması oldukça zor olacak arama motorları için de, HTML'in kurallara uygun yazılması, sitenizin daha doğru indekslenebilmesi ve aramalarda hedef kitleye ulaştırılabilmesi adına oldukça önemlidir.

## CSS - Sunum katmanı



[^1]: Bu "mutlakalık" kısmı "web uygulamaları"nda biraz daha tartışmalı gibi. Web uygulamalarında genelde hiç HTML yazmadan, Javascript ile DOM manipülasyonlarıyla işimizi görüyoruz. Ancak bu yazıda bu konuya girmeyeceğim.