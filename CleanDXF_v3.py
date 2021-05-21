# CleanDXF v3.0

# RGB to ACI table here: https://gohtx.com/acadcolors.php

from collections import namedtuple
import ezdxf, sys

from ezdxf.layouts.layout import Modelspace

if len(sys.argv) < 2: exit() # Exit when there is no file


def main():

    for file in sys.argv[1:]:

        doc = ezdxf.readfile(file)
        msp = doc.modelspace()

        entities = Entities(msp)
        query = entities.query()

        Entities.delete(query.bend)
        Entities.delete(query.dims)

        doc.save()


class Entities:

    def __init__(self, msp) -> None: 
        self.msp = msp

    def query(self):
       
        Query = namedtuple("Entities", ["bend", "dims"]) 

        # Query all entities on a layer named BEND
        bend_lines = self.msp.query('*[layer=="BEND"]')

        # Add entities on a layer named BEND_EXTENT
        bend_lines.extend('*[layer=="BEND_EXTENT"]')

        # Query all pink entities (255,0,255)
        dimensions = self.msp.query('*[color==6]')

        return Query(
            bend_lines,
            dimensions,
        )


    def delete(self, entities):

        for entity in entities: self.msp.delete_entity(entity)

if __name__ == '__main__':
   main()