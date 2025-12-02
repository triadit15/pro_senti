# reset_users.py
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    confirm = input("⚠️ This will delete ALL users. Type 'YES' to continue: ")
    if confirm == "YES":
        num_deleted = db.session.query(User).delete()
        db.session.commit()
        print(f"✅ Deleted {num_deleted} users from the database.")
    else:
        print("❌ Operation cancelled.")