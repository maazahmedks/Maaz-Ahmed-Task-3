import json

import pytest
import logging as logger

from apiautotest.src.Helpers.PetHelpers import PetHelpers
import pdb

@pytest.mark.pet
def test_get_pet_by_status():
    logger.info("TEST: Get Pets by Status")
    status= "available"

    # Make the Get Pets by Status API call
    pet_help =PetHelpers()
    rs_api= pet_help.get_pet_by_status(status)
    api_pet_id=rs_api[0]['id']
    api_pet_name = rs_api[0]['name']
    api_pet_cat_id=rs_api[0]['category']['id']
    api_pet_cat_name=rs_api[0]['category']['name']

    # Verify the response
    assert api_pet_id==4
    assert api_pet_name == 'Dog 1'
    assert api_pet_cat_id == 1
    assert api_pet_cat_name == 'Dogs'

@pytest.mark.pet
def test_get_pet_by_id():
    logger.info("TEST: Get Pets by Id")
    Id=5

    # Make the Get Pets by Id API call
    pet_help =PetHelpers()
    rs_api= pet_help.get_pet_by_id(Id)
    api_pet_id=rs_api['id']
    api_pet_name = rs_api['name']
    api_pet_cat_id=rs_api['category']['id']
    api_pet_cat_name=rs_api['category']['name']

    # Verify the response
    assert api_pet_id==5
    assert api_pet_name == 'Dog 2'
    assert api_pet_cat_id == 1
    assert api_pet_cat_name == 'Dogs'

@pytest.mark.pet
def test_add_new_pet():
    logger.info("TEST: Add a new Pet")
    # Request Payload
    data= dict()
    data = {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # Make the Post call to add a new pet
    ph=PetHelpers()
    product_c = ph.call_create_payload(data)
    api_pet_id=product_c['id']
    api_pet_name = product_c['name']
    api_pet_cat_id=product_c['category']['id']
    api_pet_cat_name=product_c['category']['name']

    # Verify the response
    assert api_pet_id==10
    assert api_pet_name == 'doggie'
    assert api_pet_cat_id == 1
    assert api_pet_cat_name == 'Dogs'

@pytest.mark.pet
def test_get_pet_by_tag():
        logger.info("TEST: Get a Pet by tag")
        tag = 'string'

        # Make the Get Pets by tag API call
        pet_help = PetHelpers()
        rs_api = pet_help.get_pet_by_tag(tag)
        api_pet_id = rs_api[0]['id']
        api_pet_name = rs_api[0]['name']
        api_pet_cat_id = rs_api[0]['category']['id']
        api_pet_cat_name = rs_api[0]['category']['name']

        # Verify the response
        assert api_pet_id == 10
        assert api_pet_name == 'doggie'
        assert api_pet_cat_id == 1
        assert api_pet_cat_name == 'Dogs'

@pytest.mark.pet
def test_delete_pet():
        logger.info("TEST: Delete Pet")
        Id = 2

        # Make the Delete Pet API call
        pet_help = PetHelpers()
        rs_api = pet_help.delete_pet(Id)

        # Verify the response
        assert rs_api['code'] == 200
        assert rs_api['message'] == 'Pet deleted'