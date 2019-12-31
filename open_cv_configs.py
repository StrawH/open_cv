"""
Most frequently need function while writing open cv code

To make donkey work faster :D

Note : file still in progress
"""
import cv2
import os
import numpy as np


def read_images_in_folder(folder_path):
    """
    read every image in specific folder

    :param folder_path: images folder path in string type
    :return: an array of images
    """
    folder = os.listdir(folder_path)
    images_list = []
    for image in folder:
        image_path = os.path.join(folder_path, image)
        image_read = cv2.imread(image_path)
        gray_read = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
        images_list.append(gray_read)

    return images_list


def draw_rect_on_image(frame, x, y, w, h):
    """

    :param frame: image
    :param x: coordinate of rect in x-axis
    :param y: coordinate of rect in x-axis
    :param w: width of rect
    :param h: hight of rect
    :return: nothing
    """
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)


def put_text_on_image(frame, x, y, w, h):
    """
    putting image besides detecting rect
    :param frame: image
    :param x: coordinate of rect in x-axis
    :param y: coordinate of rect in y-axis
    :param w: width of rect
    :param h: hight of rect
    :return: nothing
    """
    cv2.putText(frame, 'Detected', (x + w + 10, y + h), 0, 0.3, (0, 255, 0))


def make_mask_for_image(frame, lower, upper):
    """
    mask of image in HSV dimension
    :param frame: image
    :param lower: lower threshold [, , , ]
    :param upper: uppper threshold [, , , ]
    :return: masked image
    """
    lower = np.array(lower)
    upper = np.array(upper)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower, upper)

    return mask

