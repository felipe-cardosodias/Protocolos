#!/usr/bin/python3

import os
import zipfile

def ziper(zipname, savepath, dir): 
    fantasy_zip = zipfile.ZipFile(f'{savepath}/{zipname}.zip', 'w') #determina onde será salvo o zip
    for folder, subfolders, files in os.walk(f'{dir}'): #varre o diretório indicado
        for file in files:
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f'{dir}'), compress_type = zipfile.ZIP_DEFLATED) #zipa tudo que tá no diretório
    fantasy_zip.close()

    return f"{savepath}/{zipname}.zip"
