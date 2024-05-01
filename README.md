# Jira Tempo Report Processor

This Python utility enriches Jira Tempo report data by adding a 'Project' attribute to each entry. It processes the data by reading entries from a CSV file and applying mappings from a JSON file to assign the appropriate project to each entry. The enriched data is then written back to a new CSV file with a timestamp in its name to ensure uniqueness.

## Features

- Reads data from a CSV file containing Jira Tempo report entries.
- Enriches each entry with a 'Project' attribute based on predefined mappings in a JSON file.
- Outputs the enriched data to a new CSV file, named with the current date and time.

## Prerequisites

Ensure Python 3.9 or higher is installed on your machine. Additionally, install the required Python packages:

```bash
pip install -r requirements.txt
