import tensorflow as tf
from tensorflow.keras import models, layers
import matplotlib.pyplot as plt
import numpy as np

# Dataset parameters
image_size = 256
BATCH_SIZE = 32
CHANNELS = 3

# Load dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    "C:/Users/User/OneDrive/Documents/maize_disease_detection",  # Update path for maize dataset
    shuffle=True,
    image_size=(image_size, image_size),
    batch_size=BATCH_SIZE
)

# Class names
class_names = dataset.class_names
print("Class names:", class_names)

# Visualize some images
plt.figure(figsize=(10, 10))
for images, labels in dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()

# Split dataset into training, validation, and testing sets
train_size = 0.7
val_size = 0.2
test_size = 0.1

total_batches = tf.data.experimental.cardinality(dataset).numpy()
train_ds = dataset.take(int(total_batches * train_size))
val_test_ds = dataset.skip(int(total_batches * train_size))
val_ds = val_test_ds.take(int(total_batches * val_size))
test_ds = val_test_ds.skip(int(total_batches * val_size))

print(f"Training dataset size: {len(list(train_ds))} batches")
print(f"Validation dataset size: {len(list(val_ds))} batches")
print(f"Testing dataset size: {len(list(test_ds))} batches")

# Preprocess the datasets (Resize, Rescale, Batch)
AUTOTUNE = tf.data.AUTOTUNE

def preprocess(ds):
    return ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)

train_ds = preprocess(train_ds)
val_ds = preprocess(val_ds)
test_ds = preprocess(test_ds)

# Data augmentation
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
])

# Build the model
input_shape = (image_size, image_size, CHANNELS)
n_classes = len(class_names)

model = models.Sequential([
    layers.InputLayer(input_shape=input_shape),
    data_augmentation,
    layers.Rescaling(1.0 / 255),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dropout(0.5),  # Regularization
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),  # Regularization
    layers.Dense(n_classes, activation='softmax')
])

model.summary()

# Compile the model
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)

# Train the model
EPOCHS = 15
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_ds)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Plot accuracy and loss curves
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(range(EPOCHS), acc, label='Training Accuracy')
plt.plot(range(EPOCHS), val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(range(EPOCHS), loss, label='Training Loss')
plt.plot(range(EPOCHS), val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')

plt.show()

# Predict function
def predict(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

plt.figure(figsize=(15, 15))
for images, labels in test_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        img = images[i].numpy().astype("uint8")
        predicted_class, confidence = predict(model, img)
        actual_class = class_names[labels[i].numpy()]

        plt.imshow(img)
        plt.title(f"Actual: {actual_class},\nPredicted: {predicted_class},\nConfidence: {confidence}%")
        plt.axis("off")
plt.show()

# Save the model
model.save("C:/Users/User/OneDrive/Documents/maize_disease_detection/model/maize_modelv1.0.h5")
print("Model saved successfully!")
