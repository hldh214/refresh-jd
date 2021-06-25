"""CreateTaskLogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateTaskLogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("task_logs") as table:
            table.increments("id")
            table.unsigned_integer("task_id")
            table.text("response")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("task_logs")
