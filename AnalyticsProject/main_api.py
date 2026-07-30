import extractor_service
import stats_service

def get_analytics_report():
    raw_data = extractor_service.fetch_raw_log()
    report = stats_service.process_stats(raw_data)
    return report

if __name__ == '__main__':
    print('--- Running Analytics Microservices ---')
    print(get_analytics_report())