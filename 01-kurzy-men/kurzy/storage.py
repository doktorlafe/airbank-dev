"""Historie kurzů v SQLite."""
import sqlite3
from pathlib import Path

from .models import Rate

DB = Path(__file__).resolve().parent.parent / "historie.db"


def save(rates: dict[str, Rate], db: Path = DB) -> None:
    with sqlite3.connect(db) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS rate(
            day TEXT, source TEXT, code TEXT, mid REAL, buy REAL, sell REAL,
            PRIMARY KEY(day, source, code))""")
        c.executemany("INSERT OR REPLACE INTO rate VALUES (?,?,?,?,?,?)",
                      [(str(r.day), r.source, r.code, r.mid, r.buy, r.sell)
                       for r in rates.values()])
