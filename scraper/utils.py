import csv
import argparse

def save_to_csv(jobs, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'compmay', 'link'])
        writer.writeheader()
        writer.writerows(jobs)

def parse_args():
        parser = argparse.ArgumentParser(
            prog="job-scraper",
            description="Application to scrape job boards"
        )
        parser.add_argument(
            "-u",
            "--url",
            type=str,
            help="Target website",
        )
        
        args = parser.parse_args()
        return args.url