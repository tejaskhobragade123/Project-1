import sqlite3
from pathlib import Path
from datetime import datetime, timezone

class Memory:
    def __init__(self, db_path="data/embedded_agent.db"):
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS memories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kind TEXT NOT NULL,
            content TEXT NOT NULL,
            score REAL DEFAULT 0,
            created_at TEXT NOT NULL
        )""")
        self.conn.commit()

    def add(self, kind, content, score=0):
        self.conn.execute(
            "INSERT INTO memories(kind,content,score,created_at) VALUES(?,?,?,?)",
            (kind, content, score, datetime.now(timezone.utc).isoformat())
        )
        self.conn.commit()

    def recent(self, limit=10):
        return self.conn.execute(
            "SELECT kind,content,score FROM memories ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()

    def strategies(self, limit=5):
        return self.conn.execute(
            "SELECT content,score FROM memories WHERE kind='strategy' "
            "ORDER BY score DESC,id DESC LIMIT ?", (limit,)
        ).fetchall()
