'''
Extract the longest contig from a SPAdes contigs FASTA file
and write it to a new FASTA file.
'''

import sys
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(
    description="Extract longest contig from SPAdes contigs"
) # Add input FASTA argument

parser.add_argument(
    "-i", "--input",
    required=True,
    help="SPAdes contigs FASTA file"
) # Add output FASTA argument

parser.add_argument(
    "-o", "--output",
    required=True,
    help="Output FASTA file"
) # Retrieve command line arguments

args = parser.parse_args(sys.argv[1:]) # Load contigs from input FASTA file into a list

contigs = list(SeqIO.parse(args.input, "fasta")) # Find the longest contig based on sequence length


longest = max(contigs, key=lambda r: len(r.seq)) # Write the longest contig to the output FASTA file

SeqIO.write(longest, args.output, "fasta") # Print the length of the longest contig 
