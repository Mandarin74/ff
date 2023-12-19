from sshcheckers import ssh_checkout, upload_files
import yaml
import pytest

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture
def install_pack():
    return upload_files(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'{data.get("folder_in")}{data.get("file")}.deb', f'{data.get("folder_user")}{data.get("file")}.deb')


@pytest.fixture
def app_1():
    return append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user")}{data.get("file")}.deb',
         "Настраивается пакет"))


@pytest.fixture
def app_2():
    return append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -s {data.get("file")}',
        "Status: install ok installed"))


@pytest.fixture
def delete_pack():
    return ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -r {data.get("file")}',
        "Удаляется")


