import re

N = int(input())
pat = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
#pat = r'<a href="(.*?)".*?>(.*?)(?=<\/)'
# the ? in (.*?) makes the preceding quatifier lazy

for i in range(N):
	Test_String = input()

	res = re.findall(pat, Test_String)
	for link, title in res:
		print("{},{}".format(link, title.strip()))
'''
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

<a href="/wiki/File:Female_and_male_Pardalotus_punctatus.jpg" title="About this image"><img alt="About this image" src="//bits.wikimedia.org/static-1.22wmf7/extensions/ImageMap/desc-20.png" style="border: none;" /></a></div>

'''

