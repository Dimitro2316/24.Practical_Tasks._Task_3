import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")

    cursor.execute("UPDATE orders SET customer_name = ? WHERE id = ?",
                   ("Updated Customer", 1))

    cursor.execute("UPDATE order_items SET quantity = ? WHERE order_id = ? "
                   "AND product_name = ?", (10, 1, "Product 1"))

    conn.commit()

except Exception as e:
    conn.rollback()
    print(f"Ошибка: {e}")

finally:
    cursor.close()
    conn.close()





