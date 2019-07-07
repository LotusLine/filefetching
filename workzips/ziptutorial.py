import zipfile
         
jungle_zip = zipfile.ZipFile('/Users/azabro/Desktop/jungle.zip', 'w')
jungle_zip.write('/Users/azabro/Desktop/jungle.pdf', compress_type=zipfile.ZIP_DEFLATED)
 
jungle_zip.close()




