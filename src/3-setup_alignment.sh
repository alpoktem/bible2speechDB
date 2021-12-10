#! /bin/bash

#Bible speech scraper Step 3 - Setup forced alignment
#Sets up directories and creates phonetic dictionary 

TEXTCORPUS=$OUTDIR/all-scripts-merged.txt
MFADICT=$OUTDIR/$LANG.dict

# Make a copy of scripts besides their audio (for MFA)
# Merge them into a text corpus to make a dictionary
> $TEXTCORPUS
for bid in `ls $OUTDIR/scripts/normalized`
do
	for s in `ls $OUTDIR/scripts/normalized/$bid`
	do
		cp $OUTDIR/scripts/normalized/$bid/$s $WORKDIR/audio/$bid
		cat $OUTDIR/scripts/normalized/$bid/$s >> $TEXTCORPUS
	done
done

echo "Text corpus stats (L,W,C)"
wc $TEXTCORPUS

# Make dictionary for MFA
mfa g2p $LANG\_g2p $TEXTCORPUS $MFADICT --clean

