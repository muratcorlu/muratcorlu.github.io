title: Mac OSX Lion'da SSHFS kullanımı
date: 2012-03-04 19:28
category: turkish
tags: OSX

Mac OS Snow Leopard sürümünde Macports yardımıyla kolayca kurup kullandığımız(port install sshfs) sshfs uygulamasını Lion'da kullanmakta sıkıntılar yaşıyoruz zira sshfs'in kullandığı MacFUSE uygulamasının Lion uyumlu bir versiyonu çıkmadı. Lion'da sshfs ile uzak bir noktayı bilgisayarınıza mount etmek istediğinizde aşağıdaki hatayı alıyorsanız, az sonra ileteceğim çözüm sizin de işinizi görecektir:

    this MacFUSE library version is incompatible with the MacFUSE kernel extension

SSHFS'i Lion'da sorunsuz olarak kullanabilmek için MacFUSE'un varisi Fuse for OSX'i kullanabilirsiniz. [Kendi sayfasından](http://osxfuse.github.com/) son versiyonunu indireceğiniz Fuse for OSX uygulamasını kurduktan sonra, SSHFS'in Fuse for OSX ile kullanabileceğiniz versiyonunun paketini [github'daki downloads sayfasından](https://github.com/osxfuse/sshfs/downloads) indirip kurarak sorunsuz şekilde kullanabilirsiniz.

Faydası olması dileğiyle...

