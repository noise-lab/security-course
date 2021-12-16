#!/bin/bash
# check arguments
if [ "$#" -ne 2 ]; then
  echo "usage: ./format_msg.sh {original_text} {output}"
  exit 1
fi

# skips blank lines
# trim trailing ^M
# trim leading whitespace
# pick lines longer than 60
grep -vE '^(\s*$)' $1 | tr -d '\r' | sed 's/^[ \t]*//' | awk 'length($0) > 60' > $2
