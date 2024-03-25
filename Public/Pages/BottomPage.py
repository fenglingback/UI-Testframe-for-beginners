from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import bottom


class Bottom(basePage, bottom):

    def enter_twitter(self):
        self.twitter_a.click()

    def enter_facebook(self):
        self.facebook_a.click()

    def enter_linkedin(self):
        self.linkedin_a.click()


mybottom = Bottom(driver)