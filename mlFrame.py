import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
from keras._tf_keras.keras.applications import ResNet50
from keras._tf_keras.keras.layers import Dense, GlobalAveragePooling2D
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator



#preprocess
def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=5)
    image = tf.image.resize(image, [224, 224])
    image = tf.cast(image, tf.float32) / 255.0
    return image

def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)

def load_dataset(directory):
    image_paths = []
    labels = []
    class_names = sorted(os.listdir(directory))  # Get sorted list of class names
    class_indices = {name: index for index, name in enumerate(class_names)}
    for label_dir in class_names:
        label_path = os.path.join(directory, label_dir)
        if os.path.isdir(label_path):
            for image_name in os.listdir(label_path):
                image_paths.append(os.path.join(label_path, image_name))
                labels.append(class_indices[label_dir])
    return image_paths, labels

def Start():
    data_dir = 'C:/Users/radul/Desktop/licenta/ML'
    image_paths, labels = load_dataset(data_dir)
    num_classes = 5

        #model def
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


        #train 

    datagen = ImageDataGenerator(
            rescale=1./255,
            zoom_range=0.2,
            horizontal_flip=True,
            validation_split=0.2
        )

    train_generator = datagen.flow_from_directory(
            data_dir,
            target_size=(224, 224),
            batch_size=64,
            class_mode='categorical',
            subset='training'
        )

    validation_generator = datagen.flow_from_directory(
            data_dir,
            target_size=(224, 224),
            batch_size=64,
            class_mode='categorical',
            subset='validation'
        )

    model.fit(
            train_generator,
            steps_per_epoch=train_generator.samples // train_generator.batch_size,
            validation_data=validation_generator,
            validation_steps=validation_generator.samples // validation_generator.batch_size,
            epochs=15
        )



    train_generator = datagen.flow_from_directory(
            data_dir,
            target_size=(512, 512),
            batch_size=10,  
            class_mode='categorical',
            subset='training'
        )

        # Get a batch of images and labels
    images, labels = next(train_generator)
        
    loss, accuracy = model.evaluate(validation_generator)
    print(f'Validation Accuracy: {accuracy * 100:.2f}%')
        # Plot the images
    plt.figure(figsize=(20, 10))
    for i in range(10):
        ax = plt.subplot(2, 5, i + 1)
        plt.imshow(images[i])
        plt.title(f"Label: {np.argmax(labels[i])}")
        plt.axis("off")

    plt.show()
