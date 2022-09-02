'''
DESCRIPTION:
This module contains Coordinate.

NOTES:

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

import sys

from upper_gantry_coordinate import UpperGantryCoordinate

class Coordinate():
    # Public variables.
    x = None
    y = None
    z = None

    # Private variables.

    def __init__(self, location):
        if type(location) == list:
            self.x = location[0]
            self.y = location[1]
            self.z = location[2]
        elif type(location) == str:
            _ = _getCoordinateByName(location)
            self.x = _[0]
            self.y = _[1]
            self.z = _[2]

    def move(self, location):
        if type(location) == list:
            self.x = location[0]
            self.y = location[1]
            self.z = location[2]
        elif type(location) == str:
            _ = _getCoordinateByName(location)
            self.x = _[0]
            self.y = _[1]
            self.z = _[2]

coordinates = {
    'deck_plate' : {
        'sample_loading' : {},
        'reagent_cartridge' : {},
        'tip_trays' : {
            0 : { # tip tray 0
                0 : [0,0,0,0], # tip tray 0 row 0 [x,y,z,drip_plate]
                1 : [0,0,0,0],
                2 : [0,0,0,0],
                3 : [0,0,0,0],
                4 : [0,0,0,0],
                5 : [0,0,0,0],
                6 : [0,0,0,0],
                7 : [0,0,0,0],
                8 : [0,0,0,0],
                9 : [0,0,0,0],
                10 : [0,0,0,0],
                11 : [0,0,0,0]
                },
            1 : {
                0 : [0,0,0,0],
                1 : [0,0,0,0],
                2 : [0,0,0,0],
                3 : [0,0,0,0],
                4 : [0,0,0,0],
                5 : [0,0,0,0],
                6 : [0,0,0,0],
                7 : [0,0,0,0],
                8 : [0,0,0,0],
                9 : [0,0,0,0],
                10 : [0,0,0,0],
                11 : [0,0,0,0]
                },
            2 : {
                0 : [0,0,0,0],
                1 : [0,0,0,0],
                2 : [0,0,0,0],
                3 : [0,0,0,0],
                4 : [0,0,0,0],
                5 : [0,0,0,0],
                6 : [0,0,0,0],
                7 : [0,0,0,0],
                8 : [0,0,0,0],
                9 : [0,0,0,0],
                10 : [0,0,0,0],
                11 : [0,0,0,0]
                },
            3 : {
                0 : [0,0,0,0],
                1 : [0,0,0,0],
                2 : [0,0,0,0],
                3 : [0,0,0,0],
                4 : [0,0,0,0],
                5 : [0,0,0,0],
                6 : [0,0,0,0],
                7 : [0,0,0,0],
                8 : [0,0,0,0],
                9 : [0,0,0,0],
                10 : [0,0,0,0],
                11 : [0,0,0,0]
                },
            },
        'quant_strip' : {},
        'assay_strips' : {},
        'staging_deck' : {},
        'rear_space_1' : {},
        'heater_shaker' : {},
        'mag_separator' : {},
        'tip_transfer_tray' : {},
        'chiller' : {},
        'pre_amp' : {},
        'rna_heater' : {},
        'tray_out_location' : {},
        'tray_in_location' : {}
        }
    }

coordinate_names = [
    'tip_trays_tray0_row0',
    'tip_trays_tray0_row1',
    'tip_trays_tray0_row2',
    'tip_trays_tray0_row3',
    'tip_trays_tray0_row4',
    'tip_trays_tray0_row5',
    'tip_trays_tray0_row6',
    'tip_trays_tray0_row7',
    'tip_trays_tray0_row8',
    'tip_trays_tray0_row9',
    'tip_trays_tray0_row10',
    'tip_trays_tray0_row11',
    'tip_trays_tray1_row0',
    'tip_trays_tray1_row1',
    'tip_trays_tray1_row2',
    'tip_trays_tray1_row3',
    'tip_trays_tray1_row4',
    'tip_trays_tray1_row5',
    'tip_trays_tray1_row6',
    'tip_trays_tray1_row7',
    'tip_trays_tray1_row8',
    'tip_trays_tray1_row9',
    'tip_trays_tray1_row10',
    'tip_trays_tray1_row11'
    'tip_trays_tray2_row0',
    'tip_trays_tray2_row1',
    'tip_trays_tray2_row2',
    'tip_trays_tray2_row3',
    'tip_trays_tray2_row4',
    'tip_trays_tray2_row5',
    'tip_trays_tray2_row6',
    'tip_trays_tray2_row7',
    'tip_trays_tray2_row8',
    'tip_trays_tray2_row9',
    'tip_trays_tray2_row10',
    'tip_trays_tray2_row11',
    'tip_trays_tray3_row0',
    'tip_trays_tray3_row1',
    'tip_trays_tray3_row2',
    'tip_trays_tray3_row3',
    'tip_trays_tray3_row4',
    'tip_trays_tray3_row5',
    'tip_trays_tray3_row6',
    'tip_trays_tray3_row7',
    'tip_trays_tray3_row8',
    'tip_trays_tray3_row9',
    'tip_trays_tray3_row10',
    'tip_trays_tray3_row11'
    ]

def get_coordinate_by_name(coordinate_name):
    # Check if the coordinate_name is valid.
    if coordinate_name not in coordinate_names:
        sys.exit("ERROR (coordinate, get_coordinate_by_name): '{0}' is not a valid coordinate name!".format(coordinate_name))
    # Initialize the upper gantry coordinate object.
    ugc = UpperGantryCoordinate()
    # Get the coordinate by name.
    if coordinate_name == 'tip_trays_tray0_row0':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][0]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row1':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][1]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row2':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][2]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row3':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][3]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row4':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][4]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row5':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][5]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row6':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][6]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row7':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][7]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row8':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][8]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row9':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][9]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row10':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][10]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row11':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][11]
        return ugc.update(x, y, z, drip_plate)

def _getCoordinateByName(coordinate_name):
    coordinate_array = [-1,-1,-1]
    if coordinate_name == '':
        return
    elif coordinate_name == 'tip_trays_tray0_row0':
        coordinate_array = coordinates['deck_plate']['tip_trays'][0][0]
    return coordinate_array