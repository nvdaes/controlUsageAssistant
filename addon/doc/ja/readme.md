# Control Usage Assistant #

* Author: Joseph Lee, Noelia Ruiz Martínez

フォーカスされたコントロールをどのように操作するかを見つけるのにこのアドオンを使用します。チェックボックス、エディットフィールドなどの、フォーカスされたコントロールを操作することについての短いヘルプメッセージを得るためにNVDA+Hを押します。

アドオン設定をするために、NVDAメニュー、設定(P)サブメニュー、設定(S)ダイアログ、Control Usage Assistantに行きます:

* フォーカスへの自動メッセージ: 初期状態でチェック。
* オブジェクトが実行可能な時に使用されるメッセージを入力します:
  現在のオブジェクトが、オブジェクトナビゲーションで、NVDA+エンターのようなジェスチャーを押した時に、操作可能か知るために、初期またはあなたが設定したジェスチャーを表す短いメッセージを含めることが出来ます。
* 自動メッセージの出力モードを選択: チェックボックスのこのリストで読み上げまたは点字を選べます。
* 自動メッセージのピッチを変更: このスピンボックスで、NVDAが自動メッセージを読み上げる時に、ピッチを変更するか設定出来ます(-30から+30)。

## Version 20250611.0.0

* Added copy and close buttons to messages presented in browse mode.

## Version 20240324.0.0

* Improved support for edit controls and suggestions.

## Version 2023.02.19

* The message configured for clickable objects will be reported after other
  properties.
* Compatible with NVDA 2023.1.

## バージョン 2022.07.10

* 現在のオブジェクトが実行可能かを通知する、オブジェクトナビゲーションのメッセージの設定機能を追加。

## バージョン 2022.03.27

* NVDA 2022.1以降が必要。

## バージョン 22.01

* 自動メッセージのサポートを追加。
* ブラウズモードでのリクエストメッセージのサポートを改善。

## バージョン 21.10

* このアドオンに影響する、NVDAへの変更により、NVDA 2021.2以降が必要。

## バージョン 20.10

* ヘルプメッセージが英語以外の言語で通知されるようになりました。

## バージョン 20.06

* Flake8に関して多くのコード形式の問題と可能性のあるバグを解決。
* 特定のブラウズモードのコントロールで、ヘルプを得ようとする時に、NVDAが何もしていないように見えたり、エラー音が鳴ったりすることがなくなりました。

## バージョン 20.01

* NVDA 2019.3以降が必要。

## バージョン 3.0/19.11

* バージョンのスキームを年.月.にしました。
* NVDA+Hが押された時、フラッシュメッセージの表示の代わりに、ヘルプ画面が表示されるようになりました。

## バージョン 2.5

* Python 3に互換。

## バージョン 2.1

* 新しい更新された翻訳。

## バージョン2.0

* ターミナルウィンドウを含む、より多くのコントロールのヘルプメッセージの追加。
* Microsoft ExcelおよびPowerPoint、そしてWindows
  8起動画面といった、アプリケーションの一部の領域で動作するヘルプメッセージを追加。
* バーチャルバッファドキュメント(Internet Explorer, Adobe Reader, Mozilla
  Firefox,等)で、ブラウズモードとフォーカスモードの両方のフォームで動作するヘルプメッセージを追加。
* 新しい言語: デンマーク語。

## バージョン1.0

* 最初のバージョン。

[[!tag dev stable]]
