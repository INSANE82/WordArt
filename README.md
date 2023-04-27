# WordArt

IPAフォントのゴシック体を使用していますので、コード1行目を実行してください(Linux系のみ)。  
windowsは[こちら](https://moji.or.jp/ipafont/ipaex00401/)からダウンロードしてください。インストール方法は[こちら](https://moji.or.jp/ipafont/installation/)

This code use fonts-ipafont-gothic so you need to install the font(only linux-users). The command in this code row1 can be used to install the font. But windows-users need to download zip-file(font packages). [download page](https://moji.or.jp/ipafont/ipaex00401/) / [how to install page](https://moji.or.jp/ipafont/installation/)  
  
コード内で使用しているライブラリは下記のコマンドでインストールできます。
```
pip install matplotlib
```
　&
```
pip install Pillow
```
## How to user??

You need to edit row92(display word) & row96(make up display word)

## How to edit font size??

2nd and 4th arg of "str2img"(row92) are font size of display word.
