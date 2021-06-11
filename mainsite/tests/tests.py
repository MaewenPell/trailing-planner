from user_management.users import CreateNewUser
from django.test import SimpleTestCase, TestCase


class HomePageTest(SimpleTestCase):

    def test_landing_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get('').status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get(''),
            '<h1><a href="#hero">Trailing Planner</a></h1>')


class PlannerPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/planner/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/planner/"),
            "<title>Planner</title>",
        )


class WallOfFamePageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/walloffame/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/walloffame/"),
            "<title>Wall of fame</title>",
        )


class ProfilPageTest(TestCase):
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
        cls.res, cls.msg, cls.user = CreateNewUser(
            cls.data_register).register()

    def test_profil_page_url_exists_at_desired_location(self) -> None:
        self.client.login(username="userT", password='test1234&')
        self.assertEquals(self.client.get("/profil/").status_code, 200)

    def test_view_profil_contains_correct_html(self) -> None:
        self.client.login(username="userT", password='test1234&')
        self.assertContains(
            self.client.get("/profil/"),
            "<title>Profil</title>",
        )

    def test_profil_page_redirect(self) -> None:
        self.assertEquals(self.client.get("/profil/").status_code, 302)
        self.assertRedirects(self.client.get("/profil/"), '/users/register/', status_code=302,
                             target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)
