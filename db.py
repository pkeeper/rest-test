from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)
#                       ('postgresql://scott:tiger@localhost/mydatabase')
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    password = Column(String)
    #contactlist = relationship("Contacts")

    def __repr__(self):
        return "<User (username=%s, password=%s)>" % (self.username, self.password)

class Contacts(Base):
    __tablename__ = "contacts"
    contact_owner = Column(String, ForeignKey("users.username"), primary_key=True)
    #contact_owner_rel = relationship("User", backref="contactsr")
    contact = Column(String, ForeignKey("users.username"))

    def __repr__(self):
        return "<Contact %s of %s>" % (self.contact, self.contact_owner)


# Creating scheme if not created
User.metadata.create_all(engine)

u = User(username="keeper", password="f")
c = Contacts(contact_owner=u, contact=u)
