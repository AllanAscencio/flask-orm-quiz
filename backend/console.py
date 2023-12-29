from api.models import *
import psycopg2
from settings import DB_NAME, TEST_DB_NAME
conn = psycopg2.connect(dbname = TEST_DB_NAME, user = 'postgres', password='afrocs221994')
cursor = conn.cursor()



#Test
# james = Person.find_or_create_by_first_last_name_and_id(5609454)
# print(james)