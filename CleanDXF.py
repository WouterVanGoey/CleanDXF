# CleanDXF v1.0
# Deletes BEND and BEND_EXTENT elements.

import ezdxf, sys

if len(sys.argv) < 2: exit() # Exit when no file is specified.

filename = sys.argv[1]
doc = ezdxf.readfile(filename)

msp = doc.modelspace()

# Query all lines with layer "BEND_EXTENT", then delete them.
belines = msp.query('*[layer=="BEND_EXTENT"]')
for entity in belines: msp.delete_entity(entity)

# Query all lines with layer "BEND", then delete them, then save.
blines = msp.query('*[layer=="BEND"]')
for entity in blines: msp.delete_entity(entity)

doc.save()