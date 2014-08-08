---
layout: post
title: "AngularJS'de template'in gücü"
categories: turkish
tags: angularjs, javascript
---

[Sahibinden](http://www.sahibinden.com)'de 1 yıldan fazla zamandır kullanmaya başladığımız [AngularJS](http://angularjs.org)'nin en etkili özelliklerinden biri şüphesiz başarılı şablon motoru(template engine). [Deklaratif programlama](http://en.wikipedia.org/wiki/Declarative_programming)nın güzel bir örneği olan Angular templateleri, kod okunabilirliği, görsellik ve işlevsel kodların ayrımı konularında güzel imkanlar veriyor. Şimdi bu imkanları nasıl kullanabildiğimize bir göz atalım.

Bu örneği çok sık veriyorum ancak, konuya uygun ve anlaşılması kolay olduğu için tekrar bir "tab arayüzü"nün yapılması için kullandığımız yöntemler üzerinden konuyu açıklamaya çalışacağım. Bir çok jQuery yazan front-end geliştiricisi, bir web sayfasında tab görünümünü elde etmek için aşağıdaki gibi bir HTML yapısı kullanır.

{% highlight html %}
<ul class="tab-navigation">
  <li class="active">
    <a href="#tabIcerik1">Tab Baslik 1</a>
  </li>
  <li>
    <a href="#tabIcerik2">Tab Baslik 2</a>
  </li>
</ul>

<div class="tab-content active" id="tabIcerik1">
  <p>Tab icerik 1</p>
</div>

<div class="tab-content" id="tabIcerik2">
  <p>Tab icerik 2</p>
</div>
{% endhighlight %}

Bu tarz bir yöntemle bir tab davranışı sergileyebilmek için aşağı-yukarı şöyle bir jQuery kodu işimizi görecektir:

{% highlight javascript %}
$(function () {
  $('.tab-navigation a').on('click', function (el) {
    var $el = $(this),
        targetId = $el.attr('href');

    $('.tab-content')
      .removeClass('active')
      .filter(targetId)
      .addClass('active');

    $el.parent('li')
      .addClass('active')
      .siblings()
      .removeClass('active');
  });
});
{% endhighlight %}
