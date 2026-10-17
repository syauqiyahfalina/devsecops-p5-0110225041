"""CLI for SecureStore demo."""
from database import initialize_database
from store import Store
from payments import PaymentService

def main():
    initialize_database()
    store, payments = Store(), PaymentService()
    while True:
        print("\n=== SecureStore ===\n1. Produk\n2. Cari produk\n3. Buat pesanan\n4. Riwayat order\n5. Pembayaran demo\n0. Keluar")
        choice=input("Pilih: ").strip()
        try:
            if choice=="1":
                for p in store.list_products(): print(f"{p['id']}. {p['name']} - Rp{p['price']:,} (stok {p['stock']})")
            elif choice=="2":
                for p in store.search_products(input("Nama produk: ").strip()): print(p)
            elif choice=="3":
                oid=store.create_order(int(input("ID produk: ")),int(input("Jumlah: ")),input("Nama pelanggan: ").strip() or "Guest")
                print(f"Pesanan dibuat: {oid}")
            elif choice=="4":
                for order in store.order_history(input("Nama pelanggan: ").strip()): print(order)
            elif choice=="5":
                print(payments.process_payment(int(input("ID pesanan: ")),input("Metode (transfer/cash/demo): ").strip()))
            elif choice=="0": break
            else: print("Pilihan tidak dikenal.")
        except (ValueError, TypeError) as exc: print(f"Gagal: {exc}")

if __name__=="__main__": main()
