def merge_files():
    input_file = "06.Project Input File.txt"
    merge_file = "06.Project Merge File.txt"
    output_file = "06.Project Output File.txt"

    # Counters
    input_count = 0
    merge_count = 0
    output_count = 0

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if "**Insert Merge File Here**" in line:
                # Do NOT count this line as input, replace with merge contents
                with open(merge_file, "r") as mfile:
                    for mline in mfile:
                        outfile.write(mline)
                        merge_count += 1
                        output_count += 1
            else:
                # Count normal input line
                input_count += 1
                outfile.write(line)
                output_count += 1

    # Final record counts
    print(f"Input records: {input_count}")
    print(f"Merge records: {merge_count}")
    print(f"Output records: {output_count}")


# Run the function
merge_files()
