# 10.2.3 测试AnonymousSurvey类
# 10.2.4 方法setUp()

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试"""
	def setUp(self):
		"""
		创建一个调查对象和一组答案，供使用的测试方法使用
		"""		
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""测试单个答案会被妥善地存储"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	
	def test_store_three_response(self):
		"""测试三个答案是否会被妥善地存储"""
		for response in self.responses:
			self.my_survey.store_response(response)
			   # 这里是错误判断方法，只能判断一个字符串是否在一个列表中
		# self.assertIn('English', 'Spanish', 'Mandarin', my_survey.responses)
		# 正确判断方法，使用遍历答案，一个一个判断
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main() 
