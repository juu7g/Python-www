# Python-www
Web操作ライブラリ

## 概要 Description
Web操作ライブラリ

## 内容 Contents

- WebSiteクラス `en` ScrolledFrame class
	- get_html()メソッド `en` wrapped_grid() class method
	- get_text_from_html()メソッド
	- output_to_file()メソッド

## WebSiteクラス

### メソッド Method
- `get_html(self, url:str)`  
	- 引数
		- `url`：url
	- 戻り値
		- str：html
		- str：エラー内容(エラーがない時は空文字)
	- 特徴
		- 指定したurlのhtml文書を取得します  
		- エラーがあった場合、エラー内容を返します

- `get_text_from_html(self, html:str, tag:str="div", cls:str="hatenablog-entry")`  
	- 引数
		- `html`：html文書を指定
		- `tag`：テキストを取得する対象のタグ(これ以下の文書が取得対象)
		- `cls`：テキストを取得する対象のクラス
	- 戻り値
		- str：テキスト
	- 特徴
		- 指定したhtml文書からテキストを取得します
		- clsクラスを持つtagタグの子孫のテキストを取得します

- `output_to_file(self, text:str, ext:str="txt")`  
	- 引数
		- `text`：テキスト
		- `ext`：ファイル拡張子
	- 特徴
		- textをファイルに出力します
		- ファイル名は兄弟のtestsディレクトリに「html_yymmddHHMM.txt」

## 依存関係 Requirement

- Python 3.8.5  
- requests 2.31.0
- beautifulsoup4 4.12.2

## プログラムの説明サイト

- [gTTSとmpg123で作るテキスト読み上げアプリ【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/text-to-speech/speech-text)  


## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。 