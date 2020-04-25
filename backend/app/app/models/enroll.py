from sqlalchemy import Column, String, ForeignKey, Table

enroll_table = Table('association',
                     Column('user_id', String(10), ForeignKey('User.id')),
                     Column('course_id', String(15), ForeignKey('Course.id')))
