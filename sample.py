# coding=utf-8
import requests, random

a = list()
label = list()

for i in range(26):
    a.append(random.uniform(150, 200))
    label.append(chr(ord('a') + i))

data_info_radar = {'data': a, 'labels': label, 'title': 'plottest'}
r = requests.post("http://127.0.0.1:5000/radar", data=data_info_radar)
fil = open(str(id) + '.html', 'wb')
fil.write(r.text)
fil.close()
print r.text

data_info_box = {'nums': ['123', '131', '175', '115', '173', '103'], 'quantity': '3',
                 'title': ['first', 'second', 'third']}
j = requests.post("http://127.0.0.1:5000/box", data=data_info_box)
fil = open(str(id) + '.html', 'wb')
fil.write(j.text)
fil.close()

