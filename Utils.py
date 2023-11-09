"""
Utils: this python script has all auxiliary functions needed in other noteeboks.
AUTHOR: Joan Balaguer, Jaume Adrover
CREATION DATE: 2023-11-08
"""


def className2Number(class_name):
    """
    Converts class name to its respective id. It uses a switch sentence introduced in
    Python 3.10.
    """
    match class_name:
        case ('bedroom'):
            return 0
        case ('Coast'):
            return 1
        case ('Forest'):
            return 2
        case ('Highway'):
            return 3
        case ('Industrial'):
            return 4
        case ('Insidecity'):
            return 5
        case ('kitchen'):
            return 6
        case ('livingroom'):
            return 7
        case ('Mountain'):
            return 8
        case ('Office'):
            return 9
        case ('OpenCountry'):
            return 10
        case ('store'):
            return 11
        case ('Street'):
            return 12
        case ('Suburb'):
            return 13
        case ('TallBuilding'):
            return 14
        case _:
            return -1


def number2ClassName(num):
    """
    Converts number to its respective class name. It uses a switch case introduced in Python 3.10.
    """
    match num:
        case 0:
            return 'bedroom'
        case 1:
            return 'Coast'
        case 2:
            return 'Forest'
        case 3:
            return 'Highway'
        case 4:
            return 'Industrial'
        case 5:
            return 'Insidecity'
        case 6:
            return 'kitchen'
        case 7:
            return 'livingroom'
        case 8:
            return 'Mountain'
        case 9:
            return 'Office'
        case 10:
            return 'OpenCountry'
        case 11:
            return 'store'
        case 12:
            return 'Street'
        case 13:
            return 'Suburb'
        case 14:
            return 'TallBuilding'
        case _:
            return -1
