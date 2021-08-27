from django.test import TestCase, Client, LiveServerTestCase
from user_management.users import CreateNewUser
from user_profil.db_query import DBQuery
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from django.urls import reverse
from time import sleep
from datetime import datetime


class HomePageTest(TestCase):
    def test_landing_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get('').status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get(''),
            '<h1><a href="#hero">Trailing Planner</a></h1>')


class PlannerPageTest(LiveServerTestCase):
    @classmethod
    def setUp(self):
        self.data_login = {
            'username': "userT",
            "password": "test1234&"
        }
        self.data_register = {
            'first_name': "user",
            'last_name': "test",
            'username': "userT",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }

        self.new_training = {
            'trainingDate': "2021-08-01",
            'trainingType': 'Test Training',
            'trainingKm': 20,
            'trainingD': 1000,
            'trainingComments': 'Test comments',
            'status': True
        }

        self.res, self.msg, self.user = CreateNewUser(
            self.data_register).register()

        sport_profil = {}
        sport_profil['objectifName'] = "Test Run Name"
        sport_profil['objectifDistance'] = 34
        sport_profil['objectifD'] = 1250
        sport_profil['objectifDate'] = "2021/06/17"
        sport_profil['stravaLink'] = "test.stravalink.com"

        self.res, self.sportProfilObject = DBQuery(
            self.user).create_sport_profil(sport_profil)

        self.curr_user = DBQuery(self.user)
        res, self.sportProfil = self.curr_user.get_user_profil()
        self.curr_user.create_training(self.new_training)
        self.c = Client()
        self.c.post(
            '/users/login-user/',
            {'username': "userT", 'password': 'test1234&'})

        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_planner_page_url_exists_at_desired_location(self) -> None:
        self.assertRedirects(
            self.client.get("/planner/"), "/users/register/",
            302, fetch_redirect_response=True)

    def test_planner_context_correct(self) -> None:
        data = self.c.get("/planner/").context.flatten()
        self.assertIsNotNone(data["sport_profil"])
        self.assertIsNotNone(data["trainings"])

    def test_connect_user_selenium(self) -> None:
        self.driver.get(f'{self.live_server_url}{reverse("login")}')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/form/div[1]/input').send_keys(
                "userT")
        self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/form/div[2]/input').send_keys(
                "test1234&")
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="submit"]').click()

        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")

    def test_adding_training(self) -> None:
        # Connect a testing user
        self.driver.get(f'{self.live_server_url}{reverse("login")}')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/form/div[1]/input').send_keys(
                "userT")
        self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/form/div[2]/input').send_keys(
                "test1234&")
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="submit"]').click()

        self.driver.get(f'{self.live_server_url}{reverse("profil")}')

        self.assertEqual(self.driver.current_url,
                         f'{self.live_server_url}{reverse("profil")}')

        # Click add training button
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[1]/div/div[2]/a/button").click()

        self.driver.find_element_by_xpath("/html/body/div/div[2]/a").click()

        self.assertEqual(
            self.driver.current_url,
            f'{self.live_server_url}{reverse("add_new_training")}')

        # Add a training (fill the form)
        curr_date = datetime.today().strftime('%Y-%m-%d')
        day_number = datetime.today().strftime("%w")

        self.driver.find_element_by_xpath(
            "/html/body/div/div/form/div[2]/input"
            ).send_keys(curr_date)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/form/div[3]/input").send_keys("100")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/form/div[4]/input").send_keys("200")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/form/div[6]/button").click()

        parent_elem = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div")
        child_elements = parent_elem.find_elements_by_xpath('.//*')
        for elem in child_elements:
            if day_number == 0:
                if (elem.text.startswith("Sunday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 1:
                if (elem.text.startswith("Monday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 2:
                if (elem.text.startswith("Tuesday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 3:
                if (elem.text.startswith("Wednesday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 4:
                if (elem.text.startswith("Thursday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 5:
                if (elem.text.startswith("Friday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break
            elif day_number == 6:
                if (elem.text.startswith("Saturday")):
                    text = elem.text.split("\n")
                    print(text)
                    self.assertEqual(text[1], "Recovery run")
                    self.assertIn("100", text[3])
                    self.assertIn("200", text[4])
                break


class WallOfFamePageTest(TestCase):
    def test_walloffame_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/walloffame/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/walloffame/"),
            "<title>Wall of fame</title>",
        )
