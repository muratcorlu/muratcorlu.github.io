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

Bu haliyle kodun çalışan bir örneği şu şekilde olacak:

<p data-height="268" data-theme-id="0" data-slug-hash="gtayb" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/muratcorlu/pen/gtayb/'>jQuery tabbed view example</a> by Murat Çorlu (<a href='http://codepen.io/muratcorlu'>@muratcorlu</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//codepen.io/assets/embed/ei.js"></script>

Buradaki ilk problem aslında bu iş için bir JavascriptjQuery yazmaya aşina yazılımcıların

Bakın bu ihtiyacı Angular ile nasıl gideriyoruz:

{% highlight html %}
<ul class="tab-navigation">
  <li ng-class="{'active': activeTab != 2}">
    <a href="#" ng-click="activeTab=1">Tab Baslik 1</a>
  </li>
  <li ng-class="{'active': activeTab == 2}">
    <a href="#" ng-click="activeTab=2">Tab Baslik 2</a>
  </li>
</ul>

<div class="tab-content" ng-class="{'active': activeTab != 2}">
  <p>Tab icerik 1</p>
</div>

<div class="tab-content" ng-class="{'active': activeTab == 2}">
  <p>Tab icerik 2</p>
</div>
{% endhighlight %}

Görüldüğü gibi tabların görünme şartlarını, hangi durumda elementlerin ne class değeri alacağını ve durum değişimlerinin hangi event'ler ile ne şekilde olacağını template'de tanımladık. Sayfada ne döndüğünü template'i okuyarak anlamak mümkün.

Peki javascript kodumuz ne olacak?

Hiç. Evet, Angular'da yukarıdaki template ile bir tab görünümü uygulaması çalıştırmak için ekstra bir javascript koduna ihtiyaç yok.

İşte çalışan örneği de şu şekilde:

<p data-height="268" data-theme-id="0" data-slug-hash="zqHrv" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/muratcorlu/pen/zqHrv/'>Tabbed View Angular Example</a> by Murat Çorlu (<a href='http://codepen.io/muratcorlu'>@muratcorlu</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//codepen.io/assets/embed/ei.js"></script>

