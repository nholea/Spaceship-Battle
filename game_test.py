import unittest
import json
from Models import Spaceship, Weapon
from game import app

class GameTest(unittest.TestCase):
    def setUp(self):
        self.SPACESHIPS_URL = "http://127.0.0.1:5000/spaceships"
        self.spaceship_name = "/A"
        self.expected_spaceship_test = {'Name': 'A', 'Spaceship': {'health': 0, 'name': 'A', 'weapon': ''}, 'State': 'Destroyed'}
        self.spaceship_test = Spaceship("A", 0)
        self.spaceship_test2 = Spaceship("B", 6)
        self.weapon_test = Weapon()
        


    def test0_check_spaceship_model(self):
        self.assertEqual(self.spaceship_test.serialize(),{"name": "A", "health": 0, 'weapon': ''})
        self.assertEqual(self.spaceship_test.state(), "Destroyed")
        print("Test 0 completed")

    def test1_check_weapon_model(self):
        self.assertTrue(self.spaceship_test2.protection())
        self.weapon_test.shoot(self.spaceship_test2)
        self.assertFalse(self.spaceship_test2.protection())
        self.weapon_test.shoot(self.spaceship_test2)
        self.assertEqual(self.spaceship_test2.health,5)
        print("Test 1 completed")

    def test2_no_model(self):
        with self.assertRaises(ValueError):
            Spaceship("C", -1)
        print("Test 2 completed")
    
    def test3_create_spaceship(self):
        resp = app.test_client().post(self.SPACESHIPS_URL,
                           json = self.spaceship_test.serialize())
        self.assertEqual(resp.status_code, 200)
        print("Test 3 completed")


    def test4_get_spaceship(self):
        resp = app.test_client().get(self.SPACESHIPS_URL + self.spaceship_name)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(json.loads(resp.data), self.expected_spaceship_test)
        print("Test 4 completed")

    def test5_get_spaceships(self):
        resp = app.test_client().get(self.SPACESHIPS_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(json.loads(resp.data)), 2)
        print("Test 5 completed")

    def test6_spaceship_battle(self):
        self.assertTrue(self.spaceship_test.protection())
        self.spaceship_test2.battle(self.spaceship_test)
        self.assertFalse(self.spaceship_test.protection())
        self.spaceship_test2.battle(self.spaceship_test)
        self.assertEqual(self.spaceship_test.health,0)
        self.assertFalse(self.spaceship_test.protection())
        print("Test 6 completed")

    def test7_no_spaceship_battle(self):
        self.assertTrue(self.spaceship_test2.protection())
        self.spaceship_test.battle(self.spaceship_test2)
        self.assertTrue(self.spaceship_test.protection())
        self.spaceship_test.battle(self.spaceship_test2)
        self.assertEqual(self.spaceship_test2.health,6)
        print("Test 7 completed")


if __name__=="__main__":
    unittest.main()