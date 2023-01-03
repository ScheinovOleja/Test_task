from api.utils.db.main import Database


async def get_all_users_data():
    db = Database()
    with db.connection:
        all_users = db.cursor.execute("SELECT user_id, reg_time FROM users ORDER BY reg_time DESC")
        return all_users.fetchall()


async def get_user(tg_id) -> list:
    db = Database()
    with db.connection:
        user_data = db.cursor.execute(f"""
        SELECT doc_user_name, doc_user_city, doc_user_number, file_category, file_id FROM documents_data dd 
        INNER JOIN document_files df ON dd.id = df.doc_id
        WHERE dd.doc_user_id == {tg_id}
        """)
        return user_data.fetchall()
