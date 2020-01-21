from urllib.request import urlopen
from collections import Counter
import re

response = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
text_data = str(response)

regex = '<code>(.*?)</code>'
sorted_code_data = sorted(re.findall(regex, text_data))
# Show the most popular matches
print(Counter(sorted_code_data))
