# HCMV RNA-seq Analysis Pipeline

## Overview

This repository contains a reproducible Snakemake-based Python pipeline for analyzing Human cytomegalovirus (HCMV; Human cytomegalovirus) transcriptomes from RNA-seq data.

## Overview of Analysis

We compared HCMV transcriptomes from;

| Donor   | Timepoint | SRA Accession |
|---------|-----------|---------------|
| Donor 1 | 2 dpi     | SRR5660030    |
| Donor 1 | 6 dpi     | SRR5660033    |
| Donor 3 | 2 dpi     | SRR5660044    |
| Donor 3 | 6 dpi     | SRR5660045    |


All the results are summarized in a single output file called **`Ofosu_PipelineReport.txt`**

## What the pipeline does

## For each sample, the pipeline performs the following steps:

---
-   Download SRA reads and converted to fastq (Documented only)
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
-   Generate a `PipelineReport.txt`
---

## Download SRA Data
```{html}
# Example for one sample
fasterq-dump SRR5660030 --split-files

```

Repeated for :

-  SRR5660030

-  SRR5660033

-  SRR5660044

-  SRR5660045

  These files were subsampled into `TESTS/` used in the pipeline


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

In your Terminal, run in any directory of your choice:

```{=html}
git clone https://github.com/bofosu01/rna_seq_analysis.git

```

Moving into the directory containing all the files in the github repository


```{=html}
cd rna_seq_analysis

```


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

```{=html}
cd SNAKEMAKE

```

```{=html}
total 8.0K
-rw-r--r-- 1 bofosu student 7.7K Feb 22 19:15 Snakefile
```

## How to run the pipeline

### Dry run Check that everything is connected correctly

```{=html}
snakemake --dry-run

```

### Run the pipeline

```{=html}
snakemake --cores 4
```

### Results

```{=pdf}

total 32K
drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 BLAST

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 GCF_000845245.1

-rw-r--r--  1 bofosu student 2.6K Feb 22 19:25 PipelineReport.txt

drwxr-xr-x 11 bofosu student 4.0K Feb 22 19:25 OUTPUTS

-rw-r--r--  1 bofosu student 2.2K Feb 22 19:15 README.md

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:25 SCRIPTS

drwxr-xr-x  3 bofosu student 4.0K Feb 22 19:25 SNAKEMAKE

drwxr-xr-x  2 bofosu student 4.0K Feb 22 19:15 TESTS

```















