---
layout: post
title: AngularJS kullanmak için 10 neden
categories: turkish
tags: angularjs, javascript
---

5 ay kadar önce [Sahibinden](http://www.sahibinden.com)'de [AngularJS](http://angularjs.org) ile başlayan flörtleşmemiz şu ara nişan aşamasında ve birlikteliğimizi duyuracağımız nikahımızı heyecanla beklemekteyiz. AngularJS de bu arada müthiş bir ivmeyle popülerleşiyor. Ülkemizde henüz pek yaygın kullanılmadığını gördüğüm bu güzel kütüphanenin tercih edilmesinde en etkili olduğunu düşündüğüm 10 yönünü listeleyerek AngularJS'ye mesafeli duranları bu tarafa doğru çağırmak istedim.

## 1. Görsel işlemler olması gereken yerde

Dünyanın en popüler javascript kütüphanesi jQuery'i en çok DOM manipulasyonu için kullanıyoruz. Zaten o da diğerlerinden farkını güçlü ve pratik DOM seçicisi motoru ve DOM gezinme imkanlarıyla ortaya koydu. Ancak acaba bir koşula göre sayfada birşeyin gösterilip gizlenmesi, javascript tarafında yapmamız gereken bir iş miydi? Yani, bir tab arayüzü düşünelim. Tabların kulakçıklarına basıldıkça ilgili içeriğin gösterilip diğerlerinin gizlenmesi işi için jQuery'de kod yazmak, DOM'da gezinmek Javascript kodlarımızı HTML ve CSS ile gereğinden fazla içli dışlı yaptığı gibi, kodu büyütüp, geliştirilebilirliği de düşürüyor. Ancak bu işi Angular'da tamamen template üzerinde tamamlayabiliyoruz:

{% highlight html %}
<ul class="tabs">
    <li ng-class="{active: activeTab=='ilkTab'}" ng-click="activeTab='ilkTab'">Ilk Tab</li>
    <li ng-class="{active: activeTab=='ikinciTab'}" ng-click="activeTab='ikinciTab'">Ikinci Tab</li>
</ul>
<div class="tabContents">
    <div ng-show="activeTab=='ilkTab'"> Ilk tab icerigi </div>
    <div ng-show="activeTab=='ikinciTab'"> Ikinci tab icerigi </div>
</div>
{% endhighlight %}

Bir zaman sonra belki bu işi template'e de gerek kalmadan CSS ile yapabileceğiz. Ya da daha da güzeli, belki bir gün HTML'e `tab` diye bir etiket gelecek. Ama bu halinin jQuery'de click eventleri dinleyip class ekleme çıkarma yaptığımız halinden çok daha verimli olduğu aşikar.

## 2. HTML'i geliştirmenin en kolay yolu: directive'ler

Yukarıdaki örnekte "belki bir gün HTML'e `tab` etiketi gelecek" cümlesini kasıtlı kurdum, zira Angular'ın sunduğu en büyük güzelliklerden biri de HTML'i geliştirebilme(extend) özelliği. Directive adını verdikleri yapı sayesinde HTML'e yeni etiketker veya attribute'lar eklemek mümkün. Bu özellik çok önemli çünkü "web uygulamaları" geliştirmeye çalıştığımız bir dünyada "list item" etiketleriyle tablar, menüler, akordionlar, div'lerle dialog kutuları geliştirmek çok "çakma" kalıyor. Halbuki, örneğin yukarıdaki tab template'i şöyle olsa daha güzel olmaz mıydı?

{% highlight html %}
<tabs>
    <pane title="Ilk Tab"> ilk tab icerigi </pane>
    <pane title="Ikinci Tab"> Ikinci tab icerigi </pane>
</tabs>
{% endhighlight %}

HTML'e böyle bir etiket gelir mi bilinmez ama, bunu yapmak şu an [Angular ile mümkün](http://angular-ui.github.io/bootstrap/). Bu imkan web uygulaması geliştirme hızınızı katlayarak artırıyor.

## 3. Test dünyasına girmek için herşey hazır

Test Driven Development, çok yazılımcının hayali ancak çok azının harcıdır. Test yazarak geliştirmeyi gereksiz bulanlar bir yana, faydalı bulduğu halde zor geldiği için uygulamayan da çok yazılımcı var(kendimden biliyorum). Angular, bu konuda da büyük fırsatlar sunuyor. Angular'da test yazmak özendirici derecede kolay ve bol örnekli. AngularJS dokümantasyon sitesini gezerken, bütün kod örneklerinin unit ya da e2e testler ile verildiğini gördüğümde şaşırmıştım. Bu Angular ekibi ve topluluğunun test yazımına gösterdiği önemi ortaya koyuyor. Siz de front-end'de TDD'ye Angular'la çok daha pratik şekilde girebilirsiniz.

## 4. Az kod çok iş

"Write less do more" size tanıdık gelmiştir. Evet, jQuery'nin sloganı da bu ve hakikaten jQuery ile de az kod ile çok iş yapıyorsunuz. Ancak Angular'da DOM manipulasyonlarının büyük oranda template'lere taşınması ve javascript kodlarının işlevsel modüllere bölünmesi sayesinde, javascript dosyalarınız genelde 40-50 satırı geçmiyor. Örneğin, jQuery'dekinin aksine Angular'da asenkron requestlerin template'de gösterimi için callback yazma, datayı çekip template'i tekrar render etme gibi bir çok işten muafsınız. Örneğin, [$resource](http://docs.angularjs.org/api/ngResource.$resource) modülüyle bir rest kaynağından bir liste çekip göstermenin "Angularcası" şöyle:

{% highlight javascript %}
angular.module('myApp', ['ngResource']).controller('MyCtrl', function($scope, $resource) {
    $scope.refresh = function() {
        $scope.myItems = $resource('/my/items').query();
    };

    $scope.refresh();
});
{% endhighlight %}

Template:

{% highlight html %}
<ul>
    <li ng-repeat="item in myItems" ng-bind="item.name">Item adi</li>
</ul>
<p><a ng-click="refresh()">Yenile</a></p>
{% endhighlight %}

5-6 satırlık javascript kodumuzda "/my/items" adresine AJAX request yapıp sonucunu template'e "myItems" adıyla döndük. Request tamamlandığında otomatik olarak template render edildi ve sayfada listemiz göründü. Refresh fonksiyonunu her çağırdığımız -ki bu fonksiyonun nasıl çağrılacağını da javascriptte değil template'te belirtiyoruz- template yine otomatik olarak güncelleniyor.

## 5. Google güveni ve hızlı büyüyen topluluk

Belki Google [batırdığı projelerle](http://www.pinterest.com/googlegraveyard/google-graveyard/) de ün yapmış olabilir, ancak başarılı olduğu alan sayısının fazlalığı dikkate alındığında, liderliğini yaptığı bir açık kaynak projeye güvenmek için daha baştan çok büyük bir unsur elde ediyorsunuz. Bunun yanında özellikle [2013 yılı başından itibaren](https://twitter.com/muratcorlu/status/352904895944347648) müthiş bir popülariteye ulaşan Angular'ın geliştirmeye katkıda bulunan topluluğunun büyüklüğü de [Github'daki projesinin](https://github.com/angular/angular.js) hareketliliğinden görülebiliyor.

## 6. jQuery bağımsız

Sahibinden'in front-end'ini yeniden tasarlamayı düşünürken jQuery'siz bir front-end'in hayalini kuruyordum. İncelediğim alternatiflerde jQuery'siz yola devam etmenin pek mümkün olmadığını gördüğümde, Angular bir adım daha öne çıkmıştı. Angular'ın içerisinde basit ve sık kullanılan bazı jQuery özelliklerini barındıran bir [jQueryLite](http://docs.angularjs.org/api/angular.element) versiyonu var. Directive'lerde kullandığımız bu özellikler işimizi kolaylaştırıyor. Ama daha fazlası yok; CSS selector, AJAX kütüphanesi, DOM'a eleman ekleme/çıkarma, event mimarisi... Hepsi bir "Angular'ca" içinde eriyip gidiyor.

## 7. Çift yönlü değişiklik dinleme

Angular'da proje geliştirirken sizi en çok şaşırtan ve eğlendiren özellik, muhakkak bu "[two way binding](http://docs.angularjs.org/guide/dev_guide.templates.databinding)" dedikleri özellik olacaktır. Buna göre, bir değişkeniniz template ve javascript kodunuz üzerinde kullandığınız her alanda değiştikçe, bu değişken üzerinde oluşturduğunuz koşulların da otomatik olarak güncellenmesi sağlanıyor, birbirinden bağımsız alanlardaki bu değişkene ait referansların güncellenebilmesi mümkün oluyor. Değişkenleri HTML form elementlerine bağlayarak kullanıcıya anlık olarak değiştirtebiliyor veya javascript ile değiştirdiğinizde bu form elemanlarının anında güncellenmesini sağlayabiliyorsunuz. Bu özellik sayesinde, oluşturduğunuz template'ler her an canlı ve güncel kalıyor, siz javascript'te veya template üzerindeki aksiyonlarda sadece durumları(state) değiştirip, bu duruma göre şablonlarınızın otomatik olarak şekil almasını sağlayabiliyorsunuz. Bu konuyu burada ayrıntılı bir şekile anlatamayacağım ancak bir düzenleme formu örneğinin burada iyi gideceğini düşünüyorum.

HTML:
{% highlight html %}
<form ng-submit="update()">
    <p>Notunuz: <textarea ng-bind="note.content"></textarea></p>
    <button type="submit">Guncelle</button>
</form>
{% endhighlight %}

JS:
{% highlight javascript %}
$scope.note = {
    id: 1,
    content: 'Mesaj iceriginiz'
};

$scope.update = function() {
    // Burada $scope.note.content artik yeni yazilan deger
}
{% endhighlight %}

## 8. Basit ve esnek URL yönetimi

"[Tek sayfa uygulamaları](http://en.wikipedia.org/wiki/Single-page_application)" geliştirirken, uygulama içinde gezinirkenki kullanılabilirlik adına URL yönetimi önemli bir konu. Angular'ın [route modülü](http://docs.angularjs.org/tutorial/step_07) -çok gelişmiş özellikleri olmasa da- problemsiz ve basit bir şekilde URL yönetimini kotarıyor. İster HTML5 pushstate ile ister hashbang kullanarak ve bunu da browser desteğine göre otomatik olarak yapıp, tarayıcı geçmişindeki gezintiyi de destekleyen, gönderdiği eventlerle url değişimlerini takip etmeyi kolaylaştıran oldukça kararlı ve esnek bir modül. [Sahibinden Github hesabı](https://github.com/sahibinden)nda paylaştığımız [angular-router-advanced](https://github.com/sahibinden/angular-router-advanced) adlı modülümüzde bu farklı dillere özgü farklı url tanımlamaları yapma ve url'leri isimlendirme özellikleri kattığımız haliyle, uygulamada gezinme işini sıfır problemle halletmiş bulunmaktayız.

## 9. Büyüdükçe güzelleşen projeler

jQuery ile geliştirdiğimiz arayüzlerde yaşadığımız en büyük sıkıntı, büyüyen uygulamalarda kodun okunabilir ve geliştirilebilir kalmasını sağlamak konusunda harcadığımız emeğin çok fazla olması, bu kadar uğraşa rağmen genelde de başaramadığımız gerçeği. Angular'da yerli yerine oturmuş parçalar, güçlü ve temiz template yapısı, harici kütüphane gereksinimlerinin olmaması ve test edilebilir modüller, işin büyüdükçe sarpa sarmasını engelliyor. [JSDoc](http://en.wikipedia.org/wiki/JSDoc)'tan devşirme NGDoc dokümantasyon standardına kodlarınızda uyarsanız, koddan [otomatik olarak](https://github.com/m7r/grunt-ngdocs) çok başarılı dokümantasyon arayüzleri çıkarma şansına sahip olmak(ki angularjs.org da bu şekilde oluşuyor) da cabası.

## 10. Çok eğlenceli, çok karizmatik

Kod yazarken konforuna özen gösteren biri olarak, yaptığımız işi eğlenceli ve ideale yakın tutabilmek de benim için önemli bir kriter. Angular ile iş yaparken içinize sinmeyen "mecburiyetler"le pek karşılaşmıyorsunuz. Kurallar çok az ve basit, ama kapsayıcılıkları oldukça geniş. Bir şeyi ne şekilde yapmak gerektiği konusunda flu alanlar az. Dolayısıyla Angular, mimari problemlerle ve etraftan dolanmalarla uğraşmadan ve bu etraftan dolanmaların verdiği motivasyon bozukluğunu da yaşamadan seri bir şekilde ilerleme şansı veriyor.

Muhakkak bu maddeler artırılabilir, belki başkaları için buradakilerden daha öncelikli maddeler sayılabilir. Angular hakkında fikirlerinizle bu tartışmayı daha verimli hale getirebiliriz. Yorumlarınızı beklerim.