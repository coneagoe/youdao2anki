import unittest
import os

from pronounceDownloader import PRONOUNCE_LIB_YOUDAO, PronounceDownloader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dir = r'./'
        self.downloader = PronounceDownloader(PRONOUNCE_LIB_YOUDAO, self.dir)

    def test_download(self):
        word = 'yellow'
        file = os.path.join(self.dir, word)
        if os.path.exists(file):
            os.remove(file)

        self.assertNotEquals(self.downloader.download(word), False)


if __name__ == '__main__':
    unittest.main()
