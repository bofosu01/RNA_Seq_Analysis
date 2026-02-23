# HCMV RNA-seq Analysis Pipeline

## Overview

This repository contains a snakemake-based pipeline for RNA-Seq analysis of Human Cytomegalovirus (HCMV) transcriptomes to quantify expression, identify differentially expressed genes across two timepoints (2dpi vs 6dpi), assemble viral reads, and determine strain similarity using BLASTn.

All the results are summarized in a single output file called **`Ofosu_PipelineReport.txt`**

## What the pipeline does

## For each sample, the pipeline performs the following steps:

---
-   Extracts coding sequences (CDS) sequences from the HCMV reference genome
-   Builds a kallisto transcriptome index
-   Quantifies transcript expression using kallisto
-   Runs sleuth differential expression analysis (R script)
-   Builds a Bowtie2 genome index
-   Maps reads to the HCMV genome
-   Counts reads before and after mapping
-   Assembles RNA reads using SPAdes
-   Extracts the longest contig from each assembly
-   Runs BLASTN of the longest contig against a Betaherpesvirinae nucleotide database 
---

## Dependencies

The following tools and softwares must be installed and available:

-   snakemake 7.32.4 (<https://snakemake.readthedocs.io/en/v7.32.0/getting_started/installation.html>)
-   Python 3.12.3 (<https://www.python.org/downloads/release/python-3123/>)
-   R 4.5.2 (<https://cran.r-project.org/bin/windows/base/>)
-   kallisto 0.51.1 (<https://pachterlab.github.io/kallisto/download>)
-   bowtie2 2.5.2 (<https://anaconda.org/bioconda/bowtie2>)
-   sleuth (<https://pachterlab.github.io/sleuth/download>)
-   spades v3.15.5 (<https://github.com/ablab/spades/releases>)
-   conda (<https://anaconda.org/anaconda/conda>)

## Downloading the repository

On your Terminal, run in any directory of your choice:

`git clone https://github.com/bofosu01/rna_seq_analysis.git`

Moving into the directory containing all the files in the github repository
`cd rna_seq_analysis`

```{=html}

total 24K
drwxr-xr-x 2 bofosu student 4.0K Feb 22 19:15 BLAST

drwxr-xr-x 2 bofosu student 4.0K Feb 22 19:15 GCF_000845245.1

-rw-r--r-- 1 bofosu student 2.2K Feb 22 19:15 README.md

drwxr-xr-x 2 bofosu student 4.0K Feb 22 19:15 SCRIPTS

drwxr-xr-x 3 bofosu student 4.0K Feb 22 19:16 SNAKEMAKE

drwxr-xr-x 2 bofosu student 4.0K Feb 22 19:15 TESTS

```

Move into the **SNAKEMAKE** directory. It contains the `Snakefile`

`cd SNAKEMAKE`

```{=html}
total 8.0K
-rw-r--r-- 1 bofosu student 7.7K Feb 22 19:15 Snakefile
```

## How to run the pipeline

### Dry run Check that everything is connected correctly

`snakemake --dry-run`

### Run the pipeline

`snakemake --cores 4`
### Results

```{=html}

total 32K
drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 BLAST

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 GCF_000845245.1

-rw-r--r--  1 bofosu student 2.6K Feb 22 19:25 Ofosu_PipelineReport.txt

drwxr-xr-x 11 bofosu student 4.0K Feb 22 19:25 OUTPUTS

-rw-r--r--  1 bofosu student 2.2K Feb 22 19:15 README.md

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:25 SCRIPTS

drwxr-xr-x  3 bofosu student 4.0K Feb 22 19:25 SNAKEMAKE

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 TESTS

```






