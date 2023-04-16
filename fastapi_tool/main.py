from fastapi import FastAPI, File, UploadFile
import csv
import codecs
import json
import requests
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = {}
    with open("dataset.json", "w") as outfile:

        for rows in csvReader:             
            key = rows['object_name']  # Assuming a column named 'Id' to be the primary key
            print(rows)
            json.dump(rows, outfile)
            outfile.write("\n")
            data[key] = rows  
    
    file.file.close()
    return data

import codecs
import osm2geojson

@app.get("/osm2geojsonss")
def osm2geojsonss():
    with codecs.open('alabama-latest.osm', 'r', encoding='utf-8') as data:
        xml = data.read()

    print("-----------------")
    geojson = osm2geojson.xml2geojson(xml, filter_used_refs=False, log_level='INFO')
    print(geojson)
    return 'data'


from pydantic import BaseModel
from typing import Dict, Any, Optional, ForwardRef, List, Union
from enum import Enum
import uuid

class DownloadSchema(BaseModel):
    url: str
    

@app.post("/download")
def download_file_from_url(data: DownloadSchema):
    url = data.url

    r = requests.get(url, allow_redirects=True)
    open('oregon_district.json', 'wb').write(r.content)

    return data
