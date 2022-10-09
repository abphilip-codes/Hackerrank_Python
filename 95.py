# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for a, b in attrs: print(f"-> {a} > {b}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for a, b in attrs: print(f"-> {a} > {b}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

parser = MyHTMLParser()
for _ in range(int(input())): parser.feed(input())
parser.close()