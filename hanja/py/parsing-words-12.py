import re
from more_itertools import batched


hanja = []
with open('./input.txt', 'r') as raw:
    content = raw.readlines()

for rawline in content:
#    rawline = raw.readline()
    col = rawline[:-1].split('\t')
    if not col[0]:
        continue
    hanja.append(col)

def listify(words) -> str:
    ret = ''
    words = batched(words, 4)
    #print(list(hanja))
    for row in list(words):
#        print(row)
        ret += '<tr>'
        for col in row:
            line = '<td><span class="hanja">'
            line += col[0]
#            print(col)
            line += '</span> ' + col[1]
            line += '</td>'
            ret += line
        ret += '</tr>'
    return ret

with open('./output.txt', 'w') as out:
    bulk = []
    out.write('<table>')
    for row in hanja:
        if row[0][0] == '[':
            out.write(listify(bulk))
            out.write('</table>')
            out.write('<h2>' + row[0][1:-1] + '</h2><table>')
            bulk = []
        else:
            bulk.append(row)
    out.write(listify(bulk))
    out.write('</table>')