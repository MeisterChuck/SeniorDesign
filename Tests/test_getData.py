from unittest import TestCase
#tfMRI_EMOTION_LR_LS4025_3T_tfMRI_EMOTION_LR_SBRef

from GetData.GetData import GetData
import glob

class TestGetData(TestCase):
    def test_run(self):
        self.assertIsNone(GetData.run(self))

    def test_getfilepath(self):
        GetData.category = "Emotion"
        print(GetData.getfilepath(GetData.category))

        self.assertTrue(GetData.getfilepath(GetData.category))


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

    def test_getaveragedimages(self):
        file_path = "../Tests/Averaged Data/Emotion/tfMRI_EMOTION_LR_LS4025_3T_SpinEchoFieldMap_LR.nii.gz"
        category = "Emotion"

        self.assertEqual(266, GetData.getaveragedimages(file_path, category))

    def test_getaveragedfilepath(self):
            category = "Emotion"
            test = GetData.getaveragedfilepath(category)

            self.assertEqual(2, test)