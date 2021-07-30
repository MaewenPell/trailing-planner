from django.test import TestCase
from user_management.users import CreateNewUser
from user_profil.db_query import DBQuery
from mainsite.utils import (
    generate_running_data, get_index_data, get_top_runners)


class TestUtilsfunctions(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.data_register = {
            'first_name': "user",
            'last_name': "test",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }

        cls.data_register_2 = {
            'first_name': "user2",
            'last_name': "test2",
            'email': "email@test-user2.com",
            'password': "test1234&",
            're_password': "test1234&"
        }

        cls.data_register_3 = {
            'first_name': "user3",
            'last_name': "test3",
            'email': "email@test-user3.com",
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

        cls.new_training_2 = {
            'trainingDate': "1111-02-10",
            'trainingType': 'Test Training 2',
            'trainingKm': 30,
            'trainingD': 2000,
            'trainingComments': 'Test comments 2',
            'status': True
        }

        cls.new_training_2_1 = {
            'trainingDate': "2021-08-01",
            'trainingType': 'Test Training',
            'trainingKm': 21,
            'trainingD': 1000,
            'trainingComments': 'Test comments',
            'status': True
        }

        cls.new_training_2_2 = {
            'trainingDate': "1111-02-10",
            'trainingType': 'Test Training 2',
            'trainingKm': 31,
            'trainingD': 2000,
            'trainingComments': 'Test comments 2',
            'status': True
        }

        cls.new_training_3_1 = {
            'trainingDate': "2021-08-01",
            'trainingType': 'Test Training',
            'trainingKm': 30,
            'trainingD': 1000,
            'trainingComments': 'Test comments 3',
            'status': True
        }

        cls.new_training_3_2 = {
            'trainingDate': "1111-02-10",
            'trainingType': 'Test Training 3',
            'trainingKm': 40,
            'trainingD': 2000,
            'trainingComments': 'Test comments 3',
            'status': True
        }

        cls.res, cls.msg, cls.user = CreateNewUser(
            cls.data_register).register()

        cls.res_2, cls.msg_2, cls.user_2 = CreateNewUser(
            cls.data_register_2).register()

        cls.res_3, cls.msg_3, cls.user_3 = CreateNewUser(
            cls.data_register_3).register()

        sport_profil = {}

        sport_profil['objectifName'] = "Test Run Name"
        sport_profil['objectifDistance'] = 34
        sport_profil['objectifD'] = 1250
        sport_profil['objectifDate'] = "2021/06/17"
        sport_profil['stravaLink'] = "test.stravalink.com"

        cls.res, cls.sportProfilObject = DBQuery(
            cls.user).create_sport_profil(sport_profil)

        cls.res_2, cls.sportProfilObject_2 = DBQuery(
            cls.user_2).create_sport_profil(sport_profil)

        cls.res_3, cls.sportProfilObject_3 = DBQuery(
            cls.user_3).create_sport_profil(sport_profil)

        cls.curr_user = DBQuery(cls.user)
        res, cls.sportProfil = cls.curr_user.get_user_profil()
        cls.curr_user.create_training(cls.new_training)
        cls.curr_user.create_training(cls.new_training_2)

        cls.curr_user_2 = DBQuery(cls.user_2)
        res, cls.sportProfil = cls.curr_user_2.get_user_profil()
        cls.curr_user_2.create_training(cls.new_training_2_1)
        cls.curr_user_2.create_training(cls.new_training_2_2)

        cls.curr_user_3 = DBQuery(cls.user_3)
        res, cls.sportProfil = cls.curr_user_3.get_user_profil()
        cls.curr_user_3.create_training(cls.new_training_3_1)
        cls.curr_user_3.create_training(cls.new_training_3_2)

    def test_generate_running_date_are_correct(self):
        trainings = self.curr_user.get_all_trainings()
        data = generate_running_data(self.sportProfil, trainings)

        self.assertEqual(sum(data["all_km"]), 50)
        self.assertEqual(sum(data["all_deniv"]), 3000)
        self.assertEqual(data["trainings"]['0'].trainingDateDayStr, '7')

    def test_get_index_data_are_correct(self):
        res = get_index_data()
        self.assertEqual(res["nb_runners"], 3)
        self.assertEqual(res["km_ran"], 172)
        self.assertEqual(res["elevation_gained"], 9000)

    def test_get_top_runners(self):
        top_runners = get_top_runners()
        self.assertEqual(top_runners["first"], {
            'name': 'user3',
            'km_ran': 70
        })
        self.assertEqual(top_runners["second"], {
            'name': 'user2',
            'km_ran': 52
        })
        self.assertEqual(top_runners["third"], {
            "name": 'user',
            'km_ran': 50,
        })


# 'first': {'name': 'user2', 'km_ran': 52}, 
# 'second': {'name': 'user', 'km_ran': 50}, 
# 'third': {'name': '', 'km_ran': 0}}
