# Image Processing Toolkit
The Image Processing Toolkit is a lightweight and extensible Python library designed to simplify image processing tasks. It currently includes a few essential functions for `calculating image brightness and contrast`, as well as methods for `automatically adjusting image contrast using various enhancement techniques`.Future updates will bring additional tools for advanced image manipulation, feature extraction, and filtering.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

The **Image Processing Toolkit** is designed to help you calculate image brightness and contrast, and apply various contrast enhancement techniques. These include adaptive histogram equalization, simple histogram equalization, and local region-based stretching.

## Features
- **Brightness & Contrast Calculation**: Compute the brightness and contrast of an image.
- **Contrast Limited Adaptive Histogram Equalization (CLAHE)**: Enhances image contrast using CLAHE, a variation of AHE that limits contrast amplification.
- **Histogram Equalization**: Globally adjust the image contrast using traditional histogram equalization.
- **Local Region Stretching**: Improve the image contrast by stretching the histogram in local regions.

## Installation

### 1. Clone the repository: 
```bash=
git clone https://github.com/yourusername/image-processing-toolkit.git
cd your-project
```
### 2. If you are on Windows and have CUDA installed, you can use the provided .bat script for setup:
```bash=
create_env.bat
```
### 3. For other systems, follow the steps below to install dependencies:
```bash=
pip install -r requirements.txt
```

## Usage

### 1. Calculate Brightness and Contrast
Use the calculate_brightness_contrast function to compute the brightness and contrast of an image.
```python=
from ImageProcess import ImageProcess

Image_class = ImageProcess(r'./car.jpg')
brightness, contrast = Image_class.calculate_brightness_contrast()
```

### 2. CLAHE (Contrast Limited Adaptive Histogram Equalization)
Apply CLAHE to enhance image contrast by limiting contrast amplification to avoid noise.
```python=
from ImageProcess import ImageProcess

Image_class = ImageProcess(r'./car.jpg')
clahe_image = Image_class.adaptive_histogram_equalization()
```

### 3. Histogram Equalization
Use the equalize_histogram function to globally enhance image contrast.
```python=
from ImageProcess import ImageProcess

Image_class = ImageProcess(r'./car.jpg')
equalizeHist_image = Image_class.equalize_histogram
```

### 4. Local Region Stretching
Apply local region stretching to adjust the contrast in different parts of the image.
```python=
from ImageProcess import ImageProcess

Image_class = ImageProcess(r'./car.jpg')
Local_Region_image = Image_class.Local_Region_Stretch
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Reference

- https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
- https://github.com/lxcnju/histogram_equalization/tree/master