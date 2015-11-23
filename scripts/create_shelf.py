#Schuyler Mortimer Honors Thesis
import shelve

shelf_file = shelve.open('/home/schuyler/Desktop/Honors_Thesis/data_sets/file_version')
shelf_file['version'] = 5
shelf_file.close()
