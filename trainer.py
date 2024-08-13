import tensorflow as tf
from keras._tf_keras.keras import layers, models
from keras._tf_keras.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt


width, height = 64, 64
g_batch_size = 32

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1.0/255.0,
    rotation_range=30,
    horizontal_flip=True,
    validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    'data', 
    target_size=(width, height), 
    class_mode='categorical', 
    batch_size=g_batch_size, 
    shuffle=True,
    subset='training')

validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1.0/255.0,
    rotation_range=30,
    horizontal_flip=True,
    validation_split=0.2)
validation_generator = validation_datagen.flow_from_directory(
    'data', 
    target_size=(width, height), 
    class_mode='categorical', 
    batch_size=g_batch_size, 
    shuffle=True,
    subset='validation')


# Define the ResNet block
def resnet_block(inputs, filters, kernel_size=3, stride=1):
    x = layers.Conv2D(filters, kernel_size, strides=stride, padding='same', use_bias=False, kernel_initializer='he_normal')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2D(filters, kernel_size, strides=1, padding='same', use_bias=False, kernel_initializer='he_normal')(x)
    x = layers.BatchNormalization()(x)

    if stride != 1 or inputs.shape[-1] != filters:
        inputs = layers.Conv2D(filters, 1, strides=stride, padding='same', use_bias=False, kernel_initializer='he_normal')(inputs)
        inputs = layers.BatchNormalization()(inputs)

    x = layers.add([x, inputs])
    x = layers.ReLU()(x)
    return x

# Define the ResNet model
def create_resnet(input_shape, num_classes):
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(64, 3, strides=1, padding='same', use_bias=False, kernel_initializer='he_normal')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = resnet_block(x, 64)
    x = resnet_block(x, 64)

    x = resnet_block(x, 128, stride=2)
    x = resnet_block(x, 128)

    x = resnet_block(x, 256, stride=2)
    x = resnet_block(x, 256)

    x = resnet_block(x, 512, stride=2)
    x = resnet_block(x, 512)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs, x)
    return model

# Create the ResNet model
model = create_resnet((width, height, 3), train_generator.num_classes)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

checkpoint = ModelCheckpoint(' last.keras',save_freq='epoch')
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train the model
history = model.fit(train_generator, epochs=10, batch_size=g_batch_size, validation_data=validation_generator, callbacks=[checkpoint, early_stopping])

model.save('out_model.keras')

# Evaluate the model
test_loss, test_acc = model.evaluate(validation_generator)
print(f'Test accuracy: {test_acc}')

print(history.history)

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
