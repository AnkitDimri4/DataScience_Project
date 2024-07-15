# DataScience_Project
 The repository contains projects related to data science.
---
# Neural Network for Image Recognition of Letters A, B, and C
This project demonstrates a simple neural network trained to recognize images of letters A, B, and C using Python and NumPy.
## Dataset
The dataset consists of three images: 
- **A**: Represented as a list *a*
- **B**: Represented as a list *b*
- **C**: Represented as a list *c*
Each letter is encoded as a binary image in a 1-dimensional NumPy array format.
## Labels
The labels for the images are:
- A: [1, 0, 0]
- B: [0, 1, 0]
- C: [0, 0, 1]
## Neural Network Architecture
- **Input Layer**: 30 neurons (corresponding to 30 pixels in each image)
- **Hidden Layer**: 5 neurons, activated using the sigmoid function
- **Output Layer**: 3 neurons (one for each letter), activated using the sigmoid function
## Training
The neural network is trained using backpropagation with gradient descent -
- **Loss Function**: Mean Squared Error (MSE)
- **Activation Function**: Sigmoid
Training Parameters:
- Learning Rate (α): 0.1
- Epochs: 100
## Results
After training for 100 epochs, the neural network achieved an accuracy of 95.67% on the training dataset.
## Usage
To use the trained model for prediction:
```python
predict(x[2], w1, w2)  # Image is of letter C
predict(x[1], w1, w2)  # Image is of letter B
predict(x[0], w1, w2)  # Image is of letter A
```
## Visualizations

### Accuracy over Epochs
![Accuracy Plot](https://github.com/user-attachments/assets/57920e45-5a5c-444d-825b-7e8b0cfb0c36)

### Loss over Epochs
![Loss Plot](https://github.com/user-attachments/assets/6e8cb53b-790b-46be-9478-ea28b0ea96c1)

---
