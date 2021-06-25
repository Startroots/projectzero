import datetime

from google.cloud import bigquery
import pandas
import pytz
import openpyxl

df = pandas.read_excel('test1.xlsx')

client = bigquery.Client()
table_id = "projectzero-317519.data.table1"
project_id = "projectzero-317519"    


job_config = bigquery.LoadJobConfig(
    # Specify a (partial) schema. All columns are always written to the
    # table. The schema is used to assist in data type definitions.
    schema=[
        # Specify the type of columns whose type cannot be auto-detected. For
        # example the "title" column uses pandas dtype "object", so its
        # data type is ambiguous.
        bigquery.SchemaField("Title", bigquery.enums.SqlTypeNames.STRING),
        # Indexes are written if included in the schema by name.
        bigquery.SchemaField("Function", bigquery.enums.SqlTypeNames.STRING),
    ],
    # Optionally, set the write disposition. BigQuery appends loaded rows
    # to an existing table by default, but with WRITE_TRUNCATE write
    # disposition it replaces the table with the loaded data.
    write_disposition="WRITE_TRUNCATE",
)


job = client.load_table_from_dataframe(
    df, table_id, job_config=job_config
)  # Make an API request.
job.result()  # Wait for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)