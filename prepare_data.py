import os
import json
import matplotlib.pyplot as plt
import numpy
from PIL import Image, ImageDraw
from urllib.request import urlretrieve

outputJsonWriter = True
downloadImages = True

dataset_name = ""


listOut = ['']
json_path = "./labelling_" + dataset_name + ".json"
images_path = "./" + dataset_name + "_images"
json_name_out = dataset_name + "_json.json"

outputDiz = {}

if not os.path.exists(images_path):
    os.mkdir(images_path)

dd = json.load(open(json_path))
d = []
for index in range(len(dd)):
    if dd[index]['Label'] == 'Skip':
        continue
    d.append(dd[index])




for index in range(len(d)):
    print("Image", index)
    outputDiz[index] = {}
    outputDiz[index]['Name'] = images_path + '/image'+ str(index) + ".png"
    outputDiz[index]['Dataset'] = dataset_name
    outputDiz[index]['Labels'] = {}
    if downloadImages:
        urlretrieve(d[index]["Labeled Data"], images_path +"/image"+str(index)+ ".png")
    for key in (d[index]['Label'].keys()):
        num = len(d[index]['Label'][key])

        for subindex in range(len(d[index]['Label'][key])):

            aux = d[index]['Label'][key][subindex]

            obj = aux['title']
            print(obj)
            mask_path = images_path +"/image"+str(index)+ '_' + obj +".png"
            if downloadImages:
                urlretrieve(aux['instanceURI'], mask_path)
            outputDiz[index]['Labels'][obj] = mask_path


if outputJsonWriter:
    with open(json_name_out, 'w') as f:
        json.dump(outputDiz, f)
