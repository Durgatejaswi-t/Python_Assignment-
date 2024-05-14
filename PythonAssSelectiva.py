import json
import requests
import gzip
import os
import pytest

def read_and_print_crew(json_url):
    response = requests.get(json_url)
    data = response.json()
    print("Crew:", data["crew"])

def print_first_names(json_url):
    response = requests.get(json_url)
    if response.status_code == 200:
        try:
            json_objects = response.text.strip().split('\n')
            for json_obj in json_objects:
                data = json.loads(json_obj)
                print("First Name:", data.get("firstName", "N/A"))
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON data: {e}")
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

def print_5th_element(list_a):
    print("5th Element:", list_a[4])

def print_last_three_elements(list_a):
    print("Last Three Elements:", list_a[-3:])

def print_length_of_list(list_a):
    print("Length of the List:", len(list_a))

def print_keys_of_dict(dict_a):
    print("Keys of the Dictionary:", dict_a.keys())

def print_values_of_dict(dict_a):
    print("Values of the Dictionary:", dict_a.values())

def print_value_of_b(dict_a):
    print("Value of key 'b':", dict_a['b'])

def download_gh(hour="10"):
    url = f"https://data.gharchive.org/2015-01-01-{hour}.json.gz"
    filename = f"gh_archive_{hour}.json.gz"
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return os.path.abspath(filename)
    else:
        print(f"Failed to download file for hour {hour}.")
        return None

def test_download_gh():
    downloaded_file = download_gh()
    assert downloaded_file is not None
    assert os.path.exists(downloaded_file)

read_and_print_crew("https://raw.githubusercontent.com/bhargav-velisetti/flink_examples/master/data/cruise_ship_schema.json")

print_first_names("https://raw.githubusercontent.com/bhargav-velisetti/apache_beam_examples_java/master/data/sample-data.json")

list_a = [0, 1, 2, 3, 4, 5, 6]
print_5th_element(list_a)

print_last_three_elements(list_a)

print_length_of_list(list_a)

dict_a = {'a': 1, 'b': 2}
print_keys_of_dict(dict_a)

print_values_of_dict(dict_a)

print_value_of_b(dict_a)

test_download_gh()
