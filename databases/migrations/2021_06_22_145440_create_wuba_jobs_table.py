"""CreateWubaJobsTable Migration."""

from masoniteorm.migrations import Migration


class CreateWubaJobsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wuba_jobs") as table:
            table.increments("id")
            table.string("name")
            table.string("run_every")
            table.text("cookie")
            table.string("zp_id")
            table.text("zp_post_data")
            table.string("status")
            table.timestamp("last_run", nullable=True)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("wuba_jobs")
