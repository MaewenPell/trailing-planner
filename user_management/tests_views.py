from django.test import SimpleTestCase
import django

django.setup()


class RegisterPageTest(SimpleTestCase):
    def test_register_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/users/register/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/users/register/"),
            '<h2 class="form-title">Create account</h2>'
        )


class LoginPageTest(SimpleTestCase):
    def test_login_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/users/login/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/users/login/"),
            'Account Login'
        )
