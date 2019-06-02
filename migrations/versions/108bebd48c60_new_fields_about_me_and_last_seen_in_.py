"""new fields about_me and last_seen in user m model

Revision ID: 108bebd48c60
Revises: c87fff70b0b0
Create Date: 2019-06-02 22:50:18.749691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '108bebd48c60'
down_revision = 'c87fff70b0b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
