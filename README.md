# 🥔 Potato Disease Detection using CNN & Streamlit

A deep learning-based web application that detects **potato leaf diseases** from uploaded images.  
Built using **TensorFlow**, **Keras**, and **Streamlit**, this project helps farmers and researchers quickly identify diseases such as **Early Blight**, **Late Blight**, and **Healthy Leaves**.

---

## 🚀 Features

- 🧠 **Deep Learning Model:** Trained using Convolutional Neural Networks (CNN)
- 📸 **Image Upload:** Upload a leaf image directly from your device
- ⚡ **Real-time Prediction:** Get instant classification results
- 🎨 **Streamlit Interface:** Simple, user-friendly UI
- 💾 **Model Persistence:** Saved as `potato_disease_model.h5` for easy reuse

---

## 🧩 Tech Stack

| Category | Tools |
|-----------|--------|
| **Language** | Python |
| **Libraries** | TensorFlow, Keras, NumPy, Matplotlib |
| **Frontend** | Streamlit |
| **Environment** | VS Code / Streamlit Cloud |

---

## 📂 Project Structure

potato_disease_detection/
│
├── dataset/ # Training and validation images (optional)
│ ├── Potato___Early_blight/
│ ├── Potato___Late_blight/
│ └── Potato___Healthy/
│
├── potato_disease_model.h5 # Saved CNN model
├── train_model.py # Script to train and save the model
├── predict_leaf.py # Local testing script for predictions
├── app.py # Streamlit web app
├── requirements.txt # Dependencies
└── README.md # Project documentation


🧠 Model Summary

The CNN model uses:

Conv2D and MaxPooling2D layers for feature extraction

Flatten and Dense layers for classification

ReLU activation for non-linearity

Softmax activation in the output layer for multi-class classification

Training achieved an accuracy of around 93% on test data.


🌐 Deployment

You can deploy this app on Streamlit Cloud:

Push your code (excluding large files and venv/) to GitHub.

Go to Streamlit Cloud
.

Connect your GitHub repo and select app.py as the entry point.

Add dependencies to requirements.txt.

❤️ Acknowledgements

Dataset: PlantVillage Dataset (Kaggle)

Frameworks: TensorFlow, Streamlit

Inspiration: Supporting smart agriculture through AI


“Turning leaves into data, and data into diagnosis.”
