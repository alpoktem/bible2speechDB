#! /bin/bash

#Bible speech scraper environment variables for Hausa

export LANG=hausa
export WORKDIR=raw-data
export OUTDIR=corpus
export AUDIOFORMAT=mp3 #mp3 or wav

#TODO: Describe this file
export TAGSFILE=egs/hausa/openbible_chapter_tags_EST.txt

#A file containing written versions of numbers 
export NUMBERSCSV=egs/hausa/hausa_numbers.csv

#This is the translation of "Chapter" in the language. It's uttered at the beginning of each chapter followed with the chapter number
export CHAPTERUTT="Sura" 

#URLs
export AUDIOURLPREFIX=https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_
export OPENBIBLE_TEXT_ARCHIVE=https://downloads.open.bible/text/ha/haOSRK20/haOSRK20_USX.zip
export EBIBLE_TEXT_ARCHIVE=https://ebible.org/Scriptures/hausa_readaloud.zip