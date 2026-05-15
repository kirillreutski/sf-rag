"""
Create the DB table and search function for one guide.

Usage:
    python setup_guide.py apex          # table: apex_chunks, fn: search_apex
    python setup_guide.py lwc           # table: lwc_chunks,  fn: search_lwc
    python setup_guide.py aura          # table: aura_chunks, fn: search_aura

Environment variables (set in .env):
    PG_CONNECTION_STRING  postgresql://user:pass@host:5432/dbname
"""

import argparse
import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TEMPLATE = Path(__file__).parent / "setup_db.sql"


def main(guide: str) -> None:
    table = f"{guide}_chunks"
    sql = TEMPLATE.read_text().replace("{GUIDE}", guide).replace("{TABLE}", table)

    conn = psycopg2.connect(os.environ["PG_CONNECTION_STRING"])
    conn.autocommit = True
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
        print(f"Created table '{table}' and function 'search_{guide}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("guide", help="Guide name: apex | lwc | aura")
    args = parser.parse_args()
    main(args.guide)
