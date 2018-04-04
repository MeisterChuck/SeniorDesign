from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing import image
# Collect Data
# Dimensions of images
img_width, img_height = 110, 110

train_data_dir = 'Averaged Data Images/'
validation_data_dir = 'Averaged Data Images/'

# Used to rescale the pixel values from [0, 255] to [0, 1] interval
datagen = ImageDataGenerator(rescale=1.0 / 255)

# Automagically retrieve images and their classes for train and validation sets
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=16,
    class_mode='binary')

validation_generator = datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary')

# Build a Model
# Layer 1
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Layer 1 Done")

# Layer 2
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Layer 2 Done")

# Layer 3
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Layer 3 Done")

# Dropout Layer
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
print("Dropout Layer Done")

# model.summary()

# Compile Layer
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
print("Compile Layer Done")

# Training
nb_epoch = 30
nb_train_samples = 2048
nb_validation_samples = 832

# Train Model
model.fit_generator(train_generator, steps_per_epoch=nb_train_samples, epochs=nb_epoch,
                    validation_data=validation_generator, validation_steps=nb_validation_samples)
model.save_weights('models/simple_CNN.h5')
print("Train Model Done")

# Test Model
img = image.load_img(
    'Averaged Data Images/Emotion/Emotion_tfMRI_EMOTION_LR_LS4025_3T_SpinEchoFieldMap_LR_frontview23.png',
    target_size=(224, 224))
prediction = model.predict(img)
print(prediction)
