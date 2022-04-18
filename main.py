import pyautogui  # pip install pyautogui
from PIL import Image,ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return

def chake(data):
    for i in range(300, 325):
        for j in range(175, 200):
            if data[i,j] == 255:
                return True
            else:
                return False
            # return True
def isCollideD(data):
    if chake(data):
        # print(chake(data))
        # Draw the rectangle for cartus
        for i in range(380, 430):
            for j in range(425, 490):
                if data[i, j] < 100:
                    hit("up")
                    return

            # Draw the rectangle for birds

        for i in range(300, 325):
            for j in range(375, 400):
                if data[i,j] < 100:
                    hit("down")
                return
        # return
    # --------------------------
    else:
        # print(chake(data))
        # Draw the rectangle for cartus
        for i in range(380, 430):
            for j in range(425, 490):
                if data[i, j] > 100:
                    hit("up")
                    return

            # Draw the rectangle for birds

        for i in range(300, 325):
            for j in range(375, 400):
                if data[i,j] > 100:
                    hit("down")
                return
        # return

# def isCollideN(data):
#     # if chake(data):
#         # Draw the rectangle for cartus
#         for i in range(330, 380):
#             for j in range(425, 490):
#                 if data[i, j] > 100:
#                     hit("up")
#                     return
#
#             # Draw the rectangle for birds
#
#         for i in range(300, 325):
#             for j in range(375, 400):
#                 if data[i,j] > 100:
#                     hit("down")
#                 return
#
#         return

if __name__ == '__main__':
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollideD(data)
        # isCollideN(data)


        # print(asarray(image))
        # Draw the rectangle for cartus
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    #     # Draw the rectangle for cartus
    # for i in range(580, 630):
    #     for j in range(425, 490):
    #         data[i,j] = 150
    #     # Draw the rectangle for birds
    # for i in range(300, 325):
    #     for j in range(375, 400):
    #         data[i,j] = 150
    #  # chaking
    # for i in range(700, 725):
    #     for j in range(175, 200):
    #         # data[i,j] = 150
    #         data[i,j] = 255
    #
    # image.show()

