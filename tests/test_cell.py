import crisscross.cell as cell

def test_create_cell():
    test_cell = cell.Cell(isBlank=True)
    assert test_cell.value is None
    assert test_cell.display is None
    test_cell = cell.Cell(isBlank=False, value='S')
    assert test_cell.value == 'S'
    assert test_cell.display == None
    test_cell.set_display('r')
    assert test_cell.display == 'R'

def test_set_and_check_cell():
    test_cell = cell.Cell(isBlank=False, value='S')
    test_cell.set_display('T')
    assert test_cell.check_value() == False
    test_cell.set_display('S')
    assert test_cell.check_value() == True
    

def test_invalid_input():
    test_cell = cell.Cell(isBlank=False, value='R')
    test_cell.set_display(1)
    assert test_cell.display is None

def test_cant_change_blanks():
    test_cell = cell.Cell(isBlank=True)
    test_cell.set_display('R')
    assert test_cell.display == None