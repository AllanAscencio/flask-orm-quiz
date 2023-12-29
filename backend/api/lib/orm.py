
def build_from_record(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj


def find(cursor, Class, id):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE businessentityid = %s"
    cursor.execute(sql_str, (id,))
    record = cursor.fetchone()
    return build_from_record(Class, record)


def find_all(cursor, Class, limit = 10):
    sql_str = f"SELECT * FROM {Class.__table__} limit %s"
    cursor.execute(sql_str, (limit,))
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]

def find_all_by_lastname(cursor, lastname, Class):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE lastname = %s"
    # "SELECT * from person.person WHERE lastname = 'ok'"
    cursor.execute(sql_str, (lastname,))
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]

