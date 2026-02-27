import sys

def hi(list_of_names):
    print(f"Hi my first cohort students are: {list_of_names}")

if __name__ == "__main__":
    names = sys.argv[1:]   # everything after filename
    hi(names)
    print("Version 3")