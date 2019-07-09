import unittest
import build


class MyTest(unittest.TestCase):
    def test_get_image_text_bad_path(self):
        image_path = "images/badtest123.jpg"
        img = build.get_img_text(image_path)
        self.assertEqual(img, "")

    def test_get_image_text(self):
        image_path = "images/humpty_dumpty.jpg"
        img_text = build.get_img_text(image_path)
        self.assertTrue(len(img_text) > 0)