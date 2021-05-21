# CleanDXF v1.0
# Deletes BEND and BEND_EXTENT elements.

import ezdxf, sys

if len(sys.argv) < 2: exit() # Exit when no file is specified.

fname = sys.argv[1]
doc = ezdxf.readfile(fname)

msp = doc.modelspace()

# Query all lines with layer "BEND", then delete them, then save.
dimlines = msp.query('*[color==6]')
for entity in dimlines: msp.delete_entity(entity)

doc.save()