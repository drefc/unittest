import unittest
from widget import Widget

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('foo widget')

    def test_default_widget_size(self):        
        self.assertEqual(self.widget.size(), (50,50), 'nope default size')

    def test_widget_resize(self):        
        self.widget.resize(200,200)
        self.assertEqual(self.widget.size(), (200,200), 'nope size after resize')
    
    def tearDown(self):
        self.widget.dispose()