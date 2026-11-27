# 🐍 Python for Data Engineering

My learning journey from Python beginner to junior data engineer, focused on the skills data engineering and data analyst roles ask for: **Python, SQL, dbt, Airflow, Docker, cloud and CI/CD**.

Everything builds towards a capstone project: **a pipeline that recommends weekend train trips in the Netherlands** 🚆

---

## 🎯 Capstone: Best weekend trips by train

Every Friday, the pipeline answers:
> *Which destinations within X hours of my home station are worth visiting this weekend?*

It ranks destinations by **weather forecast, travel time, disruptions and things to do**.

**Planned architecture**
```
NS API, Open-Meteo (KNMI), OpenStreetMap
        │  Python extractors
        ▼
raw (Parquet) → DuckDB / PostgreSQL → dbt (staging → marts)
        │  orchestrated by Airflow, running in Docker
        ▼
weekend recommendations dashboard

Live NS disruptions → Kafka/Redpanda → disruptions table
GitHub Actions: tests on every push, automated deploys
```

---

## 🧰 Tech stack

| Area | Tools |
|---|---|
| Language | Python 3.12, SQL |
| Environment | uv, VS Code, Jupyter |
| Data | DuckDB, PostgreSQL, pandas, Polars |
| Pipelines | dbt, Apache Airflow, Kafka/Redpanda |
| Engineering | Git, GitHub Actions, pytest, ruff, Docker |
| Cloud | Azure, Databricks / PySpark |

---

## 📁 Repository structure

```
python-de/
├── lessons/          # one folder per lesson: exercises + my notes
├── data/             # small practice datasets
├── src/python_de/    # reusable code that grows into the capstone
├── pyproject.toml    # project definition and dependencies
└── uv.lock           # exact dependency versions
```

---

## ▶️ How to run

```bash
git clone https://github.com/<your-username>/python-de.git
cd python-de
uv sync                                              # rebuild the environment
uv run lessons/00_setup/hello_de.py                  # run any lesson script
```

---

## 📈 Progress

### Phase 0: Setup ✅
- [x] Python, VS Code, uv, Git and GitHub
- [x] First DuckDB script: SQL from Python, GROUP BY / HAVING

### Phase 1: Python foundations
- [x] Strings and operators
- [x] Lists and tuples
- [x] Dictionaries and sets
- [ ] Conditionals
- [ ] Loops
- [ ] Functions
- [ ] Errors and exceptions
- [ ] Files: CSV and JSON
- [ ] Checkpoint: clean and aggregate a CSV without pandas

### Phase 2: Python + databases
- [ ] sqlite3 and DuckDB from Python
- [ ] Parameterised queries
- [ ] PostgreSQL in Docker + psycopg
- [ ] SQLAlchemy basics
- [ ] Checkpoint: load related CSVs into Postgres and answer business questions

### Phase 3: Data wrangling with pandas
- [ ] DataFrames, filtering, groupby, merge
- [ ] Window-style operations, dates, missing values
- [ ] Polars and DuckDB on DataFrames
- [ ] Checkpoint: analyse a Dutch open dataset

### Phase 4: Writing code like an engineer
- [ ] Project structure, type hints, ruff
- [ ] Testing with pytest
- [ ] Logging and configuration
- [ ] Classes, dataclasses and pydantic
- [ ] Calling APIs: pagination, retries
- [ ] CI with GitHub Actions
- [ ] Checkpoint: tested API client for the NS API

### Phase 5: Building pipelines
- [ ] ETL vs ELT, incremental and idempotent loads
- [ ] dbt
- [ ] Airflow
- [ ] Docker and docker compose
- [ ] Monitoring and data quality
- [ ] CD and OTAP environments

### Phase 6: Cloud, streaming and capstone
- [ ] Azure fundamentals
- [ ] Databricks and PySpark
- [ ] Parquet, Delta Lake, partitioning
- [ ] Streaming with Kafka/Redpanda
- [ ] 🚆 Capstone: weekend trips pipeline

---

## 🔗 Related

- **SQL course:** runs alongside this one. Each topic is learned in SQL first, then in Python.

## 📚 Resources

- [Python for Data Analysis, 3rd ed.](https://wesmckinney.com/book/) (Wes McKinney)
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) (DataTalksClub)
- [Real Python](https://realpython.com)
- *Fundamentals of Data Engineering* (Joe Reis & Matt Housley)