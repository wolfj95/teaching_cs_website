#!/bin/bash

# This script uploads the built site content to the production server. 
# Just run `./upload.sh`, and ask Chris if you need help.

# Before you can use this script, you need to do the following:
# 1. Copy upload.template.sh to upload.sh (Don't change this file)
# 2. Get the values for HOST, USER, and PASS from someone who has them
#    and insert them into the spaces below, in upload.sh.

# WARNING: DO NOT COMMIT ANY FILES CONTAINING THESE SECRETS INTO GIT!

HOST='***'
USER='***'
PASS='***'
TARGETFOLDER='/'
SOURCEFOLDER='output_published/'

lftp -f "
set ssl:verify-certificate false
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
mirror --reverse --verbose $SOURCEFOLDER $TARGETFOLDER
bye
"

