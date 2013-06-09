import sys
import re

f = open(sys.argv[1], "rU")

s = f.read()
f.close()
s = re.sub(r'(\n|\t|"!"|"?")', ' ', s)
s = s.lower()

words = s.split()

d = {}

for w in words: 
    if d.has_key(w):
        d[w] += 1
    else: 
        d[w] = 1


sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "all: %d" % len(d)

i = 0
for k in sored_keys:
    if i == 20:
        break
    print k, ": ", d[k]
    i += 1



