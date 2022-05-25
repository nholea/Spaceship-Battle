import unittest
import json
from Models import Spaceship
from game import app

class GameTest(unittest.TestCase):
    def setUp(self):
        self.SPACESHIPS_URL = "http://127.0.0.1:5000/spaceships"
        self.spaceship_name = "/A"
        self.expected_spaceship_test = {'Name': 'A', 'Spaceship': {'health': 0, 'name': 'A'}, 'State': 'Destroyed'}
        self.spaceship_test = Spaceship("A", 0)
        self.spaceship_test2 = Spaceship("B", 6)
        


    def test0_check_spaceship_model(self):
        self.assertEqual(self.spaceship_test.serialize(),{"name": "A", "health": 0})
        self.assertEqual(self.spaceship_test.state(), "Destroyed")
        print("Test 0 completed")

    def test1_no_model(self):
        with self.assertRaises(ValueError):
            Spaceship("C", -1)
        print("Test 1 completed")
    
    def test2_create_spaceship(self):
        resp = app.test_client().post(self.SPACESHIPS_URL,
                           json = self.spaceship_test.serialize())
        self.assertEqual(resp.status_code, 200)
        print("Test 2 completed")


    def test3_get_spaceship(self):
        resp = app.test_client().get(self.SPACESHIPS_URL + self.spaceship_name)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(json.loads(resp.data), self.expected_spaceship_test)
        print("Test 3 completed")

    def test4_get_spaceships(self):
        resp = app.test_client().get(self.SPACESHIPS_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(json.loads(resp.data)), 2)
        print("Test 4 completed")

    def test5_spaceship_battle(self):
        self.assertTrue(self.spaceship_test.protection())
        self.spaceship_test2.battle(self.spaceship_test)
        self.assertFalse(self.spaceship_test.protection())
        self.spaceship_test2.battle(self.spaceship_test)
        self.assertEqual(self.spaceship_test.health,0)
        self.assertFalse(self.spaceship_test.protection())
        print("Test 5 completed")


if __name__=="__main__":
    unittest.main()