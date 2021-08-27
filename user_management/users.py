from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from random import randint


class CreateNewUser():
    def __init__(self, data: dict):
        self.inputs = []
        self.error_list = []
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.re_password = data['re_password']

        # if self.first_name != "" and self.last_name != "":
        #     self.user_name = self._create_user_name(False)

    def _check_no_empty_field(self) -> bool:
        for elem in (self.first_name, self.last_name, self.email,
                     self.username, self.password, self.re_password):
            if elem == "":
                self.error_list.append("Some field are empty")
                return False
            else:
                self.inputs.append(elem)
        return True

    def _inputs_are_correct(self) -> bool:
        if len(self.first_name) < 2 or len(self.last_name) < 2:
            self.error_list.append(
                "First name or Last name is too short (2 char min)")
        if (len(self.first_name) > 148 or len(self.last_name) > 150):
            self.error_list.append(
                "First name or last name is too long (150 char max)")
        if self.password != self.re_password:
            self.error_list.append("Password don't match")

        if len(self.password) >= 8:
            if self.password.isalnum():
                self.error_list.append(
                    "Password must coutain at least a special character")
        else:
            self.error_list.append(
                "Password must contain at least 8 characters")

        if len(self.error_list) > 0:
            return False
        return True

    def register(self) -> tuple:
        res_not_empty = self._check_no_empty_field()
        if res_not_empty:
            res_inputs = self._inputs_are_correct()
            if res_inputs:
                try:
                    new_user = User.objects.create_user(
                        self.username, self.email, self.password)
                    new_user.last_name = self.last_name
                    new_user.first_name = self.first_name
                    new_user.save()
                except IntegrityError:
                    pass
                    # if ('username' in e.args[0]):
                    #     # self.user_name = self._create_user_name(True)
                    #     self.register()
                return (True, "", new_user)
        return (False, self.error_list, None)

    # def _create_user_name(self, nb: bool) -> str:
    #     gen_user_name = self.first_name + self.last_name[0].upper()
    #     if nb:
    #         gen_user_name = f"{gen_user_name}{randint(1, 99)}"
    #     return f"{gen_user_name}"


class ConnectUser():
    def __init__(self, data: dict):
        self.username = data['username']
        self.password = data["password"]

    def connect(self, request) -> tuple:
        user = authenticate(request,
                            username=self.username,
                            password=self.password)
        if user is not None:
            login(request, user)
            return (True, "")
        else:
            return (False, "Authentification failed")
