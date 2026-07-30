import subprocess
from datetime import datetime

def fetch_raw_log():
    '''Fetches raw git logs and returns a list of dictionaries.'''
    try:
        raw = subprocess.check_output(['git', 'log', '--pretty=format:%s|%ai'], encoding='utf-8').split('
')
        parsed_data = []
        for entry in raw:
            if '|' not in entry: continue
            msg, date = entry.split('|')
            parsed_data.append({
                'message': msg.strip(),
                'timestamp': date.strip(),
                'type': _infer_type(msg)
            })
        return parsed_data
    except Exception as e:
        return [{'message': f'error: {e}', 'type': 'error'}]

def _infer_type(msg):
    msg = msg.lower()
    for t in ['feat', 'fix', 'perf', 'refactor', 'docs', 'chore']:
        if t in msg: return t
    return 'other'