import json
from django.db import transaction
from dashBoard.models import MarketReport
from datetime import datetime

from django.conf import settings


def import_json_data(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

            with transaction.atomic():  # Wrap the data import in a transaction
                for entry in data:
                    # Parse date strings to datetime objects
                    added = datetime.strptime(entry.get('added', ''), "%Y-%m-%d")
                    published = datetime.strptime(entry.get('published', ''), "%Y-%m-%d")

                    market_report = MarketReport(
                        end_year=entry.get('end_year', ''),
                        intensity=entry.get('intensity', 0),
                        sector=entry.get('sector', ''),
                        topic=entry.get('topic', ''),
                        insight=entry.get('insight', ''),
                        url=entry.get('url', ''),
                        region=entry.get('region', ''),
                        start_year=entry.get('start_year', ''),
                        impact=entry.get('impact', ''),
                        added=added,
                        published=published,
                        country=entry.get('country', ''),
                        relevance=entry.get('relevance', 0),
                        pestle=entry.get('pestle', ''),
                        source=entry.get('source', ''),
                        title=entry.get('title', ''),
                        likelihood=entry.get('likelihood', 0),
                    )
                    market_report.save()
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        # Handle exceptions, log errors, etc.
        # The transaction will be rolled back automatically.
        return False


json_url = settings.STATIC_URL + 'json/json_data.json'
print(json_url)


def run():
    # Fetch all questions
    imported = import_json_data(json_url)
    if imported:
        print("JSON data imported successfully.")
    else:
        print("File not found or error importing data.")

# import os
#
#
# def run():
#     # Print the current working directory
#     print("Current working directory:", os.getcwd())
#
#     # Construct the full file path
#     file_path = "json_data.json"
#     full_file_path = os.path.abspath()
#     print("Full file path:", full_file_path)
#
#     # Fetch all questions
#     imported = import_json_data(full_file_path)
#     if imported:
#         print("JSON data imported successfully.")
#     else:
#         print("File not found or error importing data2.")
