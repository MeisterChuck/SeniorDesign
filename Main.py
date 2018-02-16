import glob
import nibabel as nib

def navigateFiles(directory):
    # Used to determine if all .gz files are being found, will remove index later
    index = 0

    # For speed only navigate files that have these attributes
    for name in glob.glob(directory + '/*[Emotion, Gambling, Rest, Structural, WM]*/unprocessed/3T/*/*?.gz'):

        # Load images and its data
        image = nib.load(name)
        image_data = image.get_data()

        # Ignore all files that don't have a fourth dimension
        if(image_data.ndim == 4):
            print(image_data.shape)
            index = index + 1
        else:
            print("Outlier")
            index = index + 1

    print(index)

navigateFiles("Data-I")

