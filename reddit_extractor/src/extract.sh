#! /bin/bash

YYYY_MM=2020-06
INPUT="/media/ryan/7A70BC3170BBF24D/input"
OUTPUT="/media/ryan/7A70BC3170BBF24D/output"

python reddit.py "$YYYY_MM" \
    --task=extract \
    --wl_subreddits "../lists/subreddits.whitelist.txt" \
    --parallel=True \
    --reddit_input "$INPUT" \
    --reddit_output "$OUTPUT" \
    --clean True \
    --min_score 1 \
    --min_depth 2 \
    --max_depth 5 \
    --use_title 0 \
    --leaves_only 0
