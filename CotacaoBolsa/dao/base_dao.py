import sqlalchemy as db

class BaseDao:
    def __init__(self, table):
        conector = 'mysql+mysqlconnector'
        user = 'topskills02'
        passwd = 'Maykon2019'
        hostname = 'mysql.topskills.study'
        port = 3306
        database = 'topskills02'
        engine = db.create_engine(f'{conector}://{user}:{passwd}@{hostname}:{port}/{database}')
        Session = db.orm.sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()
        self.table = table

    def list_all(self):
        return self.session.query(self.table).all()
    
    def get_by_id(self, id):
        return self.session.query(self.table).filter_by(id=id).first()
        # return self.session.query(self.table).get(id)


    def top(self, limit):
        return self.session.query(self.table).limit(limit).all()

    #----- Insert
    def insert(self, obj):
        self.session.add(obj)
        self.session.commit()

    #----- Delete
    def delete(self, id):
        obj = self.get_by_id(id)
        self.session.delete(obj)
        self.session.commit()

