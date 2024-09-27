import cv2
import numpy as np
from unit import compute_histogram, compute_cdf, draw_histogram_


class ImageProcess:
    def __init__(self, iamge_path) -> None:
        self.image = cv2.imdecode(np.fromfile(iamge_path, dtype=np.uint8), -1)
        self.image = cv2.resize(self.image, None, fx=0.75, fy=1.0, interpolation=cv2.INTER_AREA)

    # Function to compute brightness and contrast
    def calculate_brightness_contrast(self):
        # Convert image to grayscale
        if len(self.image.shape) > 2:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image
        # Calculate brightness as the mean of the grayscale values
        brightness = np.mean(gray)
        # Calculate contrast as the standard deviation of the grayscale values
        contrast = np.std(gray)
        return brightness, contrast
    
    # Function to compute brightness and contrast using LAB color space
    def calculate_brightness_contrast_lab(self):
        # Convert the image to LAB color space
        if len(self.image.shape) > 2:
            lab = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
        else:
            lab = cv2.cvtColor(self.image, cv2.COLOR_GRAY2LAB)
        # L channel represents lightness
        L, A, B = cv2.split(lab)
        # Brightness is the mean of the L channel
        brightness = np.mean(L)

        # Contrast is the standard deviation of the L channel
        contrast = np.std(L)

        return brightness, contrast
    
    def adaptive_histogram_equalization(self):
        """
        Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to improve brightness and contrast.
        
        :return: Enhanced image.
        """
        if len(self.image.shape) == 2:
            clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(10,5))
            clahe_image = clahe.apply(self.image)
        else:
            clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(10,5))
            channel = cv2.split(self.image)
            clahe_channel = [clahe.apply(imc) for imc in channel]
            clahe_image = cv2.merge(clahe_channel)

        return clahe_image
    
    def equalize_histogram(self):
        """
        Apply histogram equalization to enhance contrast of the image

        :return: 
        """
        # self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        if len(self.image.shape) == 2: # if Gray Image
            return cv2.equalizeHist(self.image)
        elif len(self.image.shape) == 3:
            # splite RGB color space
            channels = cv2.split(self.image)
            eq_channels = [cv2.equalizeHist(ch) for ch in channels]
            # merge channel
            return cv2.merge(eq_channels)
    
    def Local_Region_Stretch(self):
        hists = cv2.calcHist([self.image], [0], None, [256], [0, 256])
        hists = hists.flatten()
        hists_cdf = np.cumsum(hists)

        scale1 = int(np.searchsorted(hists_cdf, hists_cdf[-1] * 0.333))
        scale2 = int(np.searchsorted(hists_cdf, hists_cdf[-1] * 0.667))
        
        # split images
        dark_index = (self.image <= scale1)
        mid_index = (self.image > scale1) & (self.image <= scale2)
        bright_index = (self.image > scale2)
        # Apply histogram equalization for each region
        img_equalized = np.zeros_like(self.image)

        # histogram equalization individually
        dark_hists = compute_histogram(self.image[dark_index], 0, scale1)
        dark_cdf = compute_cdf(dark_hists, 0, scale1)
        img_equalized[dark_index] = dark_cdf[self.image[dark_index]]

        mid_hists = compute_histogram(self.image[mid_index], scale1, scale2)
        mid_cdf = compute_cdf(mid_hists, scale1, scale2)
        img_equalized[mid_index] = mid_cdf[self.image[mid_index] - scale1]

        bright_hists = compute_histogram(self.image[bright_index], scale2, 256 - 1)
        bright_cdf = compute_cdf(bright_hists, scale2, 256 - 1)
        img_equalized[bright_index] = bright_cdf[self.image[bright_index] - scale2]

        return img_equalized



if __name__ == "__main__":
    ImageProcess_class = ImageProcess(r'car.jpg')

    Original_image = ImageProcess_class.image
    Local_Region_image = ImageProcess_class.Local_Region_Stretch()
    combined_image = cv2.hconcat([Original_image, Local_Region_image])
    
    cv2.imshow('Combined Image', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

