"""empty message

Revision ID: 486bf03989f3
Revises: None
Create Date: 2016-05-13 15:17:29.569354

"""

# revision identifiers, used by Alembic.
revision = '486bf03989f3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('family_name', sa.Text(), nullable=True),
    sa.Column('given_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint(u'id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
