import unittest
from widget import Widget

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('foo')
        self.assertEqual(widget.size(), (50,50))