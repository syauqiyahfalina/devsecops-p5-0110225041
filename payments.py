
"""Local-only payment simulation; never use for real transactions."""
import logging
import uuid

from database import get_connection

logger = logging.getLogger(__name__)


class PaymentService:
    def process_payment(self, order_id, payment_method):
        """Process a simulated payment for classroom purposes."""
        if payment_method not in {"transfer", "cash", "demo"}:
            raise ValueError("Metode pembayaran tidak didukung.")

        with get_connection() as db:
            order = db.execute(
                "SELECT id, total, status FROM orders WHERE id = ?",
                (order_id,)
            ).fetchone()

            if order is None:
                raise ValueError("Pesanan tidak ditemukan.")

            if order["status"] != "PENDING":
                raise ValueError("Pesanan bukan PENDING.")

            # Gunakan ID unik, bukan hash MD5.
            reference = str(uuid.uuid4())

            # Jangan mencatat referensi pembayaran ke log.
            logger.info(
                "Demo payment processed for order %s",
                order_id
            )

            db.execute(
                """
                INSERT INTO payments
                    (order_id, method, amount, status, reference)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    order_id,
                    payment_method,
                    order["total"],
                    "PAID",
                    reference
                )
            )

            db.execute(
                "UPDATE orders SET status = ? WHERE id = ?",
                ("PAID", order_id)
            )

        return f"Pembayaran demo untuk pesanan {order_id} berhasil."
