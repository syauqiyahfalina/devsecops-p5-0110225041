
from database import get_connection
from validators import validate_product_name, validate_customer_name


class Store:
    def list_products(self):
        with get_connection() as db:
            rows = db.execute(
                "SELECT id, name, price, stock FROM products ORDER BY id"
            ).fetchall()

        return [dict(row) for row in rows]

    def search_products(self, name):
        """Search products safely using a parameterized query."""
        validate_product_name(name)

        with get_connection() as db:
            query = """
                SELECT id, name, price, stock
                FROM products
                WHERE name LIKE ?
            """
            rows = db.execute(query, (f"%{name}%",)).fetchall()

        return [dict(row) for row in rows]

    def create_order(self, product_id, quantity, customer_name="Guest"):
        if quantity <= 0:
            raise ValueError("Jumlah harus lebih dari nol.")

        validate_customer_name(customer_name)

        with get_connection() as db:
            product = db.execute(
                "SELECT id, name, price, stock FROM products WHERE id = ?",
                (product_id,)
            ).fetchone()

            if product is None:
                raise ValueError("Produk tidak ditemukan.")

            if quantity > product["stock"]:
                raise ValueError("Stok tidak mencukupi.")

            total = product["price"] * quantity

            cursor = db.execute(
                """
                INSERT INTO orders
                    (customer_name, product_id, quantity, total, status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    customer_name,
                    product_id,
                    quantity,
                    total,
                    "PENDING"
                )
            )

            db.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ?",
                (quantity, product_id)
            )

            return cursor.lastrowid

    def order_history(self, customer_name):
        """Retrieve order history safely using a parameterized query."""
        validate_customer_name(customer_name)

        with get_connection() as db:
            query = """
                SELECT id, customer_name, product_id,
                       quantity, total, status
                FROM orders
                WHERE customer_name = ?
                ORDER BY id DESC
            """
            rows = db.execute(query, (customer_name,)).fetchall()

        return [dict(row) for row in rows]
