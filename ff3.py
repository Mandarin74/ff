import pytest
import yaml
from task_2 import check_command
import datetime

with open('config.yaml', encoding='utf-8') as f:
data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return check_command(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return check_command(f'rm -rf {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def make_files():
    return check_command(f'cd {data.get("folder_in")}; touch file_1.txt file_2.txt file_3.txt', '')

@pytest.fixture()
def stat_info():
    with open('stat.txt', 'a') as file:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_count = get_file_count_from_config(f'{folder_in})
        file_size = get_file_size_from_config(f'{folder_in})
        with open('proc/loadavg', 'r') as loadavg_file:
            cpu_stats = loadavg_file.read()
        stat_in = f'{current_time}, {file_count}, {file_size}, {cpu_stats}n'
        file.write(stat_in)
