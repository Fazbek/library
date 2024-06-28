from datetime import datetime
from database import get_db
from .models import User


# Users, done
def create_user_db(username, phone_number, password, email):
    db = next(get_db())
    new_user = User(username=username, phone_number=phone_number, password=password, email=email)
    db.add(new_user)
    db.commit()
    return "User successfully created!"


# done
def get_all_users_db():
    db = next(get_db())
    users = db.query(User).all()
    return users


def get_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        return user
    return "User not found"


def update_user_db(id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        try:
            if change_info == "username":
                user.username = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "email":
                user = db.query(User).filter_by(email=new_info).first()
                if user:
                    return "This email is already in use"
                else:
                    user.email = new_info
                    db.commit()
                    return "Successfully changed"
            elif change_info == "phone_number":
                user = db.query(User).filter_by(phone_number=new_info).first()
                if user:
                    return "This phone_number is already in use"
                else:
                    user.phone_number = new_info
                    db.commit()
                    return "Successfully changed"
            elif change_info == "password":
                user.password = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


def delete_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        db.delete(user)
        db.commit()
        return "User successfully deleted!"
    return "User not found"


def activate_user_db(id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        user.is_active = True
        db.commit()
        return "User activated successfully."
    return "User not found."


def deactivate_user_db(id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        user.is_active = False
        db.commit()
        return "User deactivated successfully."
    return "User not found."
