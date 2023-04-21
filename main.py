# CRUD stands for Create, Read, Update, Delete.
# For testing purposes 4 methods, related to the "pet" endpoints:
# Create (POST /pet)
# Read (GET /pet/{petId})
# Update (PUT /pet)
# Delete (DELETE /pet/{petId})
# NOTE: During testing with Postman I could see, that the most of the requests
# were precessed with 500 instead of 400/404/405 as mentioned in Swagger.
# Despite that, the expected values are set according to the data from Swagger.

import unittest
import requests
import json


class TestPostPet(unittest.TestCase):
    BASE_URL = "https://petstore.swagger.io/v2"

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

# A positive test case that verifies a pet can be successfully created with valid data.
    def test_create_pet_success(self):
        pet_data = {
            "id": 123456,
            "name": "Test Pet",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://example.com/testpet.jpg"],
            "tags": [{"id": 1, "name": "test tag"}],
            "status": "available"
        }

        response = self.session.post(f"{self.BASE_URL}/pet", json=pet_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertDictEqual(pet_data, response_data)

# A negative test case that verifies an error occurs when attempting to create a pet with an existing pet ID.

# A negative test case that verifies an error occurs when attempting to create a pet with invalid or incomplete data.
    def test_create_pet_invalid_data(self):
        pet_data = {
            "id": "invalid_id",
            "name": "",
            "category": {"id": "invalid_id", "name": ""},
            "photoUrls": [""],
            "tags": [{"id": "invalid_id", "name": ""}],
            "status": "invalid_status"
        }

        response = self.session.post(f"{self.BASE_URL}/pet", json=pet_data)
        self.assertEqual(response.status_code, 400)

# A positive test case that verifies a pet can be successfully retrieved by its ID.
    def test_get_pet_success(self):
        pet_id = 123456

        response = self.session.get(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 200)
        pet_data = response.json()
        self.assertEqual(pet_data["id"], pet_id)

# A negative test case that verifies an error occurs when attempting to retrieve a pet with a non-existent pet ID.
    def test_get_pet_non_existent_id(self):
        pet_id = 654321

        response = self.session.get(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 404)

# A negative test case that verifies an error occurs when attempting to retrieve a pet with an invalid pet ID.
    def test_get_pet_invalid_id(self):
        pet_id = "invalid_id"

        response = self.session.get(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 400)

# A positive test case that verifies a pet's information can be successfully updated with valid data.
    def test_update_pet_success(self):
        pet_data = {
            "id": 123456,
            "name": "Updated Test Pet",
            "category": {"id": 2, "name": "Cats"},
            "photoUrls": ["https://example.com/updated_testpet.jpg"],
            "tags": [{"id": 2, "name": "updated test tag"}],
            "status": "pending"
        }

        response = self.session.put(f"{self.BASE_URL}/pet", json=pet_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertDictEqual(pet_data, response_data)

# A negative test case that verifies an error occurs when attempting to update a pet with a non-existent pet ID.
    def test_update_pet_non_existent_id(self):
        pet_data = {
            "id": 654321,
            "name": "Non-existent Test Pet",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://example.com/non_existent_testpet.jpg"],
            "tags": [{"id": 1, "name": "test tag"}],
            "status": "available"
        }

        response = self.session.put(f"{self.BASE_URL}/pet", json=pet_data)
        self.assertEqual(response.status_code, 404)

# A negative test case that verifies an error occurs when attempting to update a pet with invalid or incomplete data.
    def test_update_pet_invalid_data(self):
        pet_data = {
            "id": "invalid_id",
            "name": "",
            "category": {"id": "invalid_id", "name": ""},
            "photoUrls": [""],
            "tags": [{"id": "invalid_id", "name": ""}],
            "status": "invalid_status"
        }

        response = self.session.put(f"{self.BASE_URL}/pet", json=pet_data)
        self.assertEqual(response.status_code, 400)

# A positive test case that verifies a pet can be successfully deleted by its ID.
    def test_delete_pet_success(self):
        pet_id = 123456

        response = self.session.delete(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 200)

        # Check if the pet was actually deleted
        response = self.session.get(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 404)

# A negative test case that verifies an error occurs when attempting to delete a pet with a non-existent pet ID.
    def test_delete_pet_non_existent_id(self):
        pet_id = 654321

        response = self.session.delete(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 404)

# A negative test case that verifies an error occurs when attempting to delete a pet with an invalid pet ID format.
    def test_delete_pet_invalid_id(self):
        pet_id = "invalid_id"

        response = self.session.delete(f"{self.BASE_URL}/pet/{pet_id}")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()