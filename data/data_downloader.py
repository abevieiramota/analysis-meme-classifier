import os
import urllib.request
import requests
import json
import codecs
import csv

url_retrieve_instances_info = "http://version1.api.memegenerator.net/Instances_Select_ByPopular?languageCode=en&pageIndex=%d&pageSize=24&urlName=%s"

base_files = [file for file in os.listdir() if file.endswith('.jpg')]
base_files_names = [base_file.split('.')[0] for base_file in base_files]

with codecs.open("dataset.csv", 'w', 'utf-8') as dataset:

	dataset_csv = csv.writer(dataset, delimiter=';')
	dataset_csv.writerow(['meme', 'text0', 'text1'])

	for base_file_name in base_files_names:

		print("em: " + base_file_name)

		for page_ix in range(5):

			url_instances = url_retrieve_instances_info % (page_ix, base_file_name)
			instances = json.loads(requests.get(url_instances).text)['result']

			for instance in instances:

				dataset_csv.writerow([instance['urlName'], instance['text0'], instance['text1']])