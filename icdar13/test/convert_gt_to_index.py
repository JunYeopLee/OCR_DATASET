#import re
#d = open('dict.txt','r')
#dic = eval(d.readline())
#d.close()
#dic_index = 0
#with open('gt.txt', 'r') as f, open('gt_index.txt','w') as o:
#    while True:
#        line = f.readline()
#        if not line: break
#        filename, label = line.strip().split(', ')
#        label = label.replace("\"","")
#        if not re.match('^[a-zA-Z0-9_]+$', label) or len(label) <= 2:
#            continue
#        try:
#            indices = [str(dic[c]) for c in label]
#        except:
#            continue
#        o.write(filename + '\t' + ' '.join(indices) + '\n')
#    print(len(dic))

import re
import sys

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
dic = {}
for i, c in enumerate(charset):
    dic[c] = i

#with open('annotation_%s.txt.clr'%mode, 'r') as f, open('annotation_%s_index.txt'%mode,'w') as o, open('dict.txt', 'w') as d:
with open('gt.txt', 'r') as f, open('gt_index.txt','w') as o, open('dict.txt','w') as d:
    while True:
        line = f.readline()
        if not line: break
        filepath, label = line.strip().split(', ')
        label = label.replace("\"", "")
        if not re.match('^[a-zA-Z0-9_]+$', label) or len(label) <= 2:
            continue
        indices = [str(dic[c]) for c in label]
        o.write(filepath + '\t' + ' '.join(indices) + '\n')
    print(len(dic))
    d.write(str(dic))

