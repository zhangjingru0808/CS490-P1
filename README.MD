This project is write by python.
After download the raw data(ENCFFXXXXXX.bed) and process by bedtool to get txt DNA sequence file(ENCFFXXXXXX.txt)
Run Positive.py and input the name of txt DNA sequence file to get the average and it will cut the file.(output file: ENCFFXXXXXX_Pos_output.txt) and this is the positive output file.
Now turning to negative, run Get interval.py and input the name of raw data file to get a interval file for negative data.(output:ENCFFXXXXXX_Neg.txt)
Then process this interval file by bedtool and will have a bed file name(ENCFFxxxxxx_Neg.bed)
Finally, run Neg_cut.py, insert the name of Neg bed file and the average you have from positive file output, it will process the negative file like positive(output:ENCFFxxxxxx_Neg_output.txt)