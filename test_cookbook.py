import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
arr = re.split(r'[;,\s]\s*', line)

str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text1))
