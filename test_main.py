from mainprogram import add, sub

def test_add():
    assert add(2 , 3) == 5
    assert add(-1 ,1) == 0
    assert add(0 , 0) == 0
    
def test_sub() :
    assert sub(5, 3) == 2
    assert sub (2, 5) == -3
    assert sub (0, 0) == 0
    

