"""recreate classroom and student tables

Revision ID: 9d9f28055a65
Revises: 
Create Date: 2018-11-03 21:50:59.936573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d9f28055a65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instructor', sa.String(length=140), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classroom_active'), 'classroom', ['active'], unique=False)
    op.create_index(op.f('ix_classroom_instructor'), 'classroom', ['instructor'], unique=False)
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['classroom.id'], ),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_index(op.f('ix_classroom_instructor'), table_name='classroom')
    op.drop_index(op.f('ix_classroom_active'), table_name='classroom')
    op.drop_table('classroom')
    # ### end Alembic commands ###
