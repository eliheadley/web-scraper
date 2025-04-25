from scraper.job_scraper import scrape_jobs
from scraper.filters import filter_jobs
from scraper.utils import save_to_csv, parse_args

def main():
        url = parse_args()
        jobs = scrape_jobs(url)
        filtered_jobs = filter_jobs(jobs, keyword='IT')
        save_to_csv(filtered_jobs, 'data/jobs.csv')


if __name__ == '__main__':
        main()
    