import unittest
from ..data_prep import prepareData
from ..mentions import calc_mentions
from ..verbosity import calc_verbosity
from ..follow import calc_follow
from ..nondict import calc_nondict

import os.path as osp

this_dir = osp.dirname(__file__)
path1 = osp.join(this_dir,'data_testing.csv')
path2 = osp.join(this_dir,'..','..','..','data','words_alpha.txt')

dfsmall = prepareData(path1, path2)
val_1 = calc_verbosity(dfsmall)
val_2 = calc_mentions(dfsmall)
val_3 = calc_follow(dfsmall)
val_4 = calc_nondict(dfsmall)


class AllTestCase (unittest.TestCase):
    def test_CheckLenData(self): #Test 1
        self.assertEqual(len(dfsmall), 5000)

    def test_CheckNumCol(self): #Test 2
        self.assertEqual(len(dfsmall.columns), 29)

    def test_CheckVerbosity(self): #Test 3
        x_1 = 'twilight'
        self.assertEqual(val_1[x_1], 0.26)
       
    def test_CheckVerbositySum(self): #Test 4
        self.assertEqual(round(sum(val_1.values()),2),0.99)

    def test_CheckMention(self): #Test 5
        x_2 = 'twilight'
        x_3 = 'applejack'
        self.assertEqual(val_2[x_2][x_3], 0.16)

    def test_CheckMentionSum(self): #Test 6
        x_4 = 'twilight'
        self.assertEqual(sum(val_2[x_4].values()), 1.0)

    def test_CheckFollow(self): #Test 7
        x_5 = 'twilight'
        x_6 = 'rainbow'
        self.assertEqual(val_3[x_5][x_6], 0.5)

    def test_CheckFollowSum(self): #Test 8
        x_7 = 'twilight'
        self.assertEqual(sum(val_3[x_7].values()), 1.0)

    def test_CheckNondict(self): #Test 9
        x_8 = 'twilight'
        ans_x_8 = ['ve', 'equestria','everypony','fluttershy','ponyville']
        self.assertEqual(val_4[x_8], ans_x_8)

    def test_CheckKeySimilarity(self): #Test 10
        self.assertEqual(val_1.keys(), val_3.keys())
