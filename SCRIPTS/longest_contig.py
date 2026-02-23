'''
Extract the longest contig from a SPAdes contigs FASTA file
and write it to a new FASTA file.
'''

import sys
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(
    description="Extract longest contig from SPAdes contigs"
)

parser.add_argument(
    "-i", "--input",
    required=True,
    help="SPAdes contigs FASTA file"
)

parser.add_argument(
    "-o", "--output",
    required=True,
    help="Output FASTA file"
)

args = parser.parse_args(sys.argv[1:])

contigs = list(SeqIO.parse(args.input, "fasta"))


longest = max(contigs, key=lambda r: len(r.seq))

SeqIO.write(longest, args.output, "fasta")