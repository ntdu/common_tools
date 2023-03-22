from fastapi import FastAPI, File, UploadFile
import csv
import codecs
import json

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
