from keras.models import load_model
from PIL import Image
import numpy as np
print({0: 'akiec', 1: 'bcc', 2: 'bkl', 3: 'df', 4: 'mel', 5: 'nv', 6: 'vasc'})
#image_path = str(input("image for testing: ")) # path to your image
image_path = "actinic.jpeg"

def preprocess_image(image_path, target_size=(32, 32)):
    # Load the image and resize it to the target size
    image = Image.open(image_path)
    image = image.resize(target_size)

    # Preprocess the image
    image_array = np.array(image) / 255.0  # Scale pixel values to [0, 1]
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    return image_array

def classify_image(image_path, model):
    # Preprocess the image
    image_array = preprocess_image(image_path)

    # Make prediction
    predictions = model.predict(image_array)

    # Get the predicted label
    predicted_label = np.argmax(predictions)

    return predicted_label

# Define the custom metric functions
def top_2_accuracy(y_true, y_pred):
    return tf.keras.metrics.top_k_categorical_accuracy(y_true, y_pred, k=2)

def top_3_accuracy(y_true, y_pred):
    return tf.keras.metrics.top_k_categorical_accuracy(y_true, y_pred, k=3)

# Load the model
model = load_model("model.h5", custom_objects={"top_2_accuracy": top_2_accuracy, "top_3_accuracy": top_3_accuracy})


predicted_label = classify_image(image_path, model)

print("Predicted label:", predicted_label)
label_to_dx_mapping = skin_df_balanced[['label', 'dx']].drop_duplicates().sort_values('label').set_index('label')['dx'].to_dict()

# Print the mapping
print(label_to_dx_mapping)