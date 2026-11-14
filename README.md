# Python Log Analyzer

A small Python script that reads an authentication log, counts failed logins for each IP address and flags IPs that reach a threshold, which can indicate a brute-force attempt. It uses the same idea as my Splunk brute force detection, written from scratch in Python.

## How it works
1. Reads `sample-auth.log` line by line
2. Keeps only the `FAILED` lines
3. Extracts the IP address from each line
4. Counts failures per IP in a dictionary
5. Prints an alert for any IP at or above the threshold (default 5) and saves it to `report.txt`

## Run it
```
python analyzer.py
```
Requires Python 3. No extra packages.

## Example output
```
ALERT: 203.0.113.45 8 failed logins
ALERT: 203.0.113.99 6 failed logins
```

## About the data
`sample-auth.log` is made up of several Ip addresses that were generated randomly. The IP addresses come from ranges reserved for documentation, so they do not belong to real people.

## Limitations and next steps
- The log file name and the threshold are fixed in the code
- It counts failures over the whole file and ignores timing, so it can't tell 5 failures in a minute from 5 failures in a week
- It doesn't check IPs against a threat intelligence source yet only from the sample log file.

## What I learned
- I learned how to use a dictionary to count how many times each IP address appeared in the log.
- I learned how to split each log line into pieces, then split ip=203.0.113.45 at the = sign so only the clean IP address was left.
  
