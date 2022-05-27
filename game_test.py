import unittest
import json
from flask import request
from Models import Spaceship, Weapon, Generator
from exceptions import DestroyedSpaceship
from game import app


class GameTest(unittest.TestCase):
    def setUp(self):
        self.SPACESHIPS_URL = "http://127.0.0.1:5000/spaceships"
        self.target_spaceship = "/A"
        self.expected_spaceship_test = {
            "Name": "A",
            "Spaceship": {
                "generator": {
                    "total power": 15
                },
                "health": 0,
                "name": "A",
                "weapon": {
                    "power consumed": 3,
                    "power needed": 6
                }
            },
            "State": "Destroyed"
        }
        self.spaceship_test = Spaceship("A", 0, Weapon(6, 3), Generator(15))
        self.spaceship_test2 = Spaceship("B", 6, Weapon(5, 4), Generator(20))
        self.weapon_test = Weapon(10, 6)

    def test0_check_spaceship_model(self):
        self.assertEqual(self.spaceship_test.serialize(), {'name': 'A', 'health': 0, 'weapon': {
                         'power needed': 6, 'power consumed': 3}, 'generator': {'total power': 15}})
        self.assertEqual(self.spaceship_test.state(), "Destroyed")
        print("Test 0 completed")

    def test1_check_weapon_shoot_at_spaceship(self):
        self.weapon_test.shoot(self.spaceship_test2)
        self.assertEqual(self.spaceship_test2.health, 5)
        print("Test 1 completed")

    def test2_no_model(self):
        with self.assertRaises(ValueError):
            Spaceship("C", -1, Weapon(6, 3), Generator(15))
        print("Test 2 completed")


    def test5_get_spaceships(self):
        resp = app.test_client().get(self.SPACESHIPS_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(json.loads(resp.data)), 2)
        print("Test 5 completed")

    def test6_spaceship_battle(self):
        self.spaceship_test2.shoot_at(self.spaceship_test)
        self.assertEqual(self.spaceship_test.health, 0)
        print("Test 6 completed")

    def test7_no_spaceship_battle(self):
        with self.assertRaises(DestroyedSpaceship):
            self.spaceship_test.shoot_at(self.spaceship_test2)
        print("Test 7 completed")


if __name__ == "__main__":
    unittest.main()
