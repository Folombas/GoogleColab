def process_stats(log_entries):
    stats = {'total': 0, 'feat': 0, 'fix': 0, 'other': 0}
    for entry in log_entries:
        if '|' not in entry: continue
        msg = entry.split('|')[0].lower()
        stats['total'] += 1
        if 'feat' in msg: stats['feat'] += 1
        elif 'fix' in msg: stats['fix'] += 1
        else: stats['other'] += 1
    return stats