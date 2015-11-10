#@Author Yichen Fan
import unittest
from unittest import TestCase 
import numpy as np
from Investment_instrument import *
from Input_dataset import *
from PS8 import *
"""Test if could recognize the valid or invalid import for both position and trails"""
class Test_Input_Dataset(TestCase):
	def test_get_list_valid(self):
		str1 = '[1, 10, 100, 1000]'
		self.assertTrue(get_list(str1) == [1, 10, 100, 1000])

	def test_get_list_invalid(self):
		str2 = '[dd]'
		self.assertRaises(InvalidInteger, get_list, str2)

		str3 = '[1,'
		self.assertRaises(InvalidList, get_list, str3)

		str4 = '[1, 2]'
		self.assertRaises(InvalidPosition, get_list, str4)

	def test_get_num_valid(self):
		str5 = '100'
		self.assertTrue(get_num(str5) == 100)

	def test_get_num_invalid(self):
		str6 = 'v'
		self.assertRaises(InvalidInteger, get_num, str6)



if __name__ == '__main__':
	unittest.main()
