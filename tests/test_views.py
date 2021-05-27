from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):

    def test_landing_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get('').status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get(''),
            '<h1><a href="#hero">Trailing Planner</a></h1>')


class RegisterPageTest(SimpleTestCase):
    def test_register_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/register/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/register/"),
            '<h2 class="form-title">Create account</h2>'
        )


class LoginPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/login/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/login/"),
            'Account Login'
        )


class ProfilPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/profil/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/profil/"),
            "<title>Profil</title>",
        )


class CommunityPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/community/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/community/"),
            "<title>Community</title>",
        )


class PlannerPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/planner/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/planner/"),
            "<title>Planner</title>",
        )
