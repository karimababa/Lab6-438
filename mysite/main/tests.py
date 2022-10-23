from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/players')
    #find the elements you need to submit form
    player_name = selenium.find_element_by_id('id_name')
    player_height = selenium.find_element_by_id('id_height')
    player_team = selenium.find_element_by_id('id_team')
    player_ppg = selenium.find_element_by_id('id_ppg')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    player_name.send_keys('Lebron James')
    player_team.send_keys('Los Angeles Lakers')
    player_height.send_keys('6 feet 9 inches')
    player_ppg.send_keys('25.7')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Lebron James' in selenium.page_source

class TeamFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/teams')
    #find the elements you need to submit form
    team_id = selenium.find_element_by_id('id_team_id')
    team_name = selenium.find_element_by_id('id_team_id')
    city = selenium.find_element_by_id('id_city')
    year_founded = selenium.find_element_by_id('id_year_founded')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    team_id.send_keys('20')
    team_name.send_keys('Golden State Warriors')
    city.send_keys('San Francisco')
    year_founded.send_keys('1946')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Golden State Warriors' in selenium.page_source