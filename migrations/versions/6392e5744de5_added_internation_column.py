"""added internation column

Revision ID: 6392e5744de5
Revises: cef06cdc17fe
Create Date: 2022-10-02 19:42:29.799010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6392e5744de5'
down_revision = 'cef06cdc17fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email_address', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('occupation', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
