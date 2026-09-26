# ==========================================================
# Latihan Bab 3: Soal 4
# Skenario kesalahan bertahap dari khusus ke baseException
# ==========================================================

# 4a. OverflowError > ArithmeticError > Exception
print("--- Soal 4a: OverflowError ---")
import math
try:
    # Menghasilkan OverflowError dengan math.exp nilai yang sangat besar
    res = math.exp(1000)
except OverflowError as e:
    print(f"[OverflowError] Terjadi kesalahan: {e}")
except ArithmeticError as e:
    print(f"[ArithmeticError] Terjadi kesalahan aritmatika: {e}")
except Exception as e:
    print(f"[Exception] Terjadi kesalahan umum: {e}")

# 4b. FileExistsError > OSError > Exception
print("\n--- Soal 4b: FileExistsError ---")
import os
try:
    # Menghasilkan FileExistsError dengan membuat direktori yang sudah ada secara eksklusif
    os.makedirs(".", exist_ok=False)
except FileExistsError as e:
    print(f"[FileExistsError] File/Direktori sudah ada: {e}")
except OSError as e:
    print(f"[OSError] Terjadi kesalahan sistem/OS: {e}")
except Exception as e:
    print(f"[Exception] Terjadi kesalahan umum: {e}")

# 4c. ZipImportError > ImportError > Exception
print("\n--- Soal 4c: ZipImportError ---")
import zipimport
try:
    # Menghasilkan ZipImportError jika file zip tidak valid / korup
    importer = zipimport.zipimporter("non_existent_or_invalid.zip")
    importer.load_module("some_module")
except zipimport.ZipImportError as e:
    print(f"[ZipImportError] Gagal import dari zip: {e}")
except ImportError as e:
    print(f"[ImportError] Modul tidak dapat di-import: {e}")
except Exception as e:
    print(f"[Exception] Terjadi kesalahan umum: {e}")
