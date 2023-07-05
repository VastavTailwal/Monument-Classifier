# Monument Classifier using Convolutional Neural Networks

This project is an image classifier implemented in Python using Convolutional Neural Networks (CNNs) to identify different monuments from input images. The goal is to create a model that can accurately classify images of various monuments based on their visual features.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)

## Introduction

The Monument Classifier is a deep learning project aimed at recognizing and classifying different monuments from images. It utilizes the power of Convolutional Neural Networks (CNNs), which are specifically designed for image processing tasks. By training the model on a labeled dataset of monument images, the classifier can learn to distinguish between different monuments and predict their respective classes.

This project serves as a starting point for building a monument classifier and can be extended and customized to fit specific requirements.

## Installation

To use the Monument Classifier, follow these steps:

1. Clone the repository: git clone https://github.com/VastavTailwal/Monument-Classifier.git

2. Navigate to the project directory: cd monument-classifier

3. Download the pre-trained model weights or train the model using the provided dataset (see [Training](#training)).

4. Ensure you have a dataset of monument images for testing and evaluation.

## Usage

To classify monument images using the trained model, follow these steps:

1. Place your test images in a separate directory (e.g., `test_images/`).

2. Run the specified notebook cell.

3. The classifier will process each image in the directory and display the predicted class labels along with their confidence scores.

## Dataset

The dataset used for training and evaluating the Monument Classifier consists of labeled images of different monuments.

Ensure that each class has its own subdirectory within the `dataset/` directory, and the images are named accordingly.

## Model Architecture

The Monument Classifier employs a CNN architecture to process the input images and make predictions. The specific architecture details can be found in the source code of the project.

## Training

To train the Monument Classifier on your own dataset, follow these steps:

1. Organize your dataset according to the structure mentioned in the [Dataset](#dataset) section.

2. Modify the configuration variables to suit your requirements, such as the number of epochs, batch size, and model hyperparameters.

3. Run the training script provided in the notebook. The script will load the dataset, split it into training and validation sets, and train the model using the specified configuration.

4. After training, the model weights will be saved as `model.h5` for future use.

## Evaluation

To evaluate the performance of the Monument Classifier, use the following steps:

1. Ensure you have a separate dataset of test images (see [Dataset](#dataset)).

2. Modify the configuration variables in the `evaluate.py` file if necessary.

3. Run the evaluation script provided in the notebook.

The script will load the trained model, process the test images, and display the accuracy of the classifier.

## Contributing

Contributions to the Monument Classifier project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the project's GitHub repository. If you would like to contribute code, please fork the repository, create a new branch, commit your changes, and open a pull request.
