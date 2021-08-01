from django.test import TestCase, Client
from user_management.users import CreateNewUser
from user_profil.db_query import DBQuery


class HomePageTest(TestCase):
    def test_landing_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get('').status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get(''),
            '<h1><a href="#hero">Trailing Planner</a></h1>')


class PlannerPageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data_login = {
            'username': "userT",
            "password": "test1234&"
        }
        cls.data_register = {
            'first_name': "user",
            'last_name': "test",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }

        cls.new_training = {
            'trainingDate': "2021-08-01",
            'trainingType': 'Test Training',
            'trainingKm': 20,
            'trainingD': 1000,
            'trainingComments': 'Test comments',
            'status': True
        }

        cls.res, cls.msg, cls.user = CreateNewUser(
            cls.data_register).register()

        sport_profil = {}
        sport_profil['objectifName'] = "Test Run Name"
        sport_profil['objectifDistance'] = 34
        sport_profil['objectifD'] = 1250
        sport_profil['objectifDate'] = "2021/06/17"
        sport_profil['stravaLink'] = "test.stravalink.com"

        cls.res, cls.sportProfilObject = DBQuery(
            cls.user).create_sport_profil(sport_profil)

        cls.curr_user = DBQuery(cls.user)
        res, cls.sportProfil = cls.curr_user.get_user_profil()
        cls.curr_user.create_training(cls.new_training)
        cls.c = Client()
        cls.c.post(
            '/users/login-user/',
            {'username': "userT", 'password': 'test1234&'})

    def test_planner_page_url_exists_at_desired_location(self) -> None:
        self.assertRedirects(
            self.client.get("/planner/"), "/users/register/",
            302, fetch_redirect_response=True)

    def test_planner_context_correcct(self) -> None:
        data = self.c.get("/planner/").context.flatten()
        self.assertIsNotNone(data["sport_profil"])
        self.assertIsNotNone(data["trainings"])


class WallOfFamePageTest(TestCase):
    def test_walloffame_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/walloffame/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/walloffame/"),
            "<title>Wall of fame</title>",
        )
