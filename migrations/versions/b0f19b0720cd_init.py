"""Init

Revision ID: b0f19b0720cd
Revises: 
Create Date: 2024-08-30 17:39:51.287976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b0f19b0720cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', mysql.CHAR(length=36), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('role', mysql.VARCHAR(length=255), server_default='user', nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('update_at', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('books',
    sa.Column('uid', mysql.CHAR(length=36), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('author', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('publisher', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('published_date', sa.DATE(), nullable=False),
    sa.Column('page_count', sa.INTEGER(), nullable=False),
    sa.Column('language', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('user_uid', mysql.CHAR(length=36), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('update_at', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['user_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('users')
    # ### end Alembic commands ###
