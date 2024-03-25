from time import sleep, strftime
from urllib import request
from Config.global_config import data_path


class getImg:

    def __init__(self, driver):
        self.driver = driver

    def getImgUrl(self, img):
        img_src = img.get_attribute('src')
        # print(img_src)
        return img_src

    # def saveImg(self, *img_loc):
    #     img_src = self.getImgUrl(*img_loc)
    #     img_path = data_path + '/{0}.png'.format(strftime("%Y-%m-%d-%H-%M-%S"))
    #     request.urlretrieve(img_src, img_path)
    #     print(img_path)
    #     return img_path

    # 调用的是ddddocr模块，目前测试不稳定
    # def getCaptcha(driver, *loc):
    #     img_file = getImg(driver).saveImg(*loc)
    #     ocr = ddddocr.DdddOcr()
    #     with open(img_file, 'rb') as f:
    #         img_bytes = f.read()
    #     result = ocr.classification(img_bytes)
    #     print(result)

    def getCaptcha(self, img_loc):
        img_src = self.getImgUrl(img_loc)
        captcha = img_src[-8:-4]
        return captcha

    def goTo_imgUrl_getPageSource(self, img_loc):
        img_src = self.getImgUrl(img_loc)
        self.driver.get(img_src)
        sleep(1)
        x = self.driver.page_source
        sleep(1)
        self.driver.back()
        return x
