from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    def print_as_string(self):
        return '{name: '+self.name+' quantity: '+str(self.quantity)+' description: '+self.description+' date_added: '+str(self.date_added)+'}'
