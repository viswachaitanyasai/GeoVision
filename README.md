# GeoVision

**GeoVision** is an image classification project built using FastAI that identifies countries based on map. It uses a ResNet18 model for transfer learning and fine-tunes it to classify countries. The project currently supports identifying maps of five countries: China, France, India, Japan, and the USA.

## Features

- **Image Classification**: Classifies images of maps into predefined country categories.
- **Transfer Learning**: Leverages a pre-trained ResNet18 model for fast and accurate learning.
- **Corrupt Image Handling**: Automatically verifies and removes any corrupted images from the dataset.
- **Probabilistic Output**: Provides the classification along with the probability of each country.

## Dataset

The dataset consists of urban maps from various cities across five countries:

- **India (120 images)**:
  - Mumbai
  - Delhi
  - Bangalore
  - Kolkata
  - Chennai
  - Hyderabad

- **China (70 images)**:
  - Shanghai
  - Beijing
  - Chongqing
  - Guangzhou

- **Japan (70 images)**:
  - Tokyo
  - Yokohama
  - Osaka
  - Nagoya

- **USA (70 images)**:
  - New York City
  - Los Angeles
  - Chicago
  - Houston

- **France (70 images)**:
  - Paris
  - Marseille
  - Lyon
  - Toulouse

You can access the dataset via [Kaggle](https://www.kaggle.com/datasets/viswachaitanyasai/urban-country-maps).

You can access the trained model via [Kaggle](https://www.kaggle.com/models/viswachaitanyasai/country-identifier)

## Project Setup

### Prerequisites

Make sure you have the following dependencies installed:

- Python 3.8+
- FastAI
- PyTorch
- Pillow (for image handling)

You can install the necessary libraries via:

```bash
pip install fastai torch pillow

```

### Dataset
Place your image dataset in a directory called map_images. Each image should be inside a folder named after the country it represents. For example:
```bash
map_images/
│
├── china/
│   ├── china_map1.png
│   ├── china_map2.png
│   └── ...
│
├── france/
│   ├── france_map1.png
│   ├── france_map2.png
│   └── ...
│
└── ...
```
### Results

The model was trained for 5 epochs with the following results:

- **Accuracy**: 87.5%
- **Final Training Loss**: 0.1942
- **Final Validation Loss**: 0.3274
- **Final Error Rate**: 0.125
