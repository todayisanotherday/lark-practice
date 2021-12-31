# coding: utf-8

from lark import Lark

with open('tutorial2.lark', 'r') as f:
  exp = ''.join(f.readlines())

json_parser = Lark(exp, start='value')

text = '{"key": ["item0", "item1", 3.14]}'
result = json_parser.parse(text)
print( result.pretty() )