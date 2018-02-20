import glob
import ntpath
import os
import nibabel as nib

# TODO adjust file_path to include previous directory, some directories contain files of the same name
# Used ntpath for program to navigate directories on all platforms
# Used os to get filename
def getfilename(file_path):
    file_path_name = ntpath.basename(file_path)
    file_path_name_split = os.path.splitext(file_path_name)[0]
    file_name = file_path_name_split[:-7]
    return file_name


def getaverage(file_path, category):
    image = nib.load(file_path)
    image_data = image.get_data()

    # Change hdr size from 348 to 540 to convert from NIfTI1 to NIfTI2
    image.header['sizeof_hdr'] = 540

    new_file_path = 'Averaged Data/' + category + "/" + getfilename(file_path) + '.nii.gz'

    if image_data.ndim == 4:
        print("Calculate Average")
        new_image = 0

        for x in range (0, image_data.shape[3]):
            new_image = new_image + image_data[:, :, :, x]

        new_image = new_image / 4

        nib.save(nib.Nifti2Image(new_image, image.affine, image.header), new_file_path)
    else:
        print("Skip Average")

        nib.save(nib.Nifti2Image(image_data, image.affine, image.header), new_file_path)



# Navigate the input data directory and and located all the .gz files with each mental state
def getfilepath(category):
    index = 0

    for file_path in glob.glob('Data-I/*' + category + '*/unprocessed/3T/*/*?.gz'):
        index = index + 1
        print("In {0} - {1}".format(category, getfilename(file_path)))
        getaverage(file_path, category)

    print(f"There are {index} files\n")