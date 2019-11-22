import arcpy

#This will clear a field for all features in a specific data table.

rows = arcpy.UpdateCursor("location_of_your_sde\name.sde\layer_name")

for row in rows:
    row.setValue("field_name", None)
    rows.updateRow(row)
