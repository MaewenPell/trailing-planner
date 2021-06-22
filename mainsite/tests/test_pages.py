from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    def test_landing_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get('').status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get(''),
            '<h1><a href="#hero">Trailing Planner</a></h1>')


class PlannerPageTest(SimpleTestCase):
    def test_planner_page_url_exists_at_desired_location(self) -> None:
        self.assertRedirects(
            self.client.get("/planner/"), "/users/register/",
            302, fetch_redirect_response=True)


class WallOfFamePageTest(SimpleTestCase):
    def test_walloffame_page_url_exists_at_desired_location(self) -> None:
        self.assertEquals(self.client.get("/walloffame/").status_code, 200)

    def test_view_contains_correct_html(self) -> None:
        self.assertContains(
            self.client.get("/walloffame/"),
            "<title>Wall of fame</title>",
        )
