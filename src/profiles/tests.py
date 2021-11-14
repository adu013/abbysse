# profiles/tests.py
from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuserabbysse',
            password='@c@7x:}sgvarM623',
            email='testuserabbysse@abbysse.com'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='testuserabbysse', password='@c@7x:}sgvarM623')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='notatestuserabbysse', password='@c@7x:}sgvarM623')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='testuserabbysse', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)
