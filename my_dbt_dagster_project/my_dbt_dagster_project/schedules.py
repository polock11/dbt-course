"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster import DefaultScheduleStatus
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import airbnb_dbt_assets
from .project import airbnb_project

schedules = [
     build_schedule_from_dbt_selection(
         [airbnb_dbt_assets],
         job_name="materialize_dbt_models",
         cron_schedule="0 0 * * *",
         dbt_select="fqn:*",
     ),
     build_schedule_from_dbt_selection(
         [airbnb_dbt_assets],
         job_name="materialize_fct_reviews",
         cron_schedule="0 13 * * *",
         dbt_select="+fct_reviews",
         execution_timezone="Europe/Helsinki",
         default_status=DefaultScheduleStatus.RUNNING,
     ),
     build_schedule_from_dbt_selection(
         [airbnb_dbt_assets],
         job_name="materialize_mart_full_moon_review",
         cron_schedule="15 13 * * *",
         dbt_select="+mart_full_moon_review",
         execution_timezone="Europe/Helsinki",
         default_status=DefaultScheduleStatus.RUNNING,
     ),
     build_schedule_from_dbt_selection(
         [airbnb_dbt_assets],
         job_name="prod_materialize_mart_full_moon_review",
         cron_schedule="15 13 * * *",
         dbt_select="+mart_full_moon_review",
         execution_timezone="Europe/Helsinki",
         config={
             "resources": {
                 "dbt": {
                     "config": {
                         "project_dir": str(airbnb_project.project_dir),
                         "target": "prod",
                     }
                 }
             }
         },
         default_status=DefaultScheduleStatus.RUNNING,
     ),
]
