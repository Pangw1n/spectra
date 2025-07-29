import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import sys

parse = argparse.ArgumentParser()
parse.add_argument('--input', type=str, action="store", dest='input', help="Input directory", required=True)
parse.add_argument('--output', type=str, action="store", dest='output', help="Output directory", required=True)
parse.add_argument('--combine_graphs', action="store_true", dest='combine_graphs', help="Combine data to one graph", default=False)
args = parse.parse_args()
input = args.input
output = args.output
combine_graphs = args.combine_graphs

if not os.path.exists(input):
    print(f"Error: Input path does not exist - {input}")
    sys.exit()
if not os.path.exists(output):
    print(f"Output path does not exist - {output}\nCreating new folder")
    os.mkdir(output)
    

#combine_graphs = False

#INPUT = "data"
#OUTPUT = "output"

summary = pd.DataFrame({"Name":[], "Max transmittance":[], "Wavelength of max transmittance":[], "Min transmittance":[], "Wavelength of min transmittance":[], "Mean":[], "Median":[]})
summary["Name"] = summary["Name"].astype(str)
summary["Wavelength of max transmittance"] = summary["Wavelength of max transmittance"].astype(int)
summary["Wavelength of min transmittance"] = summary["Wavelength of min transmittance"].astype(int)

count = 0

if combine_graphs:
    ax = plt.subplot()

try:
    for file in os.listdir(os.fsencode(input)):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(input, filename), sep=r'\s*,\s*', engine="python")
            if combine_graphs:
                ax = df.plot(ax=ax, x="nm", y="%T", label=filename[0:len(filename) - 4])
            else: 
                df.plot(x="nm", y="%T", label=filename[0:len(filename) - 4])
                plt.ylabel("Transmittance[%]")
                plt.xlabel("Wavelength[nm]")
                plt.ylim(0,110)
                plt.title("Transmittance spectrum for " + filename[0:len(filename) - 4])
                plt.savefig(os.path.join(output, filename[0:len(filename) - 4] + ".png"))

            max = df.sort_values(by="%T", ascending=False).head(1)
            min = df.sort_values(by="%T", ascending=True).head(1)
            mean = df["%T"].mean()
            median = df["%T"].median()
            summary.loc[count, "Name"] = filename[0:len(filename) - 4]
            summary.loc[count, "Max transmittance"] = max["%T"].iloc[0]
            summary.loc[count, "Wavelength of max transmittance"] = max["nm"].iloc[0]
            summary.loc[count, "Min transmittance"] = min["%T"].iloc[0]
            summary.loc[count, "Wavelength of min transmittance"] = min["nm"].iloc[0]
            summary.loc[count, "Mean"] = mean
            summary.loc[count, "Median"] = median

            count += 1
            continue
        else:
            continue

    if combine_graphs:
        plt.ylabel("Transmittance[%]")
        plt.xlabel("Wavelength[nm]")
        plt.ylim(0,110)
        plt.title("Transmittance spectrum")
        plt.legend()
        plt.savefig(os.path.join(output, "graph.png"))

except FileNotFoundError as e:
    print(f"Error: File not found - {filename}")
    sys.exit()
except pd.errors.EmptyDataError as e:
    print(f"Error: Empty data in file - {filename}")
except KeyError as e:
    print(f"Error: Key not found - {repr(e)}")
    sys.exit()
except Exception as e:
    print(repr(e))
    sys.exit()

summary.to_csv(os.path.join(output, "summary.csv"))
print(f"Saved to {output}")


'''
df = pd.read_csv("data2.csv")

print("\nMaximum:")
print(df.sort_values(by="%T", ascending=False).head(1))

print("\nMinimum:")
print(df.sort_values(by="%T", ascending=True).head(1))

print("\nMean:")
print(df["%T"].mean())

print("\nMedian:")
print(df["%T"].median())

df.plot(x="lambda", y="%T")

plt.ylim(0,100)
plt.ylabel("Transmittance[%]")
plt.xlabel("Wavelength[nm]")
plt.show()
plt.savefig("")
'''


'''
print("\nMaximum:")
print(df[df["%T"] == df["%T"].max()])
print("\nMinimum:")
print(df[df["%T"] == df["%T"].min()])
'''