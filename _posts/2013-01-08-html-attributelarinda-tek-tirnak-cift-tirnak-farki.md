---
layout: post
title: HTML attribute'larında tek tırnak - çift tırnak kullanımı
categories: turkish
tags: html
---

Son zamanlarda haricen aldığımız javascript hizmetlerinin örnek kodlarında HTML attribute'larının çift tırnak yerine tek tırnakla yazıldığını sıklıkla görüyorum.

{% highlight html %}
<link rel='stylesheet' type='text/css' href='css/bootstrap.css' />
{% endhighlight %}

Bu benim genel alışkanlığımın tersine bir yaklaşım, zira ben -standartların da böyle olduğunu düşünerek- bu tek tırnak yazımlarını çift tırnakla değiştiriyordum. Geçenlerde bir başka sitenin daha örnek kodunda tek tırnak kullanımını görünce bu işin HTML yazım standartlarına uygunluğunu bir kontrol edeyim dedim ve [W3C'nin HTML4 dokümanlarında](http://www.w3.org/TR/html4/intro/sgmltut.html#h-3.2.2) şöyle bir metne ulaştım:

> By default, SGML requires that all attribute values be delimited using either double quotation marks (ASCII decimal 34) or single quotation marks (ASCII decimal 39). Single quote marks can be included within the attribute value when the value is delimited by double quote marks, and vice versa. Authors may also use numeric character references to represent double quotes (&#34;) and single quotes (&#39;). For double quotes authors can also use the character entity reference &quot;.

> In certain cases, authors may specify the value of an attribute without any quotation marks. The attribute value may only contain letters (a-z and A-Z), digits (0-9), hyphens (ASCII decimal 45), periods (ASCII decimal 46), underscores (ASCII decimal 95), and colons (ASCII decimal 58). We recommend using quotation marks even when it is possible to eliminate them.

Yani tek tırnak veya çift tırnak kullanmak konusunda özgür olduğumuz hatta boşluk içermeyen değerleri tırnaksız bile verebileceğimiz belirtilmiş. XHTML referansının "[HTML4 ile farklar](http://www.w3.org/TR/xhtml1/Overview.html#diffs)" bölümünde ise, sadece HTML4'de zorunlu olmayan tırnakların, XHTML ile birlikte zorunlu hale geldiği ve değeri belirtilmeyen attribute'ların(```<input type="text" disabled>``` gibi) artık geçersiz olduğu yazılmış. Bu fark HTML5 dokümanındaki [HTML4 ve XHTML karşılaştırma tablosu](http://dev.w3.org/html5/html-author/#html-and-xhtml-comparison-1)nda da gösteriliyor.

Bunlardan anlaşıldığı üzere attribute'larda tek tırnak HTML4'den beri geçerli bir kullanımmış. HTML5'in "geriye uyumluluk(backward compatible)" olduğu göz önünde bulundurulduğunda HTML4'deki gibi, tek tırnaklı, çift tırnaklı veya tırnaksız attribute değeri vermenin geçerli bir yazım şekli olduğunu görmekteyiz. Ben en azından okunabilirlik açısından çift tırnak ile yazmayı daha makul buluyorum ancak bunun alışkanlığımız eseri olabileceği ihtimalini de kabul ediyorum.

Siz hangisini tercih edersiniz?