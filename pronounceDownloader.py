import os
import logging
import requests


PRONOUNCE_LIB_YOUDAO = 1


gPronounceDict = { PRONOUNCE_LIB_YOUDAO: r'http://dict.youdao.com/dictvoice' }


class PronounceDownloader(object):
    def __init__(self, pronounceId, saveDir):
        assert os.path.exists(saveDir), "The save directory doesn't exist."
        assert pronounceId in gPronounceDict.keys(), "The pronounce lib specified is not recognized."

        self.url = gPronounceDict[pronounceId]
        self.saveDir = saveDir
        self.country = "2"


    def download(self, word):
        # TODO: use template method to generate URL
        resp = requests.post("http://dict.youdao.com/dictvoice", data = {"audio": word, "type": self.country})
        if resp.status_code == 200:
            file_name = word + ".mp3"
            with open(os.path.join(self.saveDir, file_name), 'wb') as f:
                f.write(resp.content)
                return file_name
        else:
            logging.error("Get the pronounce of %s fail: %d", word, resp.status_code)

        return None
