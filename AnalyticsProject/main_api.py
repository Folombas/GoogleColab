import extractor_service
import stats_service

def run_analytics_pipeline():
    '''Orchestrates data flow between services.'''
    raw_entries = extractor_service.fetch_raw_log()
    final_metrics = stats_service.calculate_metrics(raw_entries)

    print(f"[Analytics Report]")
    print(f"Total Commits: {final_metrics['total_count']}")
    print(f"Last Activity: {final_metrics['last_updated']}")
    print("--- Type Distribution ---")
    for k, v in final_metrics['distribution'].items():
        print(f" - {k.upper()}: {v}")

    return final_metrics

if __name__ == '__main__':
    run_analytics_pipeline()