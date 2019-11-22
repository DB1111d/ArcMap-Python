import arcpy

rows = arcpy.UpdateCursor("location_of_your_sde\name.sde\layer_name", "field_label_you_want_to_identify_the_feature_with = field_value")

for row in rows:
    row.setValue("field_name_to_update", value_to_update)
    rows.updateRow(row)

#Use double quotes for value_to_update if fild_name_to_update is a string
#If you want to see all fields for a layer to the same value, just remove the SQL Statement.
