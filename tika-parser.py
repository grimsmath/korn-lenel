from tika import parser
import os
import shutil
import glob
import datetime

def run(directory):
    # Check to see if the processed folder exists
    x = datetime.datetime.now()
    proc_dir = directory + "/Processed-" + x.strftime("%G-%m-%d")
    os.makedirs(proc_dir, exist_ok=True)

    # Open the import file
    out_file = open(directory + "/import-data.csv", "w+")

    # Print a header
    print_header(out_file)

    # Retrieve all of the files in the current director
    files = glob.glob(directory + '/*.pdf')

    # Iterate the reports
    for f in files:
        # Parse the current report
        parse_report(f, out_file)

        # Move the current file into the processed folder
        shutil.move(f, proc_dir + "/" + os.path.basename(f))

    # close the file
    out_file.close()


def parse_report(in_file, out_file):
    raw = parser.from_file(in_file)
    text = raw['content']

    # Grab our counts
    data = {
        "date": os.path.splitext(os.path.basename(in_file))[0],
        "invalid": text.count("Invalid"),
        "medicine": text.count("Medicine"),
        "dental": text.count("Dental"),
        "nursing": text.count("Nursing"),
        "public": text.count("Public")
    }

    # Output our counts
    print_rows(data, out_file)


def print_header(out_file):
    out_file.write("Report Date,"
                   "School,"
                   "Count\n")


def print_rows(data, out_file):
    out_file.write(f"{data['date']}, "
                   "School of Medicine,"
                   f"{data['medicine']}\n")

    out_file.write(f"{data['date']}, "
                   "School of Dentistry,"
                   f"{data['dental']}\n")

    out_file.write(f"{data['date']}, "
                   "School of Nursing,"
                   f"{data['nursing']}\n")

    out_file.write(f"{data['date']}, "
                   "School of Public Health,"
                   f"{data['public']}\n")

    out_file.write(f"{data['date']}, "
                   "Invalid,"
                   f"{data['invalid']}\n")


if __name__ == '__main__':
    test_dir = "/Users/dking/OneDrive - University of Louisville/Kornhauser/2021/Badge Data/Reports"
    run(test_dir)

    # run(os.getcwd())
