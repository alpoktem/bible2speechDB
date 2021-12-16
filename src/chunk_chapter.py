import os
import sys
from praatio import textgrid
import subprocess
from pydub import AudioSegment
from text_utils import normalize_text

QUIET=False

audio_file = sys.argv[1]
aligned_textgrid_file = sys.argv[2]
text_file = sys.argv[3]
out_chunk_dir = sys.argv[4]
out_text_dir = sys.argv[5]

audio_id = os.path.splitext(os.path.basename(audio_file))[0]
audio_chunk_dir = os.path.join(out_chunk_dir, audio_id)
text_chunk_dir = os.path.join(out_text_dir, 'original', audio_id)
norm_text_chunk_dir = os.path.join(out_text_dir, 'normalized', audio_id)

if not os.path.exists(audio_chunk_dir):
    os.makedirs(audio_chunk_dir)

if not os.path.exists(text_chunk_dir):
    os.makedirs(text_chunk_dir)

if not os.path.exists(norm_text_chunk_dir):
    os.makedirs(norm_text_chunk_dir)

def audio_convert(audio_path, quiet=False):
    """Converts audio to mono wav (unless it's already or there's a converted version in the same directory)"""
    do_convert = False
    if os.path.splitext(audio_path)[1][1:] == 'wav':
        wav_path = audio_path
    else:
        wav_path = os.path.join(os.path.dirname(audio_path), os.path.splitext(os.path.basename(audio_path))[0] + '.wav')
        if os.path.exists(wav_path):
            return audio_convert(wav_path, quiet)
        else:
            do_convert = True

    if do_convert:
        if not quiet:
            print("Converting audio to wav", wav_path)
        process = subprocess.call(['ffmpeg', '-loglevel', 'quiet', '-i',
                                        audio_path, '-ac', '1', wav_path])

        return wav_path
    else:
        if not quiet:          
            print("Reading wav file", audio_path)

        return audio_path

def dump_chunk(audio, start_sec, end_sec, text, chunk_dir, text_dir, norm_text_dir, file_prefix=""):
    """Cuts and places a chunk of audio to path (for revision)"""

    start_ms = start_sec * 1000
    end_ms = end_sec * 1000

    audio_chunk_filename = file_prefix #+ "_" + "%.2f"%start_sec + "-" + "%.2f"%end_sec 
    audio_chunk_path = os.path.join(chunk_dir, audio_chunk_filename + ".wav")
    text_chunk_path = os.path.join(text_dir, audio_chunk_filename + ".txt")
    norm_text_chunk_path = os.path.join(norm_text_dir, audio_chunk_filename + ".norm.txt")
    
    if not os.path.exists(audio_chunk_path):
        audio_segment = audio[int(start_ms):int(end_ms)]
        audio_segment.export(audio_chunk_path, format="wav")
    
    with open(text_chunk_path, 'w') as f:
        f.write(text)

    with open(norm_text_chunk_path, 'w') as f:
        f.write(normalize_text(text, remove_punc=True))
    
    return audio_chunk_path

#Read textgrid
tg = textgrid.openTextgrid(aligned_textgrid_file, False)
words_tier = tg.tierDict['words']

#Read audio
audio_path = audio_convert(audio_file, quiet=QUIET)
complete_audio = AudioSegment.from_wav(audio_path)

#Parse plain text while keeping track in textgrid and store sentence beginnings and endings
segments_data = []

tg_word_index = 0

with open(text_file, 'r') as f:
    for i, l in enumerate(f):
        sura = l.strip()
        
        sura_words = sura.split()
        
        sura_intervals = words_tier.entryList[tg_word_index:tg_word_index+len(sura_words)]

        sura_beginning = normalize_text(sura_words[0], remove_punc=True).replace('’', "'")
        sura_end = normalize_text(sura_words[-1], remove_punc=True).replace('’', "'")

        if not sura_intervals[0].label == sura_beginning or not sura_intervals[-1].label == sura_end:
            if not QUIET:
                print(sura)
                print(sura_intervals)
                print(sura_intervals[0].label + " - " +  sura_beginning)
                print(sura_intervals[-1].label + " - " +  sura_end)
                print("-------------------")
            print("WARNING: Misalignment between textgrid and script. Stopped chunking after %i segments"%len(segments_data))
            break

        segment = {'text':sura, 'start':sura_intervals[0].start, 'end':sura_intervals[-1].end}
        segments_data.append(segment)
            
        #Dump chunk
        chunk_id = '{:03}'.format(i)
        dump_chunk(complete_audio, sura_intervals[0].start, 
                   sura_intervals[-1].end, sura, 
                   audio_chunk_dir, text_chunk_dir, 
                   norm_text_chunk_dir,file_prefix=audio_id + "_" +chunk_id)
        
        tg_word_index += len(sura_intervals)

# print(len(segments_data), 'segments')
