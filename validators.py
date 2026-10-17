"""Basic validation helpers."""
import re

def validate_product_name(name):
    if not isinstance(name,str) or not name.strip(): raise ValueError("Nama produk tidak boleh kosong.")
    if len(name)>80: raise ValueError("Nama produk maksimal 80 karakter.")
    if not re.fullmatch(r"[\w\s.,'()-]+",name,flags=re.UNICODE): raise ValueError("Karakter nama produk tidak didukung.")
    return name.strip()

def validate_customer_name(name):
    if not isinstance(name,str) or not name.strip(): raise ValueError("Nama pelanggan tidak boleh kosong.")
    if len(name)>80: raise ValueError("Nama pelanggan maksimal 80 karakter.")
    return name.strip()
