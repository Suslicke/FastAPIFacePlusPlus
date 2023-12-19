"""update ImageModel and create FaceModel

Revision ID: d4894f8adb07
Revises: 99b6c350812a
Create Date: 2023-12-19 17:53:39.700680

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd4894f8adb07'
down_revision = '99b6c350812a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('image_id', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('image_id'),
    sa.UniqueConstraint('image_id')
    )
    op.create_table('faces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('face_token', sa.String(), nullable=True),
    sa.Column('face_rectangle', sa.JSON(), nullable=True),
    sa.Column('image_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['images.image_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('image')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('image_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('file_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('faces_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('face_rectangle', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('image_id', name='image_pkey')
    )
    op.drop_table('faces')
    op.drop_table('images')
    # ### end Alembic commands ###