import glob
import nibabel as nib


def getfilename(file_path):
    file = file_path.split('/')

    # Used '_' instead of '/' to not have to create an unnecessary directory, just need all files to be unique.
    new_file = file[len(file)-2] + "_" + file[len(file)-1]
    file_name = new_file[:-7]

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
        print("\nSkip Average\n")

        nib.save(nib.Nifti2Image(image_data, image.affine, image.header), new_file_path)



# Navigate the input data directory and and located all the .gz files with each mental state
def getfilepath(category):
    index = 0

    for file_path in glob.glob('Data-I/*' + category + '*/unprocessed/3T/*/*?.gz'):
        index = index + 1
        print("In {0} - {1}".format(category, getfilename(file_path)))
        getaverage(file_path, category)

    print(f"There are {index} files\n")