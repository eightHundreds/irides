from app.models import InitDataGenerator, User, Picture
from .. import clear_db
import pytest


@pytest.fixture
def generator(db):
    return InitDataGenerator()


class TestDataGenerator(object):

    def test_datagenerator_user(self, generator):
        generator.init_user()
        user_in_db = User.query.filter(User.username == generator.mock_user.username).first()

        assert (user_in_db != None) == True

    def test_datagenerator_pic(self,generator):
        generator.init_picture()
        first_pic_des = generator.mock_pictures[0].despriction
        pic_in_db = Picture.query.filter(Picture.despriction == first_pic_des).first()

        assert pic_in_db
