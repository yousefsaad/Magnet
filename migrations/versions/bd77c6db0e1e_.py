"""empty message

Revision ID: bd77c6db0e1e
Revises: db84e13387cb
Create Date: 2016-10-21 20:15:25.535576

"""

# revision identifiers, used by Alembic.
revision = 'bd77c6db0e1e'
down_revision = 'db84e13387cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('date_in', sa.Date(), nullable=True),
    sa.Column('date_out', sa.Date(), nullable=True),
    sa.Column('members', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('phone_num', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_num', sa.String(length=30), nullable=True),
    sa.Column('room_type', sa.String(length=40), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('room_num')
    )
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_in', sa.Date(), nullable=True),
    sa.Column('date_out', sa.Date(), nullable=True),
    sa.Column('members', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reserved',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reserve_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reserve_id'], ['reservation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserved')
    op.drop_table('search')
    op.drop_table('room')
    op.drop_table('reservation')
    ### end Alembic commands ###
