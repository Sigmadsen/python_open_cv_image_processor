import cv2


def make_grayscale():
    image = cv2.imread('data/input/1.jpg', cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    cv2.imwrite('data/output/1.jpg', image)


if __name__ == '__main__':
    make_grayscale()
