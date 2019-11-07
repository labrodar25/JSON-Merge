import unittest
import mock
from mergeJson import mergeJsonFiles

class mergeJsonFilesTestCase(unittest.TestCase):
	def setUp(self):
		self.mergeJsonClass = mergeJsonFiles()
	
	@mock.patch('mergeJson.open')
	@mock.patch('mergeJson.json')
	@mock.patch('mergeJson.glob')
	@mock.patch('mergeJson.os')
	def test_mergeJson(self, mock_os, mock_glob, mock_json, mock_open):
		testPath = 'dummyPath/'
		testinFile = 'dummyInfile'
		testOutFile = 'dummyOutfile'
		dummyMaxFileSize = 10
		
		with self.subTest('Positive test case'):
			mock_glob.glob.return_value = ['dummyFileName.json']
			mock_os.path.getsize.return_value = 2
			mock_json.dump.return_value = {'dummyKey' : ['dummy_value']}
			mock_json.load.return_value = {'dummy_key' : ['dummy_value']}
	
			self.mergeJsonClass.mergeJson(testPath, testinFile, testOutFile, dummyMaxFileSize)
			
			mock_json.load.assert_called_once()
			mock_json.dump.assert_called_once()

		with self.subTest('Negative test case'):	
			mock_os.path.getsize.return_value = 12
			
			self.mergeJsonClass.mergeJson(testPath, testinFile, testOutFile, dummyMaxFileSize)
			
			mock_json.dump.assert_called()

if __name__ == '__main__':
    unittest.main()			
			
		
		
		
		
