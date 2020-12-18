#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio, logging
import time
import uuid
import aiomysql

from orm import *

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id)
    email = StringField()
    passwd = StringField()
    admin = BooleanField()
    name = StringField()
    image = StringField()
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id)
    user_id = StringField()
    user_name = StringField()
    user_image = StringField()
    name = StringField()
    summary = StringField()
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id)
    blog_id = StringField()
    user_id = StringField()
    user_name = StringField()
    user_image = StringField()
    content = TextField()
    created_at = FloatField(default=time.time)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    async def test():
        await create_pool(user='root', password='123456', db='awesome', loop=loop)
        u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
        await u.save()
    loop.run_until_complete(test())

#    loop.close()

#    User1 = User(id=1,name='barry',depID=2,salary=17500)
 #   loop.run_until_complete(User1.save())

#    User1 = User(id=1,name='anson',depID=2,salary=13500)
#    loop.run_until_complete(User1.update())

#    User2 = User(id=1)
#    loop.run_until_complete(User2.remove())