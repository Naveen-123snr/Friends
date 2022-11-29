import pytest

from Library.excle_lib import ReadExcle
from POM.friends_module import FriendsPage
from Library.config import Configuration



class TestFriendsPage:
    obj = ReadExcle()
    data = obj.read_test_data(Configuration.FRIENDS_TEST_DATASHEET)

    @pytest.mark.parametrize("username, password", data)
    def test_click_login_link(self, init_driver,username, password):
        driver = init_driver
        lp = FriendsPage(driver)
        lp.user_name(username)
        lp.pass_word(password)
        lp.login_btn()
        # lp.Click_1()
        lp.friends_btn1()
        lp.frd_req()
        lp.sent_req_link()
        lp.del_req()
        lp.close_btn1()
        lp.friends_btn1()
        lp.suggestion()
        lp.add_fr()
        lp.remo_fr()
        lp.friends_btn1()
        lp.all_frd()
        lp.friends_btn1()
        lp.birthday()
        lp.friends_btn1()
        lp.custom_list()
        lp.close_frd()
        lp.friends_btn1()
        lp.notification_setting()
        lp.notification_dot()