import json
import sys
import rasterio
from rasterio.mask import mask
from json import loads
import sys
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
# from rasterio.tools.mask import mask

# tiffFileName=sys.argv[1]
# folder_containing_tifffiles = "data/copyDummyData"
#states - AP, Bihar, Gujarat, Karnataka, Maharashtra, MP, Orissa
#categories - park, forest, industrial, nature_reserve, residential

#First put the json file corresponding to category in cutjson folder
category = 'quarry'

#states = {'AP', 'Bihar', 'Gujarat', 'Karnataka', 'Maharashtra', 'MP', 'Orissa','Delhi'}
states = {'Maharashtra',}
for state in tqdm(states, desc='No of States: '):

    #state = 'Orissa'
    folder_containing_tifffiles = 'download/'+state
    jsonFolderName = 'cutjson'
    output_directory = category+'/'+category+'_'+state
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    allTiffFiles = [f for f in listdir(folder_containing_tifffiles) if isfile(join(folder_containing_tifffiles, f))]

    jsonFileList=[f for f in listdir(jsonFolderName) if isfile(join(jsonFolderName,f))]


    for tiffFileName in tqdm(allTiffFiles, desc='Total TIFF Files: '):
        for jsonFileName in jsonFileList:
            jsonFileName = jsonFolderName+'/'+jsonFileName
            stateData = json.loads(open(jsonFileName).read())
            print('tiffFileName',tiffFileName)
            print('jsonFileName',jsonFileName)
            for currFeature in tqdm(stateData["features"], desc ='Current TIFF File: '):
                try:
                    #vCode2011=currVillageFeature["properties"]["village_code_2011"]
                    #vCode2001=currVillageFeature["properties"]["village_code_2001"]
                    osmId=currFeature["properties"]["osm_id"]
                    geoms=currFeature["geometry"]
                    #print(geoms)
                    listGeom=[]
                    listGeom.append(geoms)
                    geoms=listGeom
                    with rasterio.open(folder_containing_tifffiles+'/'+tiffFileName) as src:
                        out_image, out_transform = mask(src, geoms, crop=True)

                    out_meta = src.meta.copy()
                    # save the resulting raster  
                    out_meta.update({"driver": "GTiff",
                        "height": out_image.shape[1],
                        "width": out_image.shape[2],
                    "transform": out_transform})
                    saveFileName=output_directory+'/'+tiffFileName[:-4]+"@"+osmId+".tif"
                    #print(vCode2011)
                    with rasterio.open(saveFileName, "w", **out_meta) as dest:
                        dest.write(out_image)
                except:
                    continue
