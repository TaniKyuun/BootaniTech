from datetime import datetime
from typing import Optional

from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class user_credentials(UserMixin, db.Model):
    id: Mapped[int] = Column(Integer, primary_key=True)
    user_firstname: Mapped[str] = Column(String(64), index=True)
    user_lastname: Mapped[str] = Column(String(64), index=True)
    user_email: Mapped[str] = Column(String(120), index=True, unique=True)
    user_password: Mapped[Optional[str]] = Column(String(256))
    user_in_company: Mapped[bool] = Column(Boolean, default=False)
    user_company: Mapped[Optional[str]] = Column(String(128))

    def __repr__(self):
        return "<Email {}>".format(self.user_email)

    def set_password(self, password):
        self.user_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)


@login.user_loader
def load_user(id):
    return db.session.get(user_credentials, int(id))


class pestisafe_data(db.Model):
    id: Mapped[int] = Column(Integer, primary_key=True)
    data_result: Mapped[int] = Column(Integer())
    data_submitter: Mapped[int] = Column(ForeignKey(user_credentials.id), index=True)
    file_date = db.Column(DateTime)
    file_hash: Mapped[str] = Column(String(64), index=True)
    file_in_company: Mapped[bool] = Column(
        ForeignKey(user_credentials.user_in_company), default=False
    )
    file_company: Mapped[Optional[str]] = Column(
        String(128),
        ForeignKey(user_credentials.user_company),
    )


class pestisafe_result(db.Model):
    id: Mapped[int] = Column(Integer, primary_key=True)
    result_description: Mapped[str] = Column(String(256))


class pestisafe_history(db.Model):
    id: Mapped[int] = Column(Integer, primary_key=True)
    data_result: Mapped[int] = Column(
        ForeignKey(pestisafe_data.data_result), index=True
    )
    data_submitter: Mapped[int] = Column(ForeignKey(pestisafe_data.data_submitter))
    result_description: Mapped[int] = Column(
        ForeignKey(pestisafe_result.result_description)
    )
    file_date: Mapped[datetime] = Column(ForeignKey(pestisafe_data.file_date))
    file_hash: Mapped[str] = Column(ForeignKey(pestisafe_data.file_hash))
