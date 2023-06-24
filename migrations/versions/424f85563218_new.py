"""new

Revision ID: 424f85563218
Revises: 82fe06b132c1
Create Date: 2023-05-04 14:32:02.743155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '424f85563218'
down_revision = '82fe06b132c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('otp_secret', sa.String(length=16), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('otp_secret')

    # ### end Alembic commands ###