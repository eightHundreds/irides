import pytest
from app import models
from app.extensions import db


@pytest.fixture(scope='function')
def mock_picture():


    def make_mock_picture(user=None, despriction=None, address=None):


        _picture = models.Picture(
            userId=str(user.id),
            despriction=despriction or 'testdes',
            address=address or 'testaddress'
        )

        _picture.tags = [
            models.Tags(tag='testtags')
        ]

        db.session.add(_picture)
        db.session.commit()

        # _tags = models.Tags(
        #     picId=_picture.id,
        #     tag='testtag'
        # )
        # db.session.add(_tags)
        # db.session.commit()
        return _picture

    return make_mock_picture
