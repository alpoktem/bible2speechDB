#! /bin/bash

#Bible speech scraper Step 4 - Perform forced alignment
#Performs forced alignment book by book

MFADICT=$OUTDIR/$LANG.dict
TEXTGRIDDIR=$WORKDIR/textgrid

for bid in `ls $WORKDIR/audio`
do
	echo Aligning $bid
	BOUTDIR=$TEXTGRIDDIR/$bid
	# Create output directory
	if [ ! -d $BOUTDIR ]; then
	  mkdir -p $BOUTDIR;
	fi
	mfa align $WORKDIR/audio/$bid $MFADICT $LANG $BOUTDIR --clean
done