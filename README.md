# tabularize_top_stats
Tabularizes dinamic stats from top
Example usage:
top -b | awk '/Web Content/ { print strftime("%T"), $1, $9, $10; fflush(); }' | python tabularize_top_stats.py
