#!/bin/bash

# CONFIG

REPORT="../Ofosu_PipelineReport.txt"
RAW_DIR="../TESTS"
MAP_DIR="../OUTPUTS/MAPPING"

SAMPLES=("SRR5660030" "SRR5660033" "SRR5660044" "SRR5660045")




# LOOP OVER SAMPLES

for SAMPLE in "${SAMPLES[@]}"; do

    R1="${RAW_DIR}/${SAMPLE}_1.fastq"
    R2="${RAW_DIR}/${SAMPLE}_2.fastq"
    BAM="${MAP_DIR}/${SAMPLE}.bam"

    # Count raw read pairs (FASTQ = 4 lines per read)
    RAW_READS=$(($(wc -l < "$R1") / 4))

    # Count mapped read pairs (exclude unmapped reads)
    MAPPED_READS=$(samtools view -c -F 4 "$BAM")

    echo "Sample ${SAMPLE} had ${RAW_READS} read pairs before and ${MAPPED_READS} read pairs after Bowtie2 filtering." >> "$REPORT"

done