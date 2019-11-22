import arcpy
from arcpy import env
env.overwriteOutput = True
arcpy.env.workspace = r"location_of_your_sde\name.sde\layer_name"

#Syntax: AddField_management (in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
#https://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm

arcpy.AddField_management("layer_name", "new_field_name", "TEXT", "","","",NULLABLE,NON_REQUIRED)
arcpy.AddField_management("layer_name", "new_field_name", "FLOAT", 0,0,"",NULLABLE,NON_REQUIRED)
arcpy.AddField_management("layer_name", "new_field_name", "DOUBLE", 0,0,"",NULLABLE,NON_REQUIRED)
arcpy.AddField_management("layer_name", "new_field_name", "SHORT", 0,0,"",NULLABLE,NON_REQUIRED)
arcpy.AddField_management("layer_name", "new_field_name", "LONG", 0,0,"",NULLABLE,NON_REQUIRED)