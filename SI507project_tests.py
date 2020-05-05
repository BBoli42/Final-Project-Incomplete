import sqlite3
import unittest
import SI507project_tools
import nat_park_soup

##8 TESTS?
class FinalProject(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("sqlite:///./sample_national_parks.db")
		self.cur = self.conn.cursor()

    def test_state(self):
		self.cur.execute("select state from where location = 'AL'")
		data = self.cur.fetchone()
		self.assertEqual(data,('AL',"list of states"), "Testing data that results are from AL")

	def test_park(self):
		self.cur.execute("select park from where locationn = 'AL'")
		data = self.cur.fetchone()
		self.assertEqual(data,('AL',"list of descriptions"), "Testing data that results are from parks in AL")

	def test_input(self):
		data = self.cur.fetchone(user_input)
		self.assertEqual("testing that user enters a string")









	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
