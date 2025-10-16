import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Step 1: Load the trained model
model = tf.keras.models.load_model('potato_disease_model.h5')

# Step 2: Define classes
classes = ['Early_Blight', 'Healthy', 'Late_Blight']

# Step 3: Load your image
# Replace 'sample_leaf.jpg' with your image path
img_path = 'image.png'
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0  # normalize

# Step 4: Make prediction
prediction = model.predict(img_array)
predicted_class = classes[np.argmax(prediction)]

print(f"🍀 Predicted Class: {predicted_class}")
