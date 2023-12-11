from task_2 import check_command
import pytest

folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'
folder_ex = '/home/user/folder_ex'

def test_step_1():
    assert check_command(f'cd {folder_in}; 7z a {folder_out}/archive_1', 'Everything is Ok')


def test_step_2():
    assert check_command(f'cd {folder_out}; 7z d archive_1', 'Everything is Ok')

def test_step_3():
    assert check_command(f'cd {folder_in} ls -l', 'Everything is Ok')

def test_step_4():
    assert check_command(f'cd {folder_out}/archive_1; 7z x {folder_ex}', 'Everything is Ok')

if __name__ == '__main__':
    pytest.main(['-vv'])