"""empty message

Revision ID: a90dc5c3cf20
Revises: 9eb45a2d4f4d
Create Date: 2023-01-03 23:28:50.774728

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a90dc5c3cf20'
down_revision = '9eb45a2d4f4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('brand_id')
        batch_op.drop_column('category')
        batch_op.drop_column('sale_num')
        batch_op.drop_column('seller_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seller_id', mysql.VARCHAR(length=255), nullable=False))
        batch_op.add_column(sa.Column('sale_num', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('category', mysql.VARCHAR(length=255), nullable=False))
        batch_op.add_column(sa.Column('brand_id', mysql.VARCHAR(length=255), nullable=False))

    # ### end Alembic commands ###