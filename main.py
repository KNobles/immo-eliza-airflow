from collections import defaultdict
from threading import Thread

import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from utils.collect_property_data import Property
from utils.data_dictionary_prints_csv import PropertyDataWriter
from utils.url_scraper import Scraper

print("========================================================")
print("\tWELCOME TO THE COLLECTING DATA CHALLENGE")
print("========================================================\n")

Scraper.write_property_urls()

# columns = [
#     "id",
#     "locality",
#     "postal_code",
#     "region",
#     "province",
#     "type_of_property",
#     "subtype_of_property",
#     "type_of_sale",
#     "price",
#     "number_of_bedrooms",
#     "surface",
#     "kitchen_type",
#     "fully_equipped_kitchen",
#     "furnished",
#     "open_fire",
#     "terrace",
#     "terrace_surface",
#     "garden",
#     "garden_surface",
#     "land_surface",
#     "number_of_facades",
#     "swimming_pool",
#     "state_of_the_building"
# ]

# dic = defaultdict(list)
# thread_list = list()
# with ThreadPoolExecutor(max_workers=6) as exec:
#     with open("01_scraping/data/urls.csv", "r") as f:
#         for url in f.readlines():
#             exec.submit(PropertyDataWriter.append_to_dict, args=[url, dic])

# write = pd.DataFrame(data=dic, columns=columns)
# write.to_csv("big_data.csv", index=False)