#! /bin/bash

#Bible speech scraping for Hausa

# Set environment variables
. ./egs/hausa/set_env.sh 

#Download Hausa MFA models 
mfa model download acoustic $LANG
mfa model download g2p $LANG\_g2p

####
#Process starts from here
####

bash src/1-download_raw_data.sh

bash src/2-prepare_scripts.sh

bash src/3-setup_alignment.sh

bash src/4-perform_alignment.sh

bash src/5-extract_verses.sh