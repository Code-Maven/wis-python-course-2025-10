from shapes import area_of_rectangle

def test_area():
    result = area_of_rectangle(2, 3)
    assert result == 6

## Just to demo what happens when a test fails
#def test_area_again():
#    result = area_of_rectangle('2', 3)
#    assert result == 6

def test_area_2():
    assert area_of_rectangle(4, 5) == 20


