import matplotlib.pyplot as plt
import nibabel as nib

image = nib.load("Conversions/LS4025_3T_SpinEchoFieldMap_LR.nii.gz")
image_data = image.get_data()

print(image_data.shape)

new_image = 0

for x in range (0, image_data.shape[3]):
    new_image = new_image + image_data[:,:,:,x]

new_image = new_image/4
print(new_image.shape)

for x in range (0, new_image.shape[2]):
    plt.imshow(new_image[:,:,x], cmap='bone', interpolation='nearest')
    new_image_location = "New Data/topviewtest" + str(x) + ".png"
    print(new_image_location)
    plt.imsave(new_image_location, new_image[:,:,x], cmap='bone')
    plt.show()

