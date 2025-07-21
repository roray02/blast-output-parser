#!/usr/bin/python3
#!/usr/bin/env python3

import re

def parse_blast(blast_file):
    try:
        # read the BLAST file content
        with open(blast_file, 'r') as file:
            content = file.read()

        # parse the query ID and query length
        query_id_match = re.search(r'Query=\s*(\S+)', content) # regex looks for 'Query=' followed by any amount of whitespace, then captures any non-whitespace characters
        query_length_match = re.search(r"Length=(\d+)", content) # regex looks for 'Length=' followed by one or more digits, then captures those digits

        if not query_id_match or not query_length_match:
            print("Error: Query ID or length not found in BLAST file")
            return

        query_id = query_id_match.group(1) # extract the query ID from the match
        query_length = int(query_length_match.group(1)) # extracts the query length from the match and converts it to an integer

        # print the query details
        print(f"Query ID: {query_id}")
        print(f"Query Length: {query_length}\n")

        # Regex logic: looks for the > character, followed by any amount of whitespace, 
        # then captures any characters (including newlines) until it finds 'Length= followed 
        # by one or more digits, then captures those digits. Then it looks for 
        # 'Score =' followed by one or more digits, and captures those digits.
        alignment_pattern = r"^>\s*(.*?)\n.*?Length=(\d+).*?Score =\s*(\d+)"
        alignments = re.finditer(alignment_pattern, content, re.MULTILINE | re.DOTALL)
        # i used re.MULTILINE and re.DOTALL to ensure that the regex could handle newlines and any amount of whitespace

        for i, alignment in enumerate(alignments, start=1):
            if i > 10:  # Limit to the first 10 alignments
                break

            description = alignment.group(1)
            # regex looks for a pipe character, followed by any characters that are not a pipe, then another pipe
            accession_match = re.search(r"\|([^|]+)\|", description)
            if accession_match:
                accession = accession_match.group(0)
            else:
                accession = "Unknown"

            length = alignment.group(2)
            score = alignment.group(3)

            # print alignment details
            print(f"Alignment #{i}: Accession = {accession} (Length = {length}, Score = {score})")

    except FileNotFoundError:   # catch error if file is not found
        print(f"Error: File '{blast_file}' not found")
    except Exception as e:  # catch any other errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = '/home/rray16/example_blast.txt'
    parse_blast(file_path)
