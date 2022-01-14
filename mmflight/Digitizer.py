import json
import sys

def extract_curve_points(fname):
    x = []
    y = []
    try: # see if we can open this file
        with open(fname,'r') as fin:
            try: # try to load it as a json file
                data = json.load(fin)
                p = data['datasetColl'][0]['data']
                for i in p:
                    x.append(i['value'][0])
                    y.append(i['value'][1])
            except:
                print("File is not valid JSON:", fname)
                sys.exit(1)
    except:
        print("File cannot be opened:", fname)
        sys.exit(1)
    return x,y

if __name__ == '__main__':
    from pathlib import Path
    root = Path(__file__).parent.parent.resolve()
    print(root)
    test_data = 'CM.json'
    data = extract_curve_points(test_data)
    print("Cm_x =",data[0])
    print("Cm_y =",data[1])

