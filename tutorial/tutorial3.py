# coding: utf-8
# Tranformerを使ってJSONを解析してdictに変換
# 文法はtutorial2.txtを流用

from lark import Transformer, Lark

class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

with open('tutorial2.lark', 'r') as f:
  exp = ''.join(f.readlines())

json_parser = Lark(exp, start='value')
text = '{"key": ["item0", "item1", 3.14], "key2": null}'
tree = json_parser.parse(text)
result = TreeToJson().transform(tree)

print(result)