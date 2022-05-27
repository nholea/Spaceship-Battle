'''
    def test3_create_spaceship(self):
        resp = app.test_client().post(self.SPACESHIPS_URL,
                            json=self.spaceship_test.serialize())
        #self.assertEqual(resp.status_code, 200)
        print(resp.data)

    def test4_get_spaceship(self):
        resp = app.test_client().get(self.SPACESHIPS_URL + self.target_spaceship)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(json.loads(resp.data),
                             self.expected_spaceship_test)
        print("Test 4 completed")
'''



