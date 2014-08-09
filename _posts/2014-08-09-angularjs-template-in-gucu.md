---
layout: post
title: "AngularJS'de template'in gücü"
categories: turkish
tags: angularjs, javascript
---

[Sahibinden](http://www.sahibinden.com)'de 1 yıldan fazla zamandır kullanmaya başladığımız [AngularJS](http://angularjs.org)'nin en etkili özelliklerinden biri şüphesiz başarılı şablon motoru(template engine). [Deklaratif programlama](http://en.wikipedia.org/wiki/Declarative_programming)nın güzel bir örneği olan Angular templateleri, kod okunabilirliği, görsellik ve işlevsel kodların ayrımı konularında güzel imkanlar veriyor. Şimdi bu imkanları nasıl kullanabildiğimize bir göz atalım.

## Anneannemizin yöntemi

Bu örneği çok sık veriyorum ancak, konuya uygun ve anlaşılması kolay olduğu için tekrar bir "tab arayüzü"nün yapılması için kullandığımız yöntemler üzerinden konuyu açıklamaya çalışacağım. Bir çok [jQuery](http://jquery.com) yazan front-end geliştiricisi, bir web sayfasında tab görünümünü elde etmek için aşağıdaki gibi bir HTML yapısı kullanır.

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

{% include codepen.html hash="gtayb" %}

Buradaki temel problem aslında bu kadar basit bir kullanıcı etkileşimi ve DOM manipülasyonu için bile Javascript yazmak zorunda kalmamız. jQuery'nin de bu kadar popüler olmasının sebebi, Javascript'te yaptığımız DOM manipülasyonlarının çokluğu aslında. Ancak Javascript içerisinde yaptığımız her DOM manipülasyonu, bu kodu HTML'ine ve CSS koduna daha da bağımlı hale getiriyor ve kırılganlığı artırıyor.

## "Angular way"[^1]

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

Angular'ın sundugu [ng-class](https://docs.angularjs.org/api/ng/directive/ngClass) directive'i, verdiğiniz şartlara göre istediğiniz bir class'ın elemente eklenip çıkarılmasını sağlıyor. [ng-click](https://docs.angularjs.org/api/ng/directive/ngClick) directive'i ise, Javascript'in DOM eventlerine benzer şekilde, karşısına verdiğimiz kodu çalıştırmaya yarıyor. Ancak üzülmeyin, karşısındaki kod global scope'da değil, Angular'ın bu template için oluşturduğu özel bir scope'da çalışıyor.

Görüldüğü gibi tabların görünme şartlarını, hangi durumda elementlerin ne class değeri alacağını ve durum değişimlerinin hangi event'ler ile ne şekilde olacağını template'de tanımladık. Sayfada ne döndüğünü template'i okuyarak anlamak mümkün.

Peki javascript kodumuz ne olacak?

İşin güzel tarafı burası: Angular'da yukarıdaki template ile bir tab görünümü uygulaması çalıştırmak için *ekstra bir javascript koduna ihtiyaç yok*.

İşte çalışan örneği de şu şekilde:

{% include codepen.html hash="zqHrv" %}

## Neler kazandık?

- Javascript kodumuzun içerisinde görsel işlemler yapmaktan kurtulduk. AngularJS'de DOM manipülasyonu yapılan tek alan [directive](https://docs.angularjs.org/guide/directive) yazımıdır(Bu konuya daha sonra değineceğim). Bunun dışındaki javascript kodları tamamen iş akışları ve veri manipülasyonundan ibarettir. Bu sayede javascript kodlarımız en sade, CSS ve HTML'e bulaşmayan, sadece görevi olan işi yapan bir kod bloğuna dönüşmüş oluyor.
- Kendini anlatan template'lere kavuştuk. Angular'da template'i okuduğunuzda o sayfada neler döndüğünü anlayabiliyorsunuz. Neyin hangi durumda görünüp, neyin görünmeyeceğini, nereye tıklandığında ne olacağını rahatça farkedebiliyorsunuz. Ve tüm bunları inline javascriptler yazmak gibi kötü bir yöntemle de yapmıyoruz.
- Klasik manada DOM manipülasyonlarını Javascript kodları üzerinde yaptığımızda, arayüzün değişen verilere göre her zaman doğru görünümde ve işlevsellikte kalması bizim sorumluluğumuzda kalıyor ve bunu yapmak her zaman pek kolay olmuyor. Ayrıca kodumuzu da oldukça kirletiyor. Angular template'lerinde ise bu iş otomatik olarak yapılıyor. Yani biz aslında template'de state'leri tanımlıyoruz ve Angular bu template'i her duruma göre canlı tutuyor. Bu konu kendi başına ele alınabilecek genişlikte temel bir başlık. Umarım ileride değiniriz.

Yukarıdaki örnek çok basit(ancak çok sık kullanılan) bir ihtiyaç üzerineydi. Bunun gibi bir çok ihtiyaç için Angular bize [hazırda bir çok directive](https://docs.angularjs.org/api/ng/directive) sunuyor.

## Sonuç

Gitgide popülerleşen AngularJS'nin template yapısını, hemen her önyüz geliştiricisinin aşina olduğu jQuery alışkanlıkları üzerinden anlatmaya çalıştım. Biraz dağınık anlatmış olabilirim. Eğer böyle düşünüyorsanız, yönelteceğiniz soru ve önerilerle bu eksiği gidermeye çalışabilirm.

[^1]: Aslında bir tab view için "Angular way" tam olarak bu değil. Bu işin "Angularcası" [bu iş için bir directive](http://angular-ui.github.io/bootstrap/#/tabs) yazmaktır. Ancak bu konuya daha sonra ayrıntılı olarak gireceğim için burada kafa karıştırmak istemedim.

