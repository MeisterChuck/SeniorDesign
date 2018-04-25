import glob
import random

import numpy as np
from PIL import Image

category = ["Emotion", "Gambling", "Rest", "Structural", "WM"]

for state in range(0, len(category)):
    print("Generating Data for {0}".format(category[state]))

    for file_path in glob.glob('Averaged Images/train/' + category[state] + '/*.png'):
        image = Image.open(file_path)
        image = image.convert('L')
        newImage = image.resize((200, 186))

        print('Created: ' + str(category[state]) + '/' + str(category[state]) + '.original.png')
        image.save('Averaged Images/trainBlurred/' + str(category[state]) + '/' + str(category[state]) + '.original.png', "PNG")
        image.save('Averaged Images/validationBlurred/' + str(category[state]) + '/' + str(category[state]) + '.original.png', "PNG")

        newImage = np.asarray(newImage)
        blurredImage = Image.fromarray(newImage)

        # Non Traditional range for formatting purposes
        for index in range(1, 1001):
            nimage = np.empty([186, 200])

            # Function will generate an image with gauss noise added
            def noisy(image, nimage):
                mean = random.uniform(0, 1)
                # mean = 0
                print(mean)
                var = random.randint(50, 100)
                # var = 100
                print(var)
                sigma = var ** 0.5;
                for i in range(0, 186):
                    for j in range(0, 200):
                        nimage[i, j] = image[i, j] + np.random.normal(mean, sigma, 1)
                return nimage

            blurredImage = noisy(newImage, nimage)
            blurredImage = Image.fromarray(blurredImage).convert('L')

            print('Created: ' + str(category[state]) + '/' + str(category[state]) + '.' + str(index) + '.png')
            blurredImage.save('Averaged Images/trainBlurred/' + str(category[state]) + '/' + str(category[state]) + '.' + str(index) + '.png')
            blurredImage.save('Averaged Images/validationBlurred/' + str(category[state]) + '/' + str(category[state]) + '.' + str(index) + '.png')

        print("\n")