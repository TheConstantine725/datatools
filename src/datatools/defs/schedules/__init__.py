from dagster import ScheduleDefinition

clickhouse_elt_schedule = ScheduleDefinition(cron_schedule="55 1 * * *",
    execution_timezone="Europe/Athens",job_name="clickhouse_elt_job", name = "midnight_run")
