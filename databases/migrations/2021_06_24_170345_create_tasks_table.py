"""CreateTasksTable Migration."""

from masoniteorm.migrations import Migration


class CreateTasksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tasks") as table:
            table.increments("id")
            table.string("type")
            table.string("name")
            table.text("data")
            table.string("status")
            table.timestamp("last_run", nullable=True)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("tasks")
