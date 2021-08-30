from similarity import db


class Item(db.Model):
    __tablename__ = 'items_rank'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.String(), nullable=False)
    source_url = db.Column(db.String())
    category_id = db.Column(db.ForeignKey('entities_types.id'))
    category = db.relationship('Entity', backref=db.backref('items', lazy=True))
    rank = db.Column(db.Integer())
    rank_date = db.Column(db.Date())

    def __init__(self, id, description, source_url, category_id, rank, rank_date):
        self.id = id
        self.description = description
        self.source_url = source_url
        self.category_id = category_id
        self.rank = rank
        self.rank_date = rank_date

    def __rerp__(self):
        return f"""id: {self.id},
                   description: {self.description},
                   source_url: {self.source_url},
                   category_id: {self.category_id},
                   category: {self.category},
                   rank: {self.rank},
                   rank_date: {self.rank_date}
                   """


class Entity(db.Model):
    __tablename__ = 'entities_types'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category = db.Column(db.String(), nullable=False)
    source = db.Column(db.String())
    features_periodic = db.Column(db.JSON())
    features_realtime = db.Column(db.JSON())
    result_count = db.Column(db.Integer())

    def __init__(self, id, category, source, features_periodic,
                 features_realtime, result_count):
        self.id = id
        self.category = category
        self.source = source
        self.features_periodic = features_periodic
        self.features_realtime = features_realtime
        self.result_count = result_count

    def __repr__(self):
        return f'''
        id: {self.id},
        category: {self.category},
        features_periodic: {self.features_periodic},
        features_realtime: {self.features_realtime},
        result_count: {self.result_count}
        '''
