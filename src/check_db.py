import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
e = os.environ
engine = create_engine(f"postgresql+psycopg://{e['POSTGRES_USER']}:{e['POSTGRES_PASSWORD']}@localhost:5432/{e['POSTGRES_DB']}")
with engine.connect() as c:
   print(c.execute(text("select version()")).scalar())