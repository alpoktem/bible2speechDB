# bible2speechDB
Scripts to create speech corpora from open.bible resources

## Installation

Create a fresh conda environment and activate it

```
conda create -n aligner -c conda-forge sox python=3.8 openfst pynini ngram baumwelch
conda activate aligner
```

Install Montreal Forced Aligner (MFA)

```
pip install montreal-forced-aligner -U 
conda install -c conda-forge kaldi
mfa configure thirdparty download
```

Install required python modules

```
pip install -r requirements.txt
```

## Hausa complete run example

This will perform all the process from downloading of the raw data to chunking into sentences of the Hausa bible.

```
./egs/hausa/make_hausa.sh
```

## Running for a new language

#### Create the directory for language

```
mkdir egs/mylang
touch egs/mylang/set_env.sh
```

#### Fetch necessary information for the language you work with

1. Go to https://open.bible/resources/
2. Scroll down to your language
3. Note down the link where it says `DBL` (`OPENBIBLE_TEXT_ARCHIVE` in `set_env.sh`)
4. Click Audio files
5. View page source from your browser
6. Scroll down to section which looks like:

```
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_RIGHTS.rtf">Biblica® Open Hausa Contemporary Bible™ Audio Rights</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_01_GEN_mp3.zip">Genesis</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_02_EXO_mp3.zip">Exodus</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_03_LEV_mp3.zip">Leviticus</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_04_NUM_mp3.zip">Numbers</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_05_DEU_mp3.zip">Deuteronomy</a></li>
<li><a href="https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_06_JOS_mp3.zip">Joshua</a></li>
...
```

7. Note down the part `https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_` (`AUDIOURLPREFIX` in `set_env.sh`)
8. Note down the chapter tags on links on a text file (`egs/mylang/openbible_chapter_tags.txt`) line by line. In this example they go like `01_GEN`, `02_EXO`, `03_LEV`, `04_NUM`, `05_DEU`, `06_JOS`

#### Translate number dictionary to `egs/mylang/numberdict.csv`

You can build on the Hausa one and then translate

```
cp egs/hausa/numberdict.csv egs/mylang
```

#### Set environment variables `egs/mylang/set_env.sh` 

```
export LANG=mylang 		#Language name as it is used in Montreal Forced Aligner
export WORKDIR=raw-data	#Directory to store raw data downloaded from open.bible
export OUTDIR=corpus	#Directory to store processed corpus files
export AUDIOFORMAT=mp3	#mp3 or wav

#A file containing written forms of numbers in line by line format number<TAB>number in written form
export NUMBERSCSV=egs/mylang/numberdict.csv

#This is the translation of "Chapter" in the language. It's uttered at the beginning of each chapter followed with the chapter number
export CHAPTERUTT="Chapter" 

#URLs - Fetch these for your language in https://open.bible/resources/ 
export AUDIOURLPREFIX=https://downloads.open.bible/audio/ha/haOSRK20/haOSRK20_
export OPENBIBLE_TEXT_ARCHIVE=https://downloads.open.bible/text/ha/haOSRK20/haOSRK20_USX.zip

#Path to the file which contains chapter tag suffixes in the open.bible resources page source
export TAGSFILE=egs/mylang/openbible_chapter_tags.txt
```

Finally, run the whole process with:


## Partial run example

You might need to go step by step. To do that, set the environment variables and then call the script you want:

```
chmod u+x egs/hausa/set_env.sh
. ./egs/hausa/set_env.sh
bash src/1-download_raw_data.sh
```