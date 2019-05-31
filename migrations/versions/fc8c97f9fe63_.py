"""empty message

Revision ID: fc8c97f9fe63
Revises: ed8f3e3aafbd
Create Date: 2019-05-31 20:36:00.640637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8c97f9fe63'
down_revision = 'ed8f3e3aafbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ui_report_log',
    sa.Column('id', sa.String(length=30), nullable=False),
    sa.Column('equipment_id', sa.String(length=30), nullable=True),
    sa.Column('class_', sa.String(length=10), nullable=False),
    sa.Column('U1', sa.Float(), nullable=False),
    sa.Column('U2', sa.Float(), nullable=False),
    sa.Column('U3', sa.Float(), nullable=False),
    sa.Column('I1', sa.Float(), nullable=False),
    sa.Column('I2', sa.Float(), nullable=False),
    sa.Column('I3', sa.Float(), nullable=False),
    sa.Column('J1', sa.Float(precision='8,4'), nullable=False),
    sa.Column('T1', sa.Float(), nullable=False),
    sa.Column('T2', sa.Float(), nullable=False),
    sa.Column('T3', sa.Float(), nullable=False),
    sa.Column('T4', sa.Float(), nullable=False),
    sa.Column('L1', sa.Float(), nullable=False),
    sa.Column('report_time', sa.DateTime(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('modify_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ui_report_log')
    # ### end Alembic commands ###
