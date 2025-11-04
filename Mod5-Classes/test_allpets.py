from allpets import Pet

def test_pet_get_name():
    ## Setup
    new_pet = Pet('Garfield', 'orange')

    result = new_pet.get_name()

    ## Check result

    assert result == 'Pet: Garfield'
