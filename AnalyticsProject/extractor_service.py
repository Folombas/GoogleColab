import subprocess

def fetch_raw_log():
    try:
        return subprocess.check_output(['git', 'log', '--pretty=format:%s|%ai'], encoding='utf-8').split('
')
    except Exception as e:
        return [f'error|{e}']