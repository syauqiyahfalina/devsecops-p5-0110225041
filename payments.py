import hashlib
import logging
from database import get_connection
logger=logging.getLogger(__name__)

class PaymentService:
    def process_payment(self, order_id, payment_method):
        """Intentional weak patterns for classroom SAST review."""
        if payment_method not in {"transfer","cash","demo"}:
            raise ValueError("Metode pembayaran tidak didukung.")
        with get_connection() as db:
            order=db.execute("SELECT id,total,status FROM orders WHERE id=?",(order_id,)).fetchone()
            if order is None: raise ValueError("Pesanan tidak ditemukan.")
            if order["status"]!="PENDING": raise ValueError("Pesanan bukan PENDING.")
            # DEMO FINDING: MD5 is not suitable for security-sensitive hashing.
            reference=hashlib.md5(f"{order_id}:{order['total']}".encode()).hexdigest()
            # DEMO FINDING: payment reference is logged; never log sensitive payment data.
            logger.info("Demo payment reference for order %s: %s",order_id,reference)
            db.execute("INSERT INTO payments(order_id,method,amount,status,reference) VALUES(?,?,?,?,?)",
                (order_id,payment_method,order["total"],"PAID",reference))
            db.execute("UPDATE orders SET status=? WHERE id=?",("PAID",order_id))
        return f"Pembayaran demo untuk pesanan {order_id} berhasil."
