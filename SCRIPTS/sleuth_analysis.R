# Sleuth analysis of HCMV RNA-seq data
# Created by: Belinda Ofosu
# Date: 2026-02-21
# Purpose: Differential expression analysis of HCMV transcriptomes using Sleuth

library(sleuth)
library(dplyr)

# Get all kallisto sample directories
samples <- dir("../OUTPUTS/QUANT")
samples

# Create condition vector
#Donor 1 (2dpi): SRR5660030
#Donor 1 (6dpi): SRR5660033
#Donor 3 (2dpi): SRR5660044
#Donor 3 (6dpi): SRR5660045


condition <- c("2dpi", "6dpi", "2dpi", "6dpi")

# Create metadata table
s2c <- data.frame(
  sample = samples,
  condition = condition,
  stringsAsFactors = FALSE
)

# Add path column
s2c <- s2c %>%
  mutate(path = file.path("../OUTPUTS/QUANT", sample))

# Prepare sleuth object
so <- sleuth_prep(s2c, ~ condition)

# Fit full model
so <- sleuth_fit(so, ~ condition, 'full')

# Fit reduced model
so <- sleuth_fit(so, ~1, 'reduced')

# Likelihood ratio test
so <- sleuth_lrt(so, 'reduced', 'full')

# Extract results
results_table <- sleuth_results(so, 'reduced:full', 'lrt')

# Filter significant transcripts (FDR < 0.05)
sig <- results_table %>%
  filter(qval < 0.05) %>%
  select(target_id, test_stat, pval, qval)

# Write PipelineReport.txt
write.table(sig,
            file = "../OUTPUTS/TEMP/sleuth_report.txt",
            sep = "\t",
            quote = FALSE,
            row.names = FALSE,
            append = TRUE)