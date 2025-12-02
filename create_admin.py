from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    phone = "0810000000"
    password = "admin123"

    # prevent duplicates
    existing = User.query.filter_by(phone=phone).first()
    if existing:
        print("Admin already exists")
    else:
        admin = User(
            phone=phone,
            password=generate_password_hash(password),
            wallet_balance=0,
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created successfully!")