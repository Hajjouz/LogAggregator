# test_logaggregator.py
"""
Tests for LogAggregator module.
"""

import unittest
from logaggregator import LogAggregator

class TestLogAggregator(unittest.TestCase):
    """Test cases for LogAggregator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LogAggregator()
        self.assertIsInstance(instance, LogAggregator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LogAggregator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
