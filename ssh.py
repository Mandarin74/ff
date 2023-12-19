from sshcheckers import ssh_checkout, upload_files
import yaml
import pytest

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def test_deploy(install_pack, app_1, app_2):
    assert upload_files(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'{data.get("folder_in")}{data.get("file")}.deb', f'{data.get("folder_user")}{data.get("file")}.deb')
    assert ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user")}{data.get("file")}.deb', "Настраивается пакет")
    assert ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -s {data.get("file")}', "Status: install ok installed")
    

def test_delete(delete_pack):
    assert ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -r {data.get("file")}', "Удаляется")

if __name__ == '__main__':
    pytest.main(['-vv'])