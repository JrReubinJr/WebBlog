__author__ = "JrReubinJr"

import uuid
import datetime
from src.common.database import Database
from src.models.post import Post


class Blog(object):
    def __init__(self, author, author_id, title, description,  _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    date_created=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author':self.author,
            'author_id':self.author_id,
            'title':self.title,
            'description':self.description,
            '_id':self._id
        }

    @classmethod
    def from_mongo(cls, id):
        print(id)
        blog_data = Database.find_one(collection='blogs',
                                       query={'_id':id})
        print(blog_data == None)
        print(blog_data)
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        print("Author: {}".format(author_id))
        blogs = Database.find(collection='blogs',
                              query={'author_id': author_id})
        return [cls(**blog) for blog in blogs]