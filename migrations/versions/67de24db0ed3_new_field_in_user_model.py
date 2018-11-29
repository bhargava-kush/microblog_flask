"""new field in user model

Revision ID: 67de24db0ed3
Revises: 626ecae93860
Create Date: 2018-11-29 13:20:35.989576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67de24db0ed3'
down_revision = '626ecae93860'
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
