from app import session
from app.ebaymmsg.models import EbaySellers


def addtodatabase(username):
    try:
        new_person = EbaySellers(username=username)
        session.add(new_person)
        session.commit()
        print("successfully committed")
    except Exception as e:
        print(str(e))
        session.rollback()
