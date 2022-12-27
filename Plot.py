import os
import cv2  # pip3 install opencv-python
import matplotlib.pyplot as plt
from PIL import Image


def showAll():
    # create figure
    fig = plt.figure(figsize=(20, 15));

    # reading images
    imgs = os.listdir('GrafosPnG')
    rows = len(imgs) // 3 + 1;
    i = 1;
    columns = 3
    for img in imgs:
        im = cv2.imread("GrafosPnG/{}".format(img))
        fig.add_subplot(rows, columns, i);
        plt.imshow(im);
        plt.axis('off')
        plt.title("{}".format(img));
        i += 1;
    plt.savefig('graphs.png')
    im = Image.open("graphs.png")
    im.show()

def plotGraph(num):
    nu = num.rjust(2, "0");
    im = Image.open("GrafosPnG/Grafo {}.png".format(nu));
    im.show();