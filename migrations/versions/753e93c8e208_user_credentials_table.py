"""user_credentials table

Revision ID: 753e93c8e208
Revises:
Create Date: 2024-03-25 20:40:39.592655

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "753e93c8e208"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pestisafe_result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("result_description", sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_credentials",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_firstname", sa.String(length=64), nullable=True),
        sa.Column("user_lastname", sa.String(length=64), nullable=True),
        sa.Column("user_email", sa.String(length=120), nullable=True),
        sa.Column("user_password", sa.String(length=256), nullable=True),
        sa.Column("user_in_company", sa.Boolean(), nullable=True),
        sa.Column("user_company", sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("user_credentials", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_user_credentials_user_email"), ["user_email"], unique=True
        )
        batch_op.create_index(
            batch_op.f("ix_user_credentials_user_firstname"),
            ["user_firstname"],
            unique=False,
        )
        batch_op.create_index(
            batch_op.f("ix_user_credentials_user_lastname"),
            ["user_lastname"],
            unique=False,
        )

    op.create_table(
        "pestisafe_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_result", sa.Integer(), nullable=True),
        sa.Column("data_submitter", sa.Integer(), nullable=True),
        sa.Column("file_date", sa.DateTime(), nullable=True),
        sa.Column("file_hash", sa.String(length=64), nullable=True),
        sa.Column("file_in_company", sa.Boolean(), nullable=True),
        sa.Column("file_company", sa.String(length=128), nullable=True),
        sa.ForeignKeyConstraint(
            ["data_submitter"],
            ["user_credentials.id"],
        ),
        sa.ForeignKeyConstraint(
            ["file_company"],
            ["user_credentials.user_company"],
        ),
        sa.ForeignKeyConstraint(
            ["file_in_company"],
            ["user_credentials.user_in_company"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("pestisafe_data", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_pestisafe_data_data_submitter"),
            ["data_submitter"],
            unique=False,
        )
        batch_op.create_index(
            batch_op.f("ix_pestisafe_data_file_hash"), ["file_hash"], unique=False
        )

    op.create_table(
        "pestisafe_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_result", sa.Integer(), nullable=True),
        sa.Column("data_submitter", sa.Integer(), nullable=True),
        sa.Column("result_description", sa.String(length=256), nullable=True),
        sa.Column("file_date", sa.DateTime(), nullable=True),
        sa.Column("file_hash", sa.String(length=64), nullable=True),
        sa.ForeignKeyConstraint(
            ["data_result"],
            ["pestisafe_data.data_result"],
        ),
        sa.ForeignKeyConstraint(
            ["data_submitter"],
            ["pestisafe_data.data_submitter"],
        ),
        sa.ForeignKeyConstraint(
            ["file_date"],
            ["pestisafe_data.file_date"],
        ),
        sa.ForeignKeyConstraint(
            ["file_hash"],
            ["pestisafe_data.file_hash"],
        ),
        sa.ForeignKeyConstraint(
            ["result_description"],
            ["pestisafe_result.result_description"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("pestisafe_history", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_pestisafe_history_data_result"),
            ["data_result"],
            unique=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("pestisafe_history", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_pestisafe_history_data_result"))

    op.drop_table("pestisafe_history")
    with op.batch_alter_table("pestisafe_data", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_pestisafe_data_file_hash"))
        batch_op.drop_index(batch_op.f("ix_pestisafe_data_data_submitter"))

    op.drop_table("pestisafe_data")
    with op.batch_alter_table("user_credentials", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_credentials_user_lastname"))
        batch_op.drop_index(batch_op.f("ix_user_credentials_user_firstname"))
        batch_op.drop_index(batch_op.f("ix_user_credentials_user_email"))

    op.drop_table("user_credentials")
    op.drop_table("pestisafe_result")
    # ### end Alembic commands ###