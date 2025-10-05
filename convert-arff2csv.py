import sys
import pandas as pd
from scipy.io import arff

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert-arff2csv.py <input.arff> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data, meta = arff.loadarff(input_file)

    df = pd.DataFrame(data)

    df.to_csv(output_file, index=False)

    print(f"Converted {input_file} → {output_file}")

if __name__ == "__main__":
    main()
