from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"

    @validates("content")
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("the content is too short, input at least 250 characters")
        else:
            return content

    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError(
                "summary too long, please make it less than 250 characters"
            )
        else:
            return summary

    @validates("category")
    def validate_category(self, key, category):
        category_list = ["Fiction", "Non-Fiction"]

        if category not in category_list:
            raise ValueError("please enter a valid category")
        else:
            return category

    @validates("title")
    def validate_title(self, key, title):
        title_list = ["Won't Believe", "Secret", "Top", "Guess"]
        if title not in title_list:
            raise ValueError("enter a valid title")
        else:
            return title

class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"

    @validates("name")
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError("Invalid name, please enter the whole name")
        else:
            return name

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("please enter a valid phone number")
        else:
            return phone_number

