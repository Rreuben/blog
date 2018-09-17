"""Initial other migration

Revision ID: 436ebd4b546d
Revises: aee15ef163ae
Create Date: 2018-09-17 16:21:04.565200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '436ebd4b546d'
down_revision = 'aee15ef163ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_name', table_name='roles')
    op.drop_table('roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.create_index('ix_roles_name', 'roles', ['name'], unique=False)
    # ### end Alembic commands ###
