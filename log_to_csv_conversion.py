import csv
import re

def log_to_csv(log_path, csv_path):
    
    # converts the .log file to .csv
    # extracting the IP, Country, DateTime, Method, Path, Protocol, Status, Bytes, Referrer, UserAgent, ResponseTime

    log_pattern = re.compile(
        r'(?P<ip>\S+) - (?P<country>\S+) - \[(?P<datetime>[^\]]+)\] '
        r'"(?P<method>\S+) (?P<path>\S+) (?P<protocol>[^"]+)" '
        r'(?P<status>\d+) (?P<bytes>\d+) "(?P<referrer>[^"]*)" "(?P<useragent>[^"]*)" (?P<responsetime>\d+)'
    )

    with open(log_path, 'r') as log_file, open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([
            'ip', 'country', 'datetime', 'method', 'path', 'protocol', 'status', 'bytes', 'referrer', 'useragent', 'responsetime'
        ])
        for line in log_file:
            match = log_pattern.match(line.strip())
            if match:
                writer.writerow([
                    match.group('ip'),
                    match.group('country'),
                    match.group('datetime'),
                    match.group('method'),
                    match.group('path'),
                    match.group('protocol'),
                    match.group('status'),
                    match.group('bytes'),
                    match.group('referrer'),
                    match.group('useragent'),
                    match.group('responsetime')
                ])


log_file = "sample-log.log"   
csv_file = "output.csv"          
log_to_csv(log_file, csv_file)