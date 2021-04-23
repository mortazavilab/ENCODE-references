# SIRVs
## Download SIRV set 4 reference files from Lexogen
```bash
wget https://www.lexogen.com/wp-content/uploads/2020/07/SIRV_Set4_Sequences_200709a.zip
unzip SIRV_Set4_Sequences_200709a.zip
rm SIRV_Set4_Sequences_200709a.zip
```

## Concatenate the SIRV sequences and the longSIRV sequences into one fasta.
* `SIRV_isoforms_multi-fasta_200709a.fasta` contains the sequences for each of the SIRV chromosomes
* `SIRV_longSIRVs_multi-fasta_200709a.fasta` contains the sequences for each of the longSIRV chromosomes
```bash
cat SIRV_Set4_Sequences_200709a/SIRV_isoforms_multi-fasta_200709a.fasta > sirv4.fasta
cat SIRV_Set4_Sequences_200709a/SIRV_longSIRVs_multi-fasta_200709a.fasta >> sirv4.fasta
```

 ## GTF
 We attained a GTF directly from Lexogen, as they did not host a GTF split up by SIRV and longSIRV chromosomes. For convenience, the GTF has been included in this repo.

Remove the ERCCs from the GTF so that we're left with the SIRVs and longSIRVs.
 ```bash
grep -v ERCC ERCC_SIRVs_longSIRVs_multi-fasta.gtf > sirv4.gtf
 ```

 It came to light that the SIRV GTF allows transcripts from different strands to belong to the same gene, which TALON does not support. Therefore, we need to manually reconfigure the GTF file so that genes belong to only one strand.
 ```bash
python separate_multistrand_genes.py \
  --f sirv4.gtf \
  --o sirv4_multistrand.gtf
 ```

For TALON to work, we need the GTF file to have gene and transcript entries. So we need to run the TALON utility on sirv4_multistrand.gtf to get this.
```bash
talon_reformat_gtf \
  -gtf sirv4_multistrand.gtf
mv sirv4_multistrand_reformatted.gtf sirv4.gtf
 ```
