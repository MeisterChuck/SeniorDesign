from unittest import TestCase
#tfMRI_EMOTION_LR_LS4025_3T_tfMRI_EMOTION_LR_SBRef

from GetData.GetData import GetData
import glob

class TestGetData(TestCase):
    def test_getfilepath(self):
        GetData.category = "Emotion"


        self.assertIsNone(GetData.getfilepath(GetData.category))


    def test_getfilename(self):
        file_path = "Data-I/LS4025 Emotion/unprocessed/3T/tfMRI_EMOTION_LR/LS4025_3T_SpinEchoFieldMap_LR.nii.gz"

        test = GetData.getfilename(file_path)

        self.assertEqual("tfMRI_EMOTION_LR_LS4025_3T_SpinEchoFieldMap_LR", test)


    def test_getaverage_averaged(self):
        file_path = "../Data-I/LS4025 Emotion/unprocessed/3T/tfMRI_EMOTION_LR/LS4025_3T_SpinEchoFieldMap_LR.nii.gz"
        test = GetData.getaverage(file_path, "Emotion")

        self.assertEqual((90, 104, 72), test.shape)

    def test_getaverage_skipped(self):
        file_path = "../Data-I/LS4025 Emotion/unprocessed/3T/tfMRI_EMOTION_LR/LS4025_3T_tfMRI_EMOTION_LR_SBRef.nii.gz"
        test = GetData.getaverage(file_path, "Emotion")

        self.assertEqual((90, 104, 72), test.shape)