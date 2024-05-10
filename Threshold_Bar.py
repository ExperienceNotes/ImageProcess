import os
import cv2
import numpy as np
from dataclasses import dataclass, field

root = os.getcwd()


@dataclass
class GetTrackBar:
    path: str
    image: np.ndarray = field(init=False)

    def __post_init__(self):
        # Image need Gray_image
        self.image = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
        # Set image Screen Window
        cv2.namedWindow("image")
        cv2.imshow("image", self.image)
        # Set Control Bar
        cv2.createTrackbar("type", "image", 0, 4, self.on_type)
        cv2.createTrackbar("value", "image", 0, 255, self.on_value)
        cv2.createTrackbar("adapt_Type", "image", 0, 1, self.on_adapt)

        cv2.waitKey()
        # Delete All ImageWindows
        cv2.destroyAllWindows()

    def on_type(self, a):
        model_type = cv2.getTrackbarPos("type", "image")
        value = cv2.getTrackbarPos("value", "image")
        ret, dst = cv2.threshold(self.image, value, 255, model_type)
        cv2.imshow("image", dst)

    def on_value(self, a):
        model_type = cv2.getTrackbarPos("type", "image")
        value = cv2.getTrackbarPos("value", "image")
        ret, dst = cv2.threshold(self.image, value, 255, model_type)
        cv2.imshow("image", dst)

    def on_adapt(self, a):
        adapt_Type = cv2.getTrackbarPos("adapt_Type", "image")
        if adapt_Type == 0:
            adapt_image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        elif adapt_Type == 1:
            adapt_image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.imshow("image", adapt_image)


if __name__ == '__main__':
    image_path = os.path.join(root, "Invoice.jpg")
    GetTrackBar(image_path)


