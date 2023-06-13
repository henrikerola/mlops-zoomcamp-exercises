https://github.com/henrikerola/mlops-zoomcamp-homework-3


# Q1. Human-readable name

    conda create -n homework-3 python==3.9.12
    conda activate homework-3
    pip install -r requirements.txt
    prefect server start
    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api



https://docs.prefect.io/2.10.13/api-ref/prefect/tasks/

Correct answer: `@task(retries=3, retry_delay_seconds=2, name="Read taxi data")`

# Q2. Cron

    prefect project init
    prefect deploy orchestrate.py:main_flow -n homework-3 -p zoompool
    prefect worker start -p zoompool


Answer: `0 9 3 * *`

# Q3. RMSE

Answer: `5.19931`

# Q4. RMSE (Markdown Artifact)

Answer:  `5.37`

# Q5. Emails

Answer: `email_send_message`

# Q6. Prefect Cloud

Answer: `Action`






