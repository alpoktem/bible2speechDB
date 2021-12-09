#! /bin/bash

#Bible speech scraper Step 2 - Prepare chapter scripts
#Creates chapter scripts from XML format USX file 
#Outputs three versions: original, TTS and ASR optimized

FS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Create output directory
if [ ! -d $OUTDIR ]; then
  mkdir -p $OUTDIR;
fi

# Parse script from USX 
for bid in `ls $WORKDIR/audio`
do
	echo $bid
	usx_path=`find $WORKDIR/xml | grep $bid`
	book_audio_path=$WORKDIR/audio/$bid

	python $FS/prepare_book_scripts.py $bid $usx_path $OUTDIR/scripts $NUMBERSCSV $CHAPTERUTT
done
