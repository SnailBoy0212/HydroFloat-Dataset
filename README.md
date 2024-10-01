# HydroFloat Dataset

Welcome to the GitHub repository of the HydroFloat Dataset. This dataset features images of six common types of floating debris: plastic bottles, plastic bags, cans, dead fish, water hyacinths, and foam. It is designed to aid the development of machine learning models for environmental monitoring and cleanup.
## Data Collection Method

The HydroFloat Dataset was compiled using two primary methods of data collection:

1. **Manual Photography**:
   - Location: Lakes within Huai'an City.
   - Method: Photographs were taken of the lake surfaces from various angles and under different weather conditions to capture real-time scenes.
   - Objective: To gather a diverse set of images representing typical floating debris.

2. **Sourced from Public Datasets**:
   - Criteria: High-quality images with low similarity to each other were selected from publicly available datasets.
   - Objective: To enrich the dataset with a variety of examples not captured through manual photography.

### Data Curation Process
After collecting the images, a rigorous selection process was conducted to ensure the quality of the dataset:
- **Image Screening**: Images with insufficient clarity or duplicates were removed.
- **Final Dataset**: A total of 4,497 images were retained in the dataset, ensuring a high standard of image quality and diversity.

This meticulous approach to data collection and curation ensures that the HydroFloat Dataset is reliable for training and testing machine learning models aimed at environmental monitoring and debris classification.

## Dataset Content
- **Total Images**: 4497
- **Categories**: Plastic bottles, plastic bags, cans, dead fish, water hyacinths, foam
- **Resolution**: Each image is 640x640 pixels
- **Format**: JPEG

## File Structure

HydroFloat/ │ ├── images/ # Image files │ ├── train/ # Training set images │ ├── test/ # Test set images │ └── val/ # Validation set images └── labels/ # Label files ├── train/ # Training set labels ├── test/ # Test set labels └── val/ # Validation set labels


## Usage Example
Here is a simple example of how to load and use the HydroFloat Dataset in Python:
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load an example image from the training set
img = mpimg.imread('HydroFloat/images/train/sample.jpg')
imgplot = plt.imshow(img)
plt.show()
```


Contact Information
If you have any questions, please contact us at:

Email: 13834467383@163.com
