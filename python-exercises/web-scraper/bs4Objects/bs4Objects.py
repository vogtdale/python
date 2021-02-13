from bs4 import BeautifulSoup

# consider the folliwing HTML code 
html_doc = """
<html>
<head>
<title>Document</title>
</head>
<body>
<p class="title"><b>The Dormouse's Story</b></p>
<p class="story">Once upon a time there were three sisters, there names were: 
<a href="https://www.google.com" class="sister">Elsie</a>, 
<a href="https://www.msn.fr" class="sister">Lacie</a> and
<a href="https://www.youtube.com
" class="sister">Plouf</a>;
and they lived at the bottom of a well.
</p>

<p class="story">...</p>
<b class="boldest"> Extremely Bold</b>
<blockquote class="boldest"> Extremely Bold</blockquote>
<b>Test 1</b>

</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, 'lxml')

# print out nicely formated HTML
"""print(soup.prettify())"""

# Tags
print(soup.find_all("p"))
