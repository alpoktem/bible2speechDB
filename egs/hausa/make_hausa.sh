#! /bin/bash

#Bible speech scraping for Hausa

#Install MFA
#TODO...

#Download Hausa MFA models 
# mfa model download acoustic $LANG
# mfa model download g2p $LANG\_g2p

export LANG=hausa
export WORKDIR=raw-data
export OUTDIR=corpus
export AUDIOFORMAT=mp3 #mp3 or wav

#TODO: Describe this file
export TAGSFILE=egs/hausa/openbible_chapter_tags.txt

#A file containing written versions of numbers 
export NUMBERSCSV=egs/hausa/hausa_numbers.csv

#This is the translation of "Chapter" in the language. It's uttered at the beginning of each chapter followed with the chapter number
export CHAPTERUTT="Sura" 

#URLs
export AUDIOURLPREFIX=https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_
export OPENBIBLE_TEXT_ARCHIVE=https://downloads.open.bible/text/ha/haOSRK20/haOSRK20_USX.zip
export EBIBLE_TEXT_ARCHIVE=https://ebible.org/Scriptures/hausa_readaloud.zip

####
#Process starts from here
####

bash src/1-download_raw_data.sh

bash src/2-prepare_scripts.sh

bash src/3-setup_alignment.sh

bash src/4-perform_alignment.sh

bash src/5-extract_verses.sh