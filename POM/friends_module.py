import re
import time

from Library.excle_lib import ReadExcle
from Library.config import Configuration

class FriendsPage:
    obj_1 = ReadExcle()
    locator_reg = obj_1.read_locator(Configuration.FRIENDS_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def user_name(self,username):
        locator = self.locator_reg["username"]
        self.driver.find_element(*locator).send_keys(username)

    def pass_word(self,password):
        locator = self.locator_reg["password_txt"]
        self.driver.find_element(*locator).send_keys(password)
        time.sleep(3)

    def login_btn(self):
        locator = self.locator_reg["login_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def Click_1(self):
        locator = self.locator_reg["Click_1"]
        self.driver.find_element(*locator).click()
        time.sleep(6)

    def friends_btn1(self):
        locator = self.locator_reg["friends_btn1"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def frd_req(self):
        locator = self.locator_reg["frd_req"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def sent_req_link(self):
        locator = self.locator_reg["sent_req_link"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def del_req(self):
        locator = self.locator_reg["del_req"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def close_btn1(self):
        locator = self.locator_reg["close_btn1"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def suggestion(self):
        locator = self.locator_reg["suggestion"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def add_fr(self):
        locator = self.locator_reg["add_fr"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def remo_fr(self):
        locator = self.locator_reg["remo_fr"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def all_frd(self):
        locator = self.locator_reg["all_frd"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def birthday(self):
        locator = self.locator_reg["birthday"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def custom_list(self):
        locator = self.locator_reg["custom_list"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def close_frd(self):
        locator = self.locator_reg["close_frd"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def notification_setting(self):
        locator = self.locator_reg["notification_setting"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def notification_dot(self):
        locator = self.locator_reg["notification_dot"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    # def TC_Home_001(self):
    #     locator = self.locator_reg["friends_btn"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_002(self):
    #     locator = self.locator_reg["new_msg"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_003(self):
    #     locator = self.locator_reg["frd_req"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    # def TC_HOME_004(self):
    #     locator = self.locator_reg["cnfrm_req"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_005(self):
    #     locator = self.locator_reg["sent_req_link"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    # def TC_HOME_006(self):
    #     locator = self.locator_reg["del_req"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    #
    # def TC_HOME_011(self):
    #     locator = self.locator_reg["suggestion"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_012(self):
    #     locator = self.locator_reg["add_fr"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_013(self):
    #     locator = self.locator_reg["remo_fr"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_016(self):
    #     locator = self.locator_reg["all_frd"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_017(self):
    #     locator = self.locator_reg["search"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_018(self):
    #     locator = self.locator_reg["search_dot"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    # def TC_HOME_019(self):
    #     locator = self.locator_reg["msg"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    #
    # def TC_HOME_020(self):
    #     locator = self.locator_reg["block"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_021(self):
    #     locator = self.locator_reg["unfriend"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_022(self):
    #     locator = self.locator_reg["birthday"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_023(self):
    #     locator = self.locator_reg["name_click"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_024(self):
    #     locator = self.locator_reg["custom_list"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_025(self):
    #     locator = self.locator_reg["close_frd"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_026(self):
    #     locator = self.locator_reg["fav"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    # def TC_HOME_027(self):
    #     locator = self.locator_reg["frds"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    #
    # def TC_HOME_028(self):
    #     locator = self.locator_reg["notification_setting"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
    #
    # def TC_HOME_029(self):
    #     locator = self.locator_reg["notification_dot"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(3)
    #
