import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split


# Load and preprocess the dataset
def load_and_preprocess_data(dataset_dir):
    data = []
    labels = []

    for class_name in class_names:
        class_dir = os.path.join(dataset_dir, class_name)
        for filename in os.listdir(class_dir):
            if filename.endswith(".png"):  # Assuming image files are in JPG format
                img = keras.preprocessing.image.load_img(
                    os.path.join(class_dir, filename), target_size=(150,150)
                )
                img_array = keras.preprocessing.image.img_to_array(img)
                data.append(img_array)
                labels.append(class_names.index(class_name))

    data = np.array(data)
    labels = np.array(labels)
    return data, labels





if __name__ == "__main__":
    # Define your dataset directory
    dataset_dir = "C:/Users/aiskr/Repositories/DPB/mkfold/fold1/train/40X"

    # Define the class labels
    class_names = ["benign", "malignant"]

    # Define hyperparameters
    batch_size = 32
    epochs = 10
    data, labels = load_and_preprocess_data(dataset_dir)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.2, random_state=42)

    # Create a CNN model
    model = Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150,150, 3)),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ])

    # Compile the model
    model.compile(optimizer="adam", loss="binary_crossentropy",
                metrics=["accuracy"])

    # Train the model
    model.fit(X_train, y_train, batch_size=batch_size,
            epochs=epochs, validation_split=0.1)

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {test_accuracy}")

    # Make predictions on new images
    # new_image = load_and_preprocess_new_image("path/to/new_image.jpg")
    # prediction = model.predict(np.expand_dims(new_image, axis=0))
    # print("Predicted class:", class_names[int(np.round(prediction[0])))

    # Save or serialize the model for later use
    model.save("breast_cancer_classifier_model.h5")
    model.save("breast_cancer_classifier_model.keras")
