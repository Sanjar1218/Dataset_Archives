import xmltodict
import glob
import json

annotations_paths = glob.glob( 'image/train/*.xml' )

for xmlfile in annotations_paths:

    x = xmltodict.parse( open( xmlfile , 'rb' ) )
    bndbox = x[ 'annotation' ][ 'object' ][ 'bndbox' ]

    dct = {
        'label': x['annotation']['object']['name'],
        'x1': int(bndbox[ 'xmin' ]), 
        'y1': int(bndbox[ 'ymin' ]), 
        'x2': int(bndbox[ 'xmax' ]), 
        'y2': int(bndbox[ 'ymax' ])
    }

    with open(f"image/train/{x[ 'annotation' ]['filename'].split('.')[0]}.json", 'w') as f:
        json.dump(dct, f, indent=4, separators=(',', ':'))