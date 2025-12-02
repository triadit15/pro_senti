# inspect_db.py
from app import create_app, db
import app.models as models

app = create_app()
with app.app_context():
    # print mapped model classes and their tablenames
    print("Mapped models and _tablename_ (if present):")
    for name, cls in models.__dict__.items():
        try:
            # filter SQLAlchemy model classes (have _table_ attribute)
            if hasattr(cls, "_tablename_"):
                print(f"  {name}: _tablename_ = {getattr(cls, '_tablename_')}")
        except Exception:
            pass

    # print metadata tables known to SQLAlchemy
    print("\nMetadata tables known to SQLAlchemy (db.metadata.tables.keys()):")
    print(list(db.metadata.tables.keys()))