from flask import Flask, request
import numpy as np
import matplotlib.pyplot as plt
import StringIO
import pandas as pd


def radarplot(labels, data, title='defaultname'):
    dataLenth = len(labels)
    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'bo-', linewidth=2)
    ax.fill(angles, data, facecolor='r', alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="Ubuntu Mono")
    ax.set_title(title, va='bottom', fontproperties="Ubuntu Mono")
    ax.set_rlim(0, max(data))
    ax.grid(True)
    io = StringIO.StringIO()
    plt.savefig(io, format="png")
    plt.close('all')
    return '<img src="data:image/png;base64,%s"/>' % io.getvalue().encode("base64").strip()


def boxplot(nums, quantity, title):
    nums = partition(nums, quantity)
    print nums
    df = pd.DataFrame(nums,
                      columns=title)
    df.boxplot()
    bio = StringIO.StringIO()
    plt.savefig(bio, format="png")
    plt.close('all')
    return '<img src="data:image/png;base64,%s"/>' % bio.getvalue().encode("base64").strip()


def partition(lst, partition_size):
    if partition_size < 1:
        partition_size = 1
    return [
        lst[i:i + partition_size]
        for i in range(0, len(lst), partition_size)
    ]


app = Flask(__name__)


@app.route('/radar', methods=['POST'])
def radar():
    data = []
    tmpdata = request.form.getlist('data')
    print tmpdata
    for num in tmpdata:
        data.append(float(num))
    print data
    labels = request.form.getlist('labels')
    title = request.form['title']
    title = str(title)
    return radarplot(labels, data, title)


@app.route('/box', methods=['POST'])
def box():
    nums = []
    tmpnums = request.form.getlist('nums')
    print tmpnums
    for num in tmpnums:
        nums.append(float(num))
    print nums
    quantity = request.form['quantity']
    quantity = int(quantity)
    title = request.form.getlist('title')
    print title
    return boxplot(nums, quantity, title)


if __name__ == '__main__':
    app.run()
