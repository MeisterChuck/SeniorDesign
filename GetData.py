import glob
import nibabel as nib
import matplotlib.pyplot as plt


class GetData:
    category = []

    def __init__(self, category):
        GetData.category = category

    def run(self):
        print("It runs\n")
        for state in range(0, len(GetData.category)):
            # Gets averaged data
            # GetData.getfilepath(GetData.category[state])

            # Gets averaged images from averaged data
            GetData.getaveragedfilepath(GetData.category[state])

    def getfilename(file_path):
        file = file_path.split('/')

        # Used '_' instead of '/' to not have to create an unnecessary directory, just need all files to be unique.
        new_file = file[len(file) - 2] + "_" + file[len(file) - 1]
        file_name = new_file[:-7]

        return file_name

    def getaverage(file_path, category):
        image = nib.load(file_path)
        image_data = image.get_data()

        # Change hdr size from 348 to 540 to convert from NIfTI1 to NIfTI2
        image.header['sizeof_hdr'] = 540

        new_image = 0

        new_file_path = 'Averaged NIfTI/' + category + "/" + GetData.getfilename(file_path) + '.nii.gz'

        if image_data.ndim == 4:
            print("Calculate Average")

            for x in range(0, image_data.shape[3]):
                new_image = new_image + image_data[:, :, :, x]

            print(image_data.shape)
            new_image = new_image / image_data.shape[3]
            print(new_image.shape)

            nib.save(nib.Nifti2Image(new_image, image.affine, image.header), new_file_path)
        else:
            print("\nSkip Average\n")

            new_image = image_data

            nib.save(nib.Nifti2Image(image_data, image.affine, image.header), new_file_path)

        return new_image

    def getfilepath(state):
        index = 0

        for file_path in glob.glob('Data-I/*' + state + '*/unprocessed/3T/*/*?.gz'):
            print("In {0} - {1}".format(state, GetData.getfilename(file_path)))
            GetData.getaverage(file_path, state)
            index = index + 1

        return True


    def getaveragedimages(file_path, category):
        image = nib.load(file_path)
        image_data = image.get_data()

        # index_front = 0
        index_top = 0
        # index_side = 0

        # for x in range(0, image_data.shape[0]):
        #     new_image_location = "Averaged Images/train/" + category + "/" + category + "." + GetData.getfilename(file_path) + "_sideview" + str(
        #         x) + ".png"
        #
        #     print(new_image_location + " created")
        #
        #     plt.imsave(new_image_location, image_data[x, :, :], cmap='bone')
        #
        #     index_side = index_side + 1
        #
        # print(f"\nThere are {index_side} side images\n")
        #
        # for y in range(0, image_data.shape[1]):
        #     new_image_location = "Averaged Images/train/" + category + "/" + category + "." + GetData.getfilename(file_path) + "_frontview" + str(
        #         y) + ".png"
        #
        #     print(new_image_location + " created")
        #
        #     plt.imsave(new_image_location, image_data[:, y, :], cmap='bone')
        #
        #     index_front = index_front + 1
        #
        # print(f"\nThere are {index_front} front images\n")

        for z in range(0, image_data.shape[2]):

            print(image_data.shape)

            if(category == "Structural" and z == 63):
                new_image_location = "Averaged Images/train/" + category + "/" + category + "." + GetData.getfilename(
                    file_path) + "_topview" + str(
                    z) + ".png"

                print(new_image_location + " created")

                plt.imsave(new_image_location, image_data[:, :, z], cmap='bone')
            elif(z == 60 and category != "Structural"):
                new_image_location = "Averaged Images/train/" + category + "/" + category + "." + GetData.getfilename(file_path) + "_topview" + str(
                z) + ".png"

                print(new_image_location + " created")

                plt.imsave(new_image_location, image_data[:,:, z], cmap = 'bone')

            index_top = index_top + 1

        print(f"\nThere are {index_top} top images\n")

    def getaveragedfilepath(category):
        index = 0
        averagedImagePath = nib.load("Averaged NIfTI/Emotion/tfMRI_EMOTION_LR_LS4025_3T_SpinEchoFieldMap_LR.nii.gz")
        imagePath = nib.load("Data-I/LS4025 Emotion/unprocessed/3T/tfMRI_EMOTION_LR/LS4025_3T_SpinEchoFieldMap_LR.nii.gz")

        averageImage = averagedImagePath.get_data()
        image = imagePath.get_data()

        print(averageImage.shape)
        print(image.shape)


        for file_path in glob.glob('Averaged NIfTI/' + category + '/*.gz'):
            GetData.getaveragedimages(file_path, category)

            index = index + 1

        print(f"There are {index} files\n")

        return index