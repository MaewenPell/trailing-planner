from django.test import TestCase
from user_management.users import CreateNewUser
from user_profil.db_query import DBQuery


class TestDBQuery(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.data_login = {
            'username': "userT",
            "password": "test1234&"
        }

        cls.data_register = {
            'first_name': "user",
            'last_name': "test",
            'username': "userT",
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

    def test_create_user_sport_profil(self) -> None:
        self.assertTrue(self.res)
        res, sportProfil = DBQuery(self.user).get_user_profil()

        self.assertTrue(res)
        self.assertEqual(sportProfil['user']['first_name'], "user")
        self.assertEqual(sportProfil['user']['last_name'], "test")
        self.assertEqual(sportProfil['user']['email'], "email@test-user.com")
        self.assertEqual(sportProfil['user']['username'], "userT")
        self.assertEqual(sportProfil['final_objectif_deniv'], 1250)
        self.assertEqual(sportProfil['final_objectif_km'], 34)
        self.assertEqual(sportProfil['final_objectif_name'], "Test Run Name")
