# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for z in attrs: print('->', z[0], '>', z[1])

parser = MyHTMLParser()
for _ in range(int(input())): parser.feed(input())