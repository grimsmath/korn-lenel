from tika import parser
import os
import shutil
import glob


def run(directory):
    # Check to see if the processed folder exists
    procdir = directory + "/processed/"
    os.makedirs(procdir, exist_ok=True)

    # Open the import file
    outfile = open(directory + "/import-data.csv", "w+")

    # Print a header
    printheader(outfile)

    # Retrieve all of the files in the current director
    files = glob.glob(directory + '/*.pdf')

    # Iterate the reports
    for f in files:
        # Parse the current report
        parsereport(f, outfile)

        # Move the current file into the processed folder
        shutil.move(f, procdir + "/" + os.path.basename(f))

    # close the file
    outfile.close()


def parsereport(infile, outfile):
    raw = parser.from_file(infile)
    text = raw['content']

    # Grab our counts
    data = {
        "date": os.path.splitext(os.path.basename(infile))[0],
        "valid": text.count("Access Granted"),
        "invalid": text.count("Invalid"),
        "medicine": text.count("Medicine"),
        "dental": text.count("Dental"),
        "nursing": text.count("Nursing"),
        "public": text.count("Public")
    }

    # Output our counts
    printrow(data, outfile)


def printheader(outfile):
    outfile.write("Report Date,"
                  "Valid Badge Count,"
                  "Invalid Badge Count,"
                  "School of Medicine Count,"
                  "School of Dentistry Count,"
                  "School of Nursing Count,"
                  "School of Public Health Count\n")


def printrow(data, outfile):
    outfile.write(f'{data["date"]}, '
                  f'{data["valid"]}, '
                  f'{data["invalid"]}, '
                  f'{data["medicine"]}, '
                  f'{data["dental"]}, '
                  f'{data["nursing"]}, '
                  f'{data["public"]}')

    outfile.write("\n")


if __name__ == '__main__':
    testdir = "/Users/dking/OneDrive - University of Louisville/Kornhauser/2021/Badge Data/Reports"
    run(testdir)

    # run(os.getcwd())
