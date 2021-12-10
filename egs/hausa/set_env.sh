export LANG=hausa 		#Language name as it is used in Montreal forced aligner
export WORKDIR=raw-data	#Directory to store raw data downloaded from open.bible
export OUTDIR=corpus	#Directory to store processed corpus files
export AUDIOFORMAT=wav	#mp3 or wav

#A file containing written forms of numbers in line by line format number<TAB>number in written form
export NUMBERSCSV=egs/hausa/numberdict.csv

#This is the translation of "Chapter" in the language. It's uttered at the beginning of each chapter followed with the chapter number
export CHAPTERUTT="Sura" 

#URLs - Fetch these for your language in https://open.bible/resources/ 
export AUDIOURLPREFIX=https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_
export OPENBIBLE_TEXT_ARCHIVE=https://downloads.open.bible/text/ha/haOSRK20/haOSRK20_USX.zip
export EBIBLE_TEXT_ARCHIVE=https://ebible.org/Scriptures/hausa_readaloud.zip

#Path to the file which contains chapter tag suffixes in the open.bible resources page source
export TAGSFILE=egs/hausa/openbible_chapter_tags.txt
