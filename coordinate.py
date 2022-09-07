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

    def move(self, location):
        if type(location) == list:
            self.x = location[0]
            self.y = location[1]
            self.z = location[2]

coordinates = {
    'deck_plate' : {
        'safe': [-240000, -200000, -150000, 0],
        'test' : [-240000, -337000, 0, 0],
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
    'home',
    'safe',
    'test',
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
