from flask_fixtures import FixturesMixin
from similarity import create_app, db, TestingConfig
from similarity.models import Item, Entity
from flask_testing import TestCase


class BaseTest(TestCase):

    def create_app(self):

        # pass in test configuration
        return create_app(TestingConfig)

    def setUp(self):

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        # This is an ugly workaround to avoid the next error:
        # "AssertionError: Popped wrong app context."
        self._ctx = None


class TestDBCAlls(FixturesMixin, BaseTest):
    db = db
    fixtures = [
        'fixtures/entity.json',
        # 'fixtures/item.json',
    ]

    def test_number_of_entites(self):
        entities = Entity.query.all()
        assert len(entities) == Entity.query.count() == 3

    # def test_number_of_items(app):
    #     items = Item.query.all()
    #     assert len(items) == Item.query.count() == 1
