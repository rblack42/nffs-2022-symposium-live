from pathlib import Path
import json
import sys

def extract_curve_points(airfoil, curve):
    dir = Path(__file__).parent
    print("Running in", dir)
    data_dir = dir / "arc3"
    print("airfoil data dir", data_dir)
    jname = curve + '.json'
    fname = data_dir / jname
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

    rname  = curve + '.py'
    rfile = data_dir / rname
    print("output:", rfile)
    try:
        with open(rfile, 'w') as fout:
            fout.write(f"x = {str(x)}\n")
            fout.write(f"y = {str(y)}\n")
    except:
        print("output failed")
    return x,y

if __name__ == '__main__':
    data = extract_curve_points('arc3','CL')
    data = extract_curve_points('arc3','CD')
    data = extract_curve_points('arc3','CM')

