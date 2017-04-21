1. bam file is the sorted aligned file
2. bam.bai is the index file of the bam file
3. getCoverage.py uses pysam package, calculated the coverage of every position of trough regions
4. resulted file in coverage_trough_776.txt, which is a tab splited file
5. in coverage_trough_776.txt, the first column is the chromosome number, 
	second column is the start position and the third column is the stop position.

..........................................................
preprocessed steps:
	1. SRA toolkits: fastq-dump -I --split-files SRR3000776   （for data:  GSM1972521	HEPG2 mRNA untreated IP replicate C）
	2. get hg19.fa from UCSC, index it as reference fasta file
	3. index our downloaded reads
	4. use bwa mem to align reads to reference genome, generated aln_human_positive_trough.sam
	5. use samtools to convert sam to bam
	6. sort bam file
	7. index sorted bam file