import sqlite3

file = "stork.db"

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS shops (discordid text, item text)")
        c.execute("CREATE TABLE IF NOT EXISTS shops_stock (item text, time timestamp)")
        c.execute("CREATE TABLE IF NOT EXISTS item_alias (item text, alias text)")
        c.execute("CREATE TABLE IF NOT EXISTS item_value (item text, value integer)")
        c.close()
        conn.close()
        print("Database stork.db formed.")
    except:
        print("Database stork.db not formed.")
