import glob
from colorama import Fore

from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing import image
from keras.utils import plot_model
import pydot
import graphviz
# import h5py
import numpy as np

# Collect Data
# Dimensions of images
img_width, img_height = 200, 186

# Location of Image Directories
train_data_dir = 'Averaged Images/trainBlurred'
validation_data_dir = 'Averaged Images/validationBlurred'


# Used to rescale the pixel values from [0, 255] to [0, 1] interval
datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, rotation_range=50, vertical_flip=True)

# Automatically retrieve images and their classes for train and validation sets from directory structure
train_generator = datagen.flow_from_directory(
    train_data_dir,
    color_mode='rgb',
    classes=['Emotion', 'Gambling', 'Rest', 'Structural', 'WM'],
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='categorical',
    shuffle=False)

validation_generator = datagen.flow_from_directory(
    validation_data_dir,
    color_mode='rgb',
    classes=['Emotion', 'Gambling', 'Rest', 'Structural', 'WM'],
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='categorical',
    shuffle=False)

print(train_generator.image_shape)
print()

# Build a Model
# Layer 1
model = Sequential()
# 32 is the size of the Conv Window and 3 are the strides along the window
model.add(Conv2D(32, 3, input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
print("Layer 1 Done")

# Layer 2
model.add(Conv2D(32, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))

print("Layer 2 Done")

# Layer 3
model.add(Conv2D(64, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
print("Layer 3 Done")

# Dropout Layer
# Final layer, 5 nodes representing each class, softmax activation makes sure every node sums up to 1
# That means the output nodes are in % score for each image.
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(5))
model.add(Activation('softmax'))
print("Dropout Layer Done")

model.summary()

# Compile Layer
adam = Adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
print("Compile Layer Done")

# Training
nb_epoch = 60
nb_train_samples = 2000
nb_validation_samples = 1500

# Train Model
# Fit Generator contains samples, total number of batch samples, total number of iterations on the data
model.fit_generator(train_generator, steps_per_epoch=nb_train_samples, epochs=nb_epoch,
                    validation_data=validation_generator, validation_steps=nb_validation_samples, use_multiprocessing=False)
model.save_weights('models/simple_CNN_weights_trainBlur.h5')
model.save('models/simple_CNN_trainBlur.h5')
print("Train Model Done")

# Test Model
model = load_model('models/simple_CNN_trainBlur.h5')
model.load_weights('models/simple_CNN_weights_trainBlur.h5')
print('Done loading model')

def predict(mental_state):
    emotionIndex = 0
    gamblingIndex = 0
    restIndex = 0
    structuralIndex = 0
    wmIndex = 0
    for file_path in glob.glob('Averaged Images/validationBlurred/' + mental_state + '/*.png'):
        pictureEmotion = file_path
        emotion = image.load_img(pictureEmotion, target_size=(200, 186))
        emotion = img_to_array(emotion)
        emotion = np.expand_dims(emotion, axis=0)
        prediction = model.predict_classes(emotion)
        if prediction == 0:
            emotionIndex = emotionIndex + 1
            # print("WRONG: {0} is predicted to be {1}".format(pictureEmotion, prediction))
        elif prediction == 1:
            gamblingIndex = gamblingIndex + 1
            # print("WRONG: {0} is predicted to be {1}".format(pictureEmotion, prediction))
        elif prediction == 2:
            restIndex = restIndex + 1
            # print(Fore.GREEN + "CORRECT: {0} is predicted to be {1}".format(pictureEmotion, prediction))
        elif prediction == 3:
            structuralIndex = structuralIndex + 1
            # print("WRONG: {0} is predicted to be {1}".format(pictureEmotion, prediction))
        else:
            wmIndex = wmIndex + 1
        #     print("CORRECT: {0} is predicted to be {1}".format(pictureEmotion, prediction))
        # Fore.RESET
    print(mental_state + " Stats")
    print("\tEmotion: {0}".format(emotionIndex))
    print("\tGambling: {0}".format(gamblingIndex))
    print("\tRest: {0}".format(restIndex))
    print("\tStructural: {0}".format(structuralIndex))
    print("\tWM: {0}".format(wmIndex))

    total = emotionIndex + gamblingIndex + restIndex + structuralIndex + wmIndex
    accuracy = 0

    if mental_state == "Emotion":
        accuracy = (emotionIndex/total) * 100
        print("\tEmotion Accuracy: {0:.3f}%\n".format(accuracy))
        return accuracy
    elif mental_state == "Gambling":
        accuracy = (gamblingIndex/total) * 100
        print("\tGambling Accuracy: {0:.3f}%\n".format(accuracy))
        return accuracy
    elif mental_state == "Rest":
        accuracy = (restIndex/total) * 100
        print("\tRest Accuracy: {0:.3f}%\n".format(accuracy))
        return accuracy
    elif mental_state == "Structural":
        accuracy = (structuralIndex/total) * 100
        print("\tStructural Accuracy: {0:.3f}%\n".format(accuracy))
        return accuracy
    else:
        accuracy = (wmIndex/total) * 100
        print("\tWM Accuracy: {0:.3f}%\n".format(accuracy))
        return accuracy

overallAccuracy = (predict('Emotion') + predict('Gambling') + predict('Rest') + predict('Structural') + predict('WM')) / 5
print("Overall Accuracy: {0:.3f}%".format(overallAccuracy))
# # 1000 testing images
# score = model.evaluate_generator(validation_generator, 1000, use_multiprocessing=False)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])

# Will be used to generate plot for loss and acc, unfortunately there is an error saying pydot and graphviz are not
# installed when in fact they are along with "from keras.utils import plot_model".
#
# plot_model(model, to_file='models/model_v1.png')
# plot_model(model, show_shapes=True, to_file='models/model_v2.png')

# prediction = model.predict(img)




