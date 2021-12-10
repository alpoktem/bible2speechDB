#! /bin/bash

#Bible speech scraper Step 1 - Download raw data
#Downloads raw audio and text from ebible and openbible repositories
#The books to download are specified in TAGSFILE (format?)

FS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

####
#Process starts from here
####

# Create working directory
if [ ! -d $WORKDIR ]; then
  mkdir -p $WORKDIR;
fi

# Download text archive from eBible and unzip it (if needed)
curl -O $EBIBLE_TEXT_ARCHIVE
unzip $LANG\_readaloud.zip -d $WORKDIR/ebible
rm $LANG\_readaloud.zip

# Download XML scripts from open.bible
curl -o $WORKDIR/openbible_text.zip $OPENBIBLE_TEXT_ARCHIVE
unzip $WORKDIR/openbible_text.zip -d $WORKDIR/xml
rm $WORKDIR/openbible_text.zip

# Download audio archives
while read CID           
do       
	CHAPTERURL=$AUDIOURLPREFIX$CID\_$AUDIOFORMAT.zip    
    echo Downloading $CID in $AUDIOFORMAT
    curl -o $WORKDIR/$CID.zip $CHAPTERURL
    unzip $WORKDIR/$CID.zip -d $WORKDIR/audio
    rm $WORKDIR/$CID.zip
done < $TAGSFILE 


