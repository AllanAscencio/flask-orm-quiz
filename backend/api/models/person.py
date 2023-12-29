from api.lib.orm import build_from_record, find
from api.lib.db import save, test_cursor, cursor, test_conn

class Person:
    __table__ = 'person.person'
    columns = ['businessentityid', 'persontype', 'namestyle', 'title', 'firstname',
      'middlename', 'lastname', 'suffix', 'emailpromotion', 
      'additionalcontactinfo', 'demographics', 'rowguid', 'modifieddata']
    
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        self.__dict__ = kwargs

    
    @classmethod
    def find_or_create_by_first_last_name_and_id(Class, firstname= '', lastname='', businessentityid='', conn=''):
        person_found = find(test_cursor, Person, businessentityid)
        if person_found == None:
            create_person = Person(firstname = firstname, lastname= lastname, businessentityid= businessentityid)
            save(create_person, test_conn, test_cursor)
            return create_person
        else:
            return person_found
            
