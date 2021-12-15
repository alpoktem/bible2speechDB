#! /bin/bash

#Bible speech scraper Step 5 - Extract verses
#Extract verse audio, text pairs for each book using alignments

FS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

TEXTGRIDDIR=$WORKDIR/textgrid
AUDIOCHUNKSDIR=$OUTDIR/audio
TEXTCHUNKSDIR=$OUTDIR/text

# Create output directories
if [ ! -d $AUDIOCHUNKSDIR ]; then
  mkdir -p $AUDIOCHUNKSDIR;
fi

if [ ! -d $TEXTCHUNKSDIR ]; then
  mkdir -p $TEXTCHUNKSDIR;
fi

for bid in `ls $TEXTGRIDDIR`
do
	for tg in `ls $TEXTGRIDDIR/$bid`
	do
		cid="${tg%.*}"
		echo $bid $cid
		python $FS/chunk_chapter.py $WORKDIR/audio/$bid/$cid.$AUDIOFORMAT $TEXTGRIDDIR/$bid/$tg $OUTDIR/scripts/original/$bid/$cid.txt $AUDIOCHUNKSDIR $TEXTCHUNKSDIR
	done
done