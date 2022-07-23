# Kontrol Kullanım Asistanı #

* Yazar: Joseph Lee
* [Kararlı sürüm][1]ü indir
* [geliştirme sürümü][2]nü indir
* NVDA uyumluluğu: 2021.2 ve üstü

Mevcut odak hakkında kısa bir yardım mesajı dinlemek için bu eklentiyi
kullanın.  Onay kutuları, yazı alanları vb Odaktaki kontrolle nasıl
etkileşime geçeceğinizle ilgili kısa bir mesaj için NvDA+H tuşlarına basın.

Go to NVDA's menu, Preferences submenu, Settings dialog, Control Usage
Asistant category to configure add-on settings:

* Automatic messages for focus: Checked by default.
* Type the message to be used when an object can be activated: You may
  include a short message indicating the default or your configured gesture
  to know if the current object has an associated action when pressing a
  gesture like NVDA+enter in object navigation.
* Select output modes for automatic messages: This list of checkboxes allows
  to select speech and braille.
* Pitch change for automatic messages: This spin box allows to set the pitch
  change when NVDA reads automatic messages (from -30 to +30).

## Version 2022.07.10

* Added ability to set a message for object navigation, to announce if the
  current object can be activated.

## Version 2022.03.27

* Requires NVDA 2022.1 or later.

## Version 22.01

* Added support for automatic messages.
* Improved support for requested messages in browse mode.

## Sürüm 21.10

* Bu eklentiyi etkileyen NVDA'daki değişiklikler nedeniyle NVDA 2021.2 veya
  üstü gereklidir.

## Sürüm 20.10

* Yardım mesajları İngilizce dışındaki dillerde gösterilir.

## Sürüm 20.06

* Flake8 ile birçok kodlama stili sorunu ve olası hatalar çözüldü.
* NVDA, belirli tarama kipi kontrolleri için yardım almaya çalışırken artık
  hiçbir şey yapmıyormuş gibi görünmeyecek veya hata tonları çalmayacaktır.

## Sürüm 20.01

* NVDA 2019.3 veya üstü gerekli.

## Sürüm 3.0/19.11

* Sürüm şeması artık yıl.ay şeklinde
* NVDA+H'ye basıldığında, hızlı bir mesaj yerine bir yardım ekranı
  gösterilecektir.

## Sürüm 2.5

* Python3 ile uyumlu.

## Sürüm 2.1

* Yeni ve güncellenmiş çeviriler.

## Sürüm 2.0

* Terminal pencereleri dahil, daha fazla kontrol için yardım mesajı eklendi.
* Microsoft Excel ve Powerpoint ve Windows 8 başlangıç ​​ekranı gibi bazı
  uygulamalar için yardım mesajları eklendi.
* (Internet Explorer, Adobe Reader, Mozilla Firefox, vb) uygulamalar için,
  tarama ve odak kiplerine dair yardım mesajları eklendi
* Yeni dil: Danimarkaca.

## Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
