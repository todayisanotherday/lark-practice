# coding: utf-8

from lark import Lark, Transformer

class Links(Transformer):
  def links(self, tree):
    return list(tree)
  def link(self, tree):
    return list(tree)
  def url(self, token):
    return token[0].value
  def text(self, token):
    return token[0].value


with open('markdown_link.lark', 'r') as f:
  exp = ''.join(f.readlines())
parser = Lark(exp, start='links', transformer=Links(), parser='lalr')


text = '''
[Google](https://www.google.com/)
[Yahoo](https://www.yahoo.co.jp/)
[Amazon](https://www.amazon.co.jp/)
'''
result = parser.parse(text)
print(result)