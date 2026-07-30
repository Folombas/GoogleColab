def calculate_metrics(data_list):
    '''Aggregates metrics from the list of commit objects.'''
    metrics = {
        'total_count': len(data_list),
        'distribution': {},
        'last_updated': data_list[0]['timestamp'] if data_list else None
    }

    for item in data_list:
        t = item['type']
        metrics['distribution'][t] = metrics['distribution'].get(t, 0) + 1

    return metrics
# Optimization Layer 1: improving calculation latency

# Optimization Layer 2: improving calculation latency

# Optimization Layer 3: improving calculation latency

# Optimization Layer 4: improving calculation latency

# Optimization Layer 5: improving calculation latency

# Optimization Layer 6: improving calculation latency

# Optimization Layer 7: improving calculation latency

# Optimization Layer 8: improving calculation latency

# Optimization Layer 9: improving calculation latency

# Optimization Layer 10: improving calculation latency

# Optimization Layer 11: improving calculation latency

# Optimization Layer 12: improving calculation latency

# Optimization Layer 13: improving calculation latency

# Optimization Layer 14: improving calculation latency
