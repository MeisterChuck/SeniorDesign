import os

import nibabel as nib
import numpy
import scipy
import dicom
import matplotlib.pyplot as plt

# Load File
file_path = 'Data-I/LS4025 Rest4/unprocessed/3T/rfMRI_REST4_LR/LS4025_3T_rfMRI_REST4_LR.nii.gz'

# Load Brain Scan
epi_image = nib.load(file_path)
mask_image = nib.load(file_path)
# Create Mask
epi_data = epi_image.get_data()
mask_data = mask_image.get_data()

# Retrieve File Name
file_base_name = os.path.basename(file_path)
file_name = os.path.splitext(file_base_name)[0]

# Plot Brain Scan
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17,7))
# vmin and vmax change the contrast values
ax1.imshow(1 + mask_data[:,:,50,90], interpolation='nearest', cmap='gray', vmin=-50, vmax=2000)
ax2.imshow(1 - epi_data[:,:,50,419], interpolation='nearest', cmap='gray', vmax=2000)

# Apply Mask to Image
#mask_data = mask_data.astype(bool)
#epi_data_masked = epi_data[mask_data]

# ToDo - What does it mean by too many indices!?!?
#ax3.imshow(1 - epi_data_masked[1,:], interpolation='nearest', cmap'gray', vmax=2000)

ax1.set_title('Mask Image')
ax2.set_title('EPI Image')
plt.show()
print(mask_data.shape)