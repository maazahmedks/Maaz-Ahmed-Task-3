
from apiautotest.src.Utilities.requestUtilities import RequestUtility
import logging as logger

class PetHelpers(object):

      def __init__(self):
        self.request_utility= RequestUtility()

      def get_pet_by_status(self, pet_status):
        return self.request_utility.get(f"findByStatus?status={pet_status}")

      def get_pet_by_id(self, pet_id):
        return self.request_utility.get(f"{pet_id}")

      def call_create_payload(self, payload):
        test = self.request_utility.apost('', payload=payload, expected_status_code=201)
        return test

      def get_pet_by_tag(self, pet_tag):
        return self.request_utility.get(f"findByTags?tags={pet_tag}")

      def delete_pet(self, pet_id):
        return self.request_utility.delete(f"{pet_id}")
