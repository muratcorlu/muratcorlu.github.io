title: "Python ile TC Kimlik Numarası doğrulama"
date: 2012-03-11 22:48
categories: turkish
tags: python, gist

Merak edip TC Kimlik no algoritmasını araştırdığımda aşağıdaki kurallara [ulaştım](http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi):

{% blockquote %}
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
{% endblockquote %}

Kütüphanemde bulunması için bu kurallara göre bir Python doğrulama metodu yazayım dedim. Ortaya şöyle birşey çıktı:

{% gist 2018156 %}

Herhangi bir hata ya da eksik gördüğünüzde iletin lütfen.

