"""empty message

Revision ID: e13af5d7b054
Revises: a9d7e9bfbdd9
Create Date: 2023-01-02 04:46:35.011643

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e13af5d7b054'
down_revision = 'a9d7e9bfbdd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=45),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=45),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_index('username')
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('username', ['username'], unique=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=45),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=45),
               existing_nullable=False)
        batch_op.drop_column('email')

    # ### end Alembic commands ###