import unittest
from models.dojo import Dojo

class TestAddPerson(unittest.TestCase):
    """add_person command testcases"""
    def setUp(self):
        self.dojo=Dojo()

    def test_person_can_only_be_staff_or_fellow(self):
        person1=self.dojo.add_person('mwenda','1213','Y')
        self.assertEqual('Person type can only be a fellow or a staff!',person1)

    def test_person_name_only_string(self):
        person2=self.dojo.add_person('mwenda',1213,'Y')
        person3=self.dojo.add_person(123,'office','Y')
        error='names and person type should be a strings!'
        self.assertEqual(error,person2)
        self.assertEqual(error,person3)

    def test_person_created_successfully(self):
        employee_count = len(self.dojo.all_employees)
        mwenda = self.dojo.add_person("mwenda", "staff")
        new_count = len(self.dojo.all_employees)
        self.assertEqual((new_count - employee_count), 1)
        
if __name__ == '__main__':
    unittest.main()