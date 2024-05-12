import re
from more_itertools import batched


hanja = []
with open('./input.txt', 'r') as raw:
    content = raw.readlines()

for rawline in content:
#    rawline = raw.readline()
    col = rawline[:-1].split('\t')
    hanja.append(col)

hanja = batched(hanja, 5)
#print(list(hanja))

with open('./output.txt', 'w') as out:
    for row in list(hanja):
#        print(row)
        out.write('<tr>')
        for col in row:
            line = '<td><span class="hanja">'
            line += col[1]
#            print(col)
            line += '</span> ' + col[0]
            line += '</td>'
            out.write(line)
        out.write('</tr>')