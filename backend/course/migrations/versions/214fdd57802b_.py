"""empty message

Revision ID: 214fdd57802b
Revises: f534cc5cab3f
Create Date: 2020-08-13 17:13:24.377779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '214fdd57802b'
down_revision = 'f534cc5cab3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('announce', 'status')
    op.drop_column('answer', 'status')
    op.drop_column('assignment', 'status')
    op.drop_column('course', 'status')
    op.drop_column('course_resource', 'status')
    op.drop_column('discussion_answer', 'status')
    op.drop_column('discussion_topic', 'status')
    op.drop_column('enroll', 'status')
    op.drop_column('history', 'status')
    op.drop_column('history_answer', 'status')
    op.drop_column('history_question', 'status')
    op.drop_column('question', 'status')
    op.drop_column('question_up_vote', 'status')
    op.drop_column('schedule', 'status')
    op.drop_column('tag', 'status')
    op.drop_column('user', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('schedule', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('question_up_vote', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('question', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('history_question', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('history_answer', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('history', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('enroll', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('discussion_topic', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('discussion_answer', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('course_resource', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('course', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('assignment', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('answer', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.add_column('announce', sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    # ### end Alembic commands ###