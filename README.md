# BALT-BEP Python Dashboard / Sales Report

This is the Render-ready Flask service for the BALT-BEP Admin Dashboard and Sales Report.

## Render settings

Build Command:
`pip install -r requirements.txt`

Start Command:
`gunicorn app:app`

## Environment variables

Set these on Render after the InfinityFree PHP API endpoints are created:

- `DASHBOARD_API_URL`
- `SALES_API_URL`

The PHP/MySQL system remains on InfinityFree. Render only serves the Python dashboard and sales report.
