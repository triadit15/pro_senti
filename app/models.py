<<<<<<< HEAD
from datetime import datetime
from flask_login import UserMixin
from . import db

# ============================================================
# USER MODEL
# ============================================================

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    wallet_balance = db.Column(db.Float, default=0)
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id)


# ============================================================
# WALLET TRANSACTION LOG
# ============================================================

class WalletTransaction(db.Model):
    __tablename__ = "wallet_transactions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    type = db.Column(db.String(100))      # e.g. "Airtime", "Electricity", "Voucher Redeemed"
    amount = db.Column(db.Float)          # positive for incoming, negative for spending
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============================================================
# MERCHANT PAYMENT
# ============================================================

class MerchantPayment(db.Model):
    __tablename__ = "merchant_payments"

    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    code = db.Column(db.String(50), unique=True, nullable=False)

    status = db.Column(db.String(20), default="pending")  # pending/paid
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_at = db.Column(db.DateTime)


# ============================================================
# VOUCHERS
# ============================================================

class Voucher(db.Model):
    __tablename__ = "vouchers"

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    status = db.Column(db.String(20), default="active")  # active/redeemed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    redeemed_at = db.Column(db.DateTime)


# ============================================================
# STORE + MARKETPLACE MODELS
# ============================================================

class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    domain = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=True)
    store = db.relationship("Store", backref="products")

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class CartItem(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="cart_items")

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product = db.relationship("Product")

    qty = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class MarketplaceOrder(db.Model):
    __tablename__ = "marketplace_orders"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="marketplace_orders")

    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="processing")
    external_order_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=True)


# ============================================================
# UTILITY PURCHASE LOG (AIRTIME, ELECTRICITY, VOUCHERS, LOTTO)
# ============================================================

class UtilityPurchase(db.Model):
    __tablename__ = "utility_purchases"

    id = db.Column(db.Integer, primary_key=True)

    # FIXED: correct foreign key to "users.id"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="utility_purchases")

    category = db.Column(db.String(50))     # airtime, electricity, vouchers, lotto
    amount = db.Column(db.Float)
    details = db.Column(db.String(200))     # phone, meter, brand, ticket type
    status = db.Column(db.String(20), default="completed")

=======
from datetime import datetime
from flask_login import UserMixin
from . import db

# ============================================================
# USER MODEL
# ============================================================

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    wallet_balance = db.Column(db.Float, default=0)
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id)


# ============================================================
# WALLET TRANSACTION LOG
# ============================================================

class WalletTransaction(db.Model):
    __tablename__ = "wallet_transactions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    type = db.Column(db.String(100))      # e.g. "Airtime", "Electricity", "Voucher Redeemed"
    amount = db.Column(db.Float)          # positive for incoming, negative for spending
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============================================================
# MERCHANT PAYMENT
# ============================================================

class MerchantPayment(db.Model):
    __tablename__ = "merchant_payments"

    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    code = db.Column(db.String(50), unique=True, nullable=False)

    status = db.Column(db.String(20), default="pending")  # pending/paid
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_at = db.Column(db.DateTime)


# ============================================================
# VOUCHERS
# ============================================================

class Voucher(db.Model):
    __tablename__ = "vouchers"

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    status = db.Column(db.String(20), default="active")  # active/redeemed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    redeemed_at = db.Column(db.DateTime)


# ============================================================
# STORE + MARKETPLACE MODELS
# ============================================================

class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    domain = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=True)
    store = db.relationship("Store", backref="products")

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class CartItem(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="cart_items")

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product = db.relationship("Product")

    qty = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class MarketplaceOrder(db.Model):
    __tablename__ = "marketplace_orders"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="marketplace_orders")

    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="processing")
    external_order_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=True)


# ============================================================
# UTILITY PURCHASE LOG (AIRTIME, ELECTRICITY, VOUCHERS, LOTTO)
# ============================================================

class UtilityPurchase(db.Model):
    __tablename__ = "utility_purchases"

    id = db.Column(db.Integer, primary_key=True)

    # FIXED: correct foreign key to "users.id"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="utility_purchases")

    category = db.Column(db.String(50))     # airtime, electricity, vouchers, lotto
    amount = db.Column(db.Float)
    details = db.Column(db.String(200))     # phone, meter, brand, ticket type
    status = db.Column(db.String(20), default="completed")

>>>>>>> 7762d9128f8de91025cf4a55232aad8b63d6ce04
    created_at = db.Column(db.DateTime, default=datetime.utcnow)