# dog-breed-image-classifier

A Python-based deep learning project focused on classifying pet images, comparing model predictions, and evaluating classification results.

## About the Project

I worked on this project as part of my AI-focused Nanodegree learning journey, gaining practical experience with pretrained deep learning models, image classification, and model evaluation.

The project uses three CNN architectures—AlexNet, VGG, and ResNet—to classify pet images, compare predicted labels with expected labels, and distinguish dogs from other animals.

## My Work and Learning

Through this project, I worked with:

- Processing and organizing pet-image labels.
- Running image classification using pretrained CNN models.
- Configuring scripts through command-line arguments.
- Comparing predicted labels with expected labels.
- Evaluating model results across different architectures.
- Understanding dog-versus-non-dog classification.

This repository documents the project code and my practical learning experience. It does not imply that every component was independently developed from scratch.

## Technologies Used

- Python
- Deep Learning
- Convolutional Neural Networks (CNNs)
- Image Classification
- Command-Line Arguments

## Models Evaluated

- AlexNet
- VGG
- ResNet

## Getting Started

Clone the repository:

```bash
git clone https://github.com/samarthjain-ai/pet-image-classifier.git
cd pet-image-classifier
```

Install the required dependencies, prepare the pet-image dataset, and ensure that the dog-name file is available.

Example:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

If included in the repository, run the batch script to compare model results:

```bash
bash run_models_batch.sh
```

## Author

**Samarth Jain**

- GitHub: https://github.com/samarthjain-ai
- LinkedIn: https://www.linkedin.com/in/samarth-jain-a90b2337b
