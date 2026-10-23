# bahn-delays — project context

## What this is
Portfolio project #1 (of 3) for Paul, a CS bachelor student (VU Amsterdam, on Erasmus at LMU Munich until ~end of Feb 2027). Goal: land a working-student / junior AI or data role in Amsterdam from March 2027. Recruiters will look at this repo, so it must be clean, finished, and deployed.

Question: Which stations, lines and hours around Munich are most delay-prone, and can we predict whether a stop will be 6+ minutes late? (6 min = DB's own punctuality cutoff.)

## Data
- Source: Hugging Face dataset piebro/deutsche-bahn-data (CC BY 4.0, by Deutsche Bahn), monthly files monthly_processed_data/data-YYYY-MM.parquet
- Local: data/raw/data-2026-09.parquet (gitignored, large: never load the full month into pandas at once; read in batches or filter while reading)
- Columns: station_name, xml_station_name, eva, train_number, line_number (null for ICE/IC/EC), final_destination_station, delay_in_min, time, arrival_is_canceled, departure_is_canceled, train_type, train_line_ride_id, train_line_station_num, arrival_planned_time, arrival_change_time, departure_planned_time, departure_change_time, id
- Plan: filter to Munich-area stations before loading into Postgres

## Stack / environment
- Windows 11 + WSL2 Ubuntu 22.04, VS Code with WSL extension
- Python 3.10 managed with uv (always use uv add / uv run, never pip)
- Postgres 17 in Docker (docker-compose.yml, credentials in .env, never commit .env)
- SQLAlchemy + psycopg, pandas, pyarrow, scikit-learn, matplotlib, Jupyter
- Later: Streamlit dashboard, deployed publicly; stretch: scheduled ingest + dbt

## Structure
data/raw (gitignored) · notebooks/ · sql/ · src/ · docker-compose.yml · .env / .env.example · README.md

## Milestones
1. Week of 26 Oct: setup done (Docker, Postgres, uv, data downloaded, repo on GitHub) ✅
2. Week of 2 Nov: load Munich-area data into Postgres, explore in a notebook, 5–10 findings with charts
3. Week of 9 Nov: clean data + build a feature table in SQL (CTEs, window functions); one SQL script rebuilds it from scratch
4. Week of 16 Nov: data mining step (classification of 6+ min delays and/or clustering stations by delay profile), evaluated honestly with a metric + short write-up
5. Week of 23 Nov: Streamlit dashboard, deployed, README with screenshots

## How to help me
- I'm learning. I write the core parts myself: the SQL feature table, the pandas exploration, and the data mining step. For those, explain, give hints, and review my code; don't write them for me unless I explicitly ask.
- Boilerplate is fine to write: load scripts, config, Streamlit layout, Docker fixes, README drafts.
- Before writing code, briefly say what you'll do and why. Keep changes small so I can review the diff.
- Remind me to commit before big changes.
- Log notable AI contributions in AI_NOTES.md (what you generated, what I changed and why). It's interview material.
- Style: casual, direct, concise. Numbered steps for instructions. Code blocks must be copy-paste safe (no extra indentation).
