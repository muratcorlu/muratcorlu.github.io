title: "CSS3'te :after ve :before sözde elementleri"
date: 2012-02-08 15:13
published: false
category: turkish
tags: css3, pseudo-elements

IE 6'nın ölümü ve IE 7'nin gidici olmasıyla CSS3 ve HTML5 teknolojilerini kullanma aşk ve iştiyakımıza vurduğumuz gemi gevşetmeye başladığımız güzel günlerdeyiz. Bu yazımda da sizlerle IE6 ve 7 dışındaki güncel bütün tarayıcıların desteklediği :after ve :before sözde(pseudo) elementlerinin kullanımıyla ilgili örnekleri paylaşacağım.

## Sözde element(pseudo-element) ne demek?

Sözde elementler, adı üzerinde aslında element olmayıp, element gibi davranırlar. Sözde element tanımı yaptığımızda aslında HTML dokümanına birşey eklenmez, ancak görüntüde bir farklılık olur.

## Temel sözdizimi

CSS'de basit bir :before ve :after sözde elementinin tanımlanması şu şekilde yapılıyor:

    li:before {
        content: "#. ";
    }

    li:after {
        content: ".";
    }

Bu tanımlamalar HTML dokümanındaki her liste elemanının içeriğinin önüne "#. " ve sonuna da "." karakterlerini ekler. Bu "ekleme" sadece görsel manadadır. Yani HTML DOM objesine bir ekleme yapılmaz.

content özelliği zorunludur. Eğer verilmezse diğer verilecek değerlerin de bir hükmü olmayacaktır. Ancak content değeri olarak boş bir dize (""), bir resim veya bir başka değer referansı(ileride değineceğim) verilebilir.

## CSS ile içeriğe müdahale mi?

CSS'in "görsellikle" ilgilenen ve "içeriğe bulaşmayan" bir katman olduğunu akıldan çıkarmamak gerekir. Dolayısıyla, bu sözde elementlerdeki content değeri bir "içerik" sunmak için değildir. Bir örnek verelim:

Eskiden yanyana bağlantılardan oluşan bir menüyü şu şekilde yapardık:

    <p><a href="#">Ana Sayfa</a> | <a href="#">Yazılar</a> | <a href="#">İletişim</a></p>

Bağlantıların arasındaki boru(pipe) karakterlerinin aslında semantik olarak bir anlamı yok. Tamamen görsellik adına, menü elemanlarını birbirinden ayırmak için eklediğimiz bir karakter. Semantik olarak yanlış olan bu yazımı, sonraları sırasız liste(ul) elementi ile aşağıdaki şekilde yazmaya başladık:

    <ul>
        <li><a href="#">Ana Sayfa</a></li>
        <li><a href="#">Yazılar</a></li>
        <li><a href="#">İletişim</a></li>
    </ul>

Bu yazımda aynı görüntüyü elde edebilmek için li elementlerine border-left vererek müdahale ettik. Ancak border yüksekliği boru karakterinden daha yüksek geldiği için aynı görüntüyü elde edemiyoruz. İşte burada bize :before sözde elementi yardımcı olabiliyor. "Görsellik" adına HTML'e eklediğimiz boru karakterlerini, görselliğin asıl görev alanı olan CSS'ten ekleme şansını veriyor:

    li {
        display:inline;
    }

    li:before {
        content:"| ";
    }

    li:first-child:before {
        content:"";
    }

Anlaşıldığı üzere, content değeri, siteye bir içerik(veri demek daha doğru belki) eklemek için değil. Görsel bir müdahalede bulunmak için.

## Şimdi ayrıntılar...

Öncelikle :before ve :after sözde elementlerinin tam olarak nereye ekleneceğini anlamak gerekiyor. Örneğin ```p:before``` seçicisini uyguladığınızda vereceğiniz içerik p elementinin **içeriğinin önüne** eklenecektir, p elementinin çerçevesinin dışına değil. Bir örnek görüntü herşeyi açıklayacaktır:

    <ul>
        <li>İlk madde</li>
        <li>İkinci madde</li>
        <li>Üçüncü madde</li>
    </ul>

    li {
        background-color:#efefef;
        border:solid 1px #666;
        padding:10px;
        margin:5px;
    }

    li:before {
        content:"* ";
        background-color:#ff0;
    }

    li:after {
        content:".";
        background-color:#ff0;
    }

Sonuç:

![CSS3 :before - :after örneği](/uploads/css3-before-after/yildizli-imler.png)

Gördüğünüz gibi, aslında HTML dokümanımızda satır başlarındaki * ve satır sonlarındaki . işaretleri yok. Ancak CSS :before ve :after tanımlarıyla her bir satırın başına *, sonuna da . ekledik. Konumların daha iyi belli olması için verdiğim artalan ve çerçeve renkleri sayesinde gördüğünüz gibi, :before ve :after ile eklediğimiz sözde elementler, li elementinin çerçevesi içinde, içeriğindeki metnin hemen önünde ve arkasındalar.

## Referanslar

http://coding.smashingmagazine.com/2011/07/13/learning-to-use-the-before-and-after-pseudo-elements-in-css/

