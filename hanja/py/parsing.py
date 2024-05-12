import re
from more_itertools import batched


hanja = []
with open('input.txt', 'r') as raw:
    content = raw.readlines()

for rawline in content:
#    rawline = raw.readline()
    col = rawline[:-1].split('\t')
    data = []
    data += col[0:3]
    if len(col) > 3:
        data += col[3][1:-1]
#    print(data)
    hanja.append(data)

hanja = batched(hanja, 5)
#print(list(hanja))

with open('output.txt', 'w') as out:
    for row in list(hanja):
#        print(row)
        out.write('<tr>')
        for col in row:
            line = '<td><span class="hanja">'
            line += col[0]
#            print(col)
            if len(col) > 3:
                line += '(<span class="zh">' + col[-1] + '</span>)'
            line += '</span> ' + col[1] + ' ' + col[2]
            line += '</td>'
            out.write(line)
        out.write('</tr>')