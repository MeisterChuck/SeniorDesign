from nilearn import image
import nibabel as nib
#from nilearn import datasets
from nilearn import surface
# from nilearn import plotting adding this comment makes it work?!?!

import matplotlib.pyplot

# Load File
file_path = nib.load('Data-I/LS4025 WM/unprocessed/3T/tfMRI_WM_LR/LS4025_3T_tfMRI_WM_LR_SBRef_gdc.nii.gz')
file_path_data = file_path.get_data()

print(file_path.shape)
print(file_path.shape[2])


def average(number):
    array=[]
    for i in range (0, number+1):
        array.append(i)
        print(array[i])

    return int(sum(array)/number)

print(average(file_path.shape[2]))
#fsaverage = datasets.fetch_surf_fsaverage5()

from nilearn import plotting

smoothed_image = image.smooth_img(file_path, fwhm=5)
#texture = surface.vol_to_surf(file_path, fsaverage.pial_right)

#3D doesn't work yet
#plotting.plot_surf_stat_map(fsaverage.infl_right, texture, hemi='right',
#                            title='Surface right hemisphere',
#                            threshold=1., bg_map=fsaverage.sulc_right,
#                            cmap='cold_hot')
#plotting.plot_stat_map(file_path, display_mode='x', threshold=20., cut_coords=range(0, 100, 5), title='Slices')
#plotting.plot_stat_map(file_path, threshold=3)
plotting.plot_epi(smoothed_image, title="Senior Design", resampling_interpolation='continuous', bg_img=None)
#plotting.plot_img(smoothed_image)
#plotting.plot_glass_brain(file_path)
plotting.show()