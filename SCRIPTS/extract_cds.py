'''
The script extracts all CDS features from the genome
using the GFF annotation file.
It writes a FASTA file containing only CDS sequences
with the RefSeq protein_id as the header.
It also writes the total number of CDS to a count file.

'''

# Import necessary libraries
import sys
import argparse
from Bio import SeqIO

# Function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(
        description="Extract CDS sequences from genome"
    )

    # Add genome FASTA argument
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Genome FASTA file"
    )

    # Add GFF annotation argument
    parser.add_argument(
        "-a", "--gff",
        required=True,
        help="GFF annotation file"
    )

    # Add output FASTA argument
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output CDS FASTA file"
    )

    # Add count output argument
    parser.add_argument(
        "-c", "--count",
        required=True,
        help="CDS count file"
    )

    return parser.parse_args(args)

# Retrieve command line arguments
arguments = check_arg(sys.argv[1:])
genome_file = arguments.input
gff_file = arguments.gff
output_fasta = arguments.output
count_file = arguments.count

# Load genome sequences into a dictionary keyed by sequence ID
genome_dict = SeqIO.to_dict(SeqIO.parse(genome_file, "fasta"))

# Initialize CDS counter
cds_count = 0

# Open output FASTA for writing CDS sequences
with open(output_fasta, "w") as out_handle:

    # Open and parse GFF file line by line
    with open(gff_file) as gff:
        for line in gff:
            # Skip comments
            if line.startswith("#"):
                continue

            # Split GFF columns
            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue

            seqid, source, feature_type, start, end, score, strand, phase, attributes = parts

            # Only process CDS features
            if feature_type != "CDS":
                continue

            # Convert start/end to 0-based Python indexing
            start = int(start) - 1
            end = int(end)

            # Extract sequence from genome
            seq = genome_dict[seqid].seq[start:end]

            # Reverse complement if on minus strand
            if strand == "-":
                seq = seq.reverse_complement()

            # Parse protein_id from attributes
            attr_dict = dict(item.split("=") for item in attributes.split(";") if "=" in item)
            protein_id = attr_dict.get("protein_id", f"CDS_{cds_count+1}")

            # Write sequence to FASTA
            out_handle.write(f">{protein_id}\n{seq}\n")

            # Increment CDS counter
            cds_count += 1

# Write total CDS count to count file
with open(count_file, "w") as f:
    f.write(f"The HCMV genome (GCF_000845245.1) has {cds_count} CDS.\n")



