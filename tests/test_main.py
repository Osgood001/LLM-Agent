import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch, MagicMock
import thread

class TestMain(unittest.TestCase):
    @patch('main.OpenAI')
    @patch('main.importlib')
    def test_call_openai_agent(self, mock_importlib, mock_openai):
        mock_openai.return_value.files.retrieve.return_value = 'file'
        mock_openai.return_value.beta.assistants.retrieve.return_value = 'assistant'
        assistant, file = thread.call_openai_agent('file_id', 'assistant_id')
        self.assertEqual(assistant, 'assistant')
        self.assertEqual(file, 'file')

    @patch('main.importlib')
    def test_call_tool(self, mock_importlib):
        mock_module = MagicMock()
        mock_importlib.import_module.return_value = mock_module
        thread.call_tool('tool_name', 'prompt')
        mock_module.run.assert_called_once_with('prompt')

if __name__ == '__main__':
    unittest.main()