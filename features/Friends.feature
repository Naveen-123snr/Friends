Feature: friends_module
#Scenario:
  Scenario Outline:
    Given launch Firefox browser
    And  enter username "<username_>"
    And  enter password "<pwd>"
    Then click on login
    Then  click on friends button
    And click on friend requests
    And click on send requests
    And click on cancel request
    And click on close button
    And click on friends button
    Then click on suggestion
    And click on add friend
    And click on remove friend
    And click on friends button
    Then  click on all friends
    And click on friends button
    Then click on birthday
    And click on friends button
    Then click on custom list
    And click on close friend
    And click on friends button
    Then click on notification settings
    And  click on notification dot
    Examples:
      |username_                   | pwd        |
      |naveen124snr                | Naveen@12 |
      |7989315252                  | Naveen@12 |



#Feature: Friends_Module
#
#  Background: Common Steps
#    Given Open the browser and enter the valid URL
#    When Enter the Username"naveen124snr"
#    And Enter the Password"Naveen@12"
#    And Click on login button open
#
#  Scenario: Verify that user is able to click on all friend button and also able to click on message
#    And Click on friends button open
##    And Click on all friend button
##    And Click on search bar
##    And Click on search dot
##    And Click on message button
##    And Click on block button
##    Then Click on unfriend button
#
##
#
#
##   Scenario: Verify that user is able to click on custom list button and can able to click on close friend, fav and frds button
##    And Click on custom list
##    And Click on close friend button
##    And Click on fav button
##    Then Click on frds button
##
##  Scenario: verify that user is able to click on notification settings button
##    And Click on notification settings button
##    And Click on notification dot button
##    Then Close the browser
#
#
#
##Feature: Friends_Module
##
##  Background: Common Steps
##    Given Open the browser and enter the valid URL
##    When Enter the Username"naveen124snr "
##    And Enter the Password"Naveen@12"
##    And Click on login button open
##
##  Scenario: Verify that user is able to click on all friend button and also able to click on message
##    And Click on friends button open
##    And Click on all friend button
##    And Click on search bar
##    And Click on search dot
##    And Click on message button
##    And Click on block button
##    Then Click on unfriend button
##
##   Scenario: Verify that user is able to click on birthday button and can able to see next upcoming button
##    And Click on Birthday button open
##    Then Click on name link_1
##
##   Scenario: Verify that user is able to click on custom list button and can able to click on close friend, fav and frds button
##    And Click on custom list
##    And Click on close friend button
##    And Click on fav button
##    Then Click on frds button
##
##  Scenario: verify that user is able to click on notification settings button
##    And Click on notification settings button
##    And Click on notification dot button
##    Then Close the browser