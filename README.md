# lark-practice
larkの練習用リポジトリ

## link
- https://github.com/lark-parser/lark
  - リポジトリ 
- https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md
  - JSONを解析するチュートリアル 
- https://lark-parser.readthedocs.io/en/latest/
  -  ドキュメント
- https://github.com/lark-parser/lark/blob/master/docs/_static/lark_cheatsheet.pdf
  - チートシート
- https://www.lark-parser.org/ide/
  - Larkを試す

## markdownのリンクを試す

`[]()` からリンクとテキストを抜き出すだけのもの。記号周りをその場しのぎで定義しているので使いようはない。

```bash
$ python markdown_link.py
[['Google', 'https://www.google.com/'], ['Yahoo', 'https://www.yahoo.co.jp/'], ['Amazon', 'https://www.amazon.co.jp/']]
```

実行方法。

```bash
$ pipenv shell
$ cd markdown
$ python markdown_link.py
```