from db.postgresql import get_db_cursor
import datetime
from typing import List, Dict

def get_session(session : str) -> Dict:

    if not session:
        return {'status' : 'Parameter session tidak ditemukan'}

    with get_db_cursor() as cursor:
        cursor.execute("SELECT data_session FROM tblsession WHERE session = %s",(session,))
        row = cursor.fetchone()

        if not row:
            return {'status' : 'Session tidak ditemukan'}

    return row['data_session']

def check_session(session : str) -> Dict:

    if not session:
        return {'status' : 'Parameter session tidak ditemukan'}

    with get_db_cursor() as cursor:
        cursor.execute("SELECT * tblsession WHERE session = %s",(session,))
        row = cursor.fetchone()

        if not row:
            return {'status' : 'Session tidak ditemukan'}

    expired = row['expired']

    if not expired:
        return {'status' : 'Session sudah kadaluwarsa'}

    now = datetime.datetime.now()

    if now > expired:
        with get_db_cursor(True) as cursor:
            try:
                cursor.execute("DELETE FROM tblsession WHERE session = %s", (session,))
            except:
                return {'status' : 'Session sudah kadaluwarsa'}
                
        return {'status' : 'Session sudah kadaluwarsa'}

    return {'status': 'Ok'}
