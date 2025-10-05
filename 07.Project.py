def ParseDegreeString(ddmmss):
    """
    Inputs:
        ddmmss - string in the form of dd°mm'ss"
    Returns:
        degrees, minutes, seconds - all floats
    """
    degree_symbol = chr(176)  # The ° symbol
    deg_index = ddmmss.find(degree_symbol)
    min_index = ddmmss.find("'")
    sec_index = ddmmss.find('"')

    # Extract values safely
    degrees = float(ddmmss[:deg_index])
    minutes = float(ddmmss[deg_index + 1:min_index])
    seconds = float(ddmmss[min_index + 1:sec_index])

    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):
    """Convert degrees, minutes, and seconds to decimal degrees."""
    return degrees + (minutes / 60) + (seconds / 3600)


def main():
    input_file = "07.Project Angles Input.txt"
    output_file = "07.Project Angles Output.txt"

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            ddmmss = line.strip()
            if not ddmmss:
                continue

            degrees, minutes, seconds = ParseDegreeString(ddmmss)
            decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)
            outfile.write(f"{decimal_value}\n")

    print(f"✅ Conversion complete! Results written to {output_file}")


if __name__ == "__main__":
    main()
