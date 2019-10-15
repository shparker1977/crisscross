import crisscross.cell as cell

def test_create_cell():
    test_cell = cell.Cell(is_blank=True)
    assert test_cell.value == " "
    assert test_cell.display == " "
    test_cell = cell.Cell(is_blank=False, value='S')
    assert test_cell.value == 'S'
    assert test_cell.display == " "
    test_cell.set_display('r')
    assert test_cell.display == 'R'

def test_set_and_check_cell():
    test_cell = cell.Cell(is_blank=False, value='S')
    test_cell.set_display('T')
    assert test_cell.check_value() == False
    test_cell.set_display('S')
    assert test_cell.check_value() == True
    

def test_invalid_input():
    test_cell = cell.Cell(is_blank=False, value='R')
    test_cell.set_display(1)
    assert test_cell.display == " "

def test_cant_change_blanks():
    test_cell = cell.Cell(is_blank=True)
    test_cell.set_display('R')
    assert test_cell.display == " "