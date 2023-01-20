# streaming-02-multiple-processes
## Abby Lloyd

> Multiple processes accessing a shared resource concurrently

## Overview

This example starts up a shared database and three different processes.

The processes represent multiple users, or locations, or programs 
hitting a shared database at the same time. 

## Prerequisite

Complete the setup at [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).

## About

Execute about.py to generate some useful information.

## First Run

Executing multiple_processes.py script.

Read the output. Read the code. 
Try to figure out what's going on. 

1. What libraries did we import? 
   - sqlite3, time, multiprocessing, os, datetime, platform, sys
2. Where do we set the task_duration? 
   - Line 34 
3. How many functions are defined? 
   - 7
4. What are the function names? 
   - create_table(), drop_table(), insert_pet(), process_one(), process_two(), process_three(), recreate_database()
5. In general, what does each function do? 
   - create_table() makes a tables named 'pets' using sqlite3   
   - drop_table() drops the table named 'pets'
   - insert_pet() adds a row to the table 'pets' with the pet name and breed
   - process_one(), process_two(), and process_three() all call insert_pet() to add pet names and breeds to the 'pets' table
   - recreate_database() deletes the table 'pets' and creates a new empty table named 'pets'
6. Where does the execution begin? 
   - Line 132 
7. How many processes do we start? 
   - 3
8. How many records does each process insert? 
   - 2

In this first run, we start 3 processes, 
each inserting 2 records into a shared database 
(for a total of 6 records inserted.)

In each case, the process gets a connection to the database, 
and a cursor to execute SQL statements.
They insert a record, and get out of the database quickly.

In general, we're successful and six new records get inserted. 

## Second Run

For the second run, modify the task_duration to make each task take 3 seconds. Run it again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with an error. 

## Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.

## Select All, Copy, Paste

On Windows the select all, copy, paste hotkeys are:

- CTRL a 
- CTRL c 
- CTRL v 

On a Mac the select all, copy, paste hotkeys are:

- Command a
- Command c
- Command v

Detailed copy/paste instructions (as needed)

1. To use these keys to transfer your output into a file, clear the terminal, run the script, then click in the terminal to make it active.
2. To select all terminal content, hold CTRL and the 'a' key together. 
3. To copy the selected content, hold CTRL and the 'c' key together. 
4. To paste, open the destination file (e.g. out0.py) for editing.
5. Click somewhere in the destination file to make it the active window.
6. Now hit CTRL a (both together) to select all of the destination file.
7. Hit CTRL v (both together) to paste the content from your clipboard.

Do a web search to find helpful videos on anything that seems confusing. 

## Reading Error Messages

Python has pretty helpful error messages. 
When you get an error, read them carefully. 

- What error do you get? 
  - sqlite3.OperationalError: database is locked
- Can you tell what line it was executing when it failed? 
  - insert_pet("P2", "Cooper", "Rabbit")


## Database Is Locked Error

Do a web search on the sqlite3 'database is locked' error.

- What do you learn? 
  - "This error occurs when more than one process is using the same session file, that is, when you run two or more clients at the same time using the same session name or in case another program has accessed the file" from https://docs.pyrogram.org/faq/sqlite3-operationalerror-database-is-locked
- Once a process fails, it crashes the main process and everything stops. 

## Deadlock

Deadlock is a special kind of locking issue where a process 
is waiting on a resource or process, that is waiting also. 

Rather than crashing, a system in deadlock may wait indefinitely, 
with no process able to move forward and make progress.

## Learn More

Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 

Notes:

Conditions for deadlock:
- Mutual Exclusion
- No Preemption: no force stopping a process
- Hold and Wait
- Circular Wait

Deadlock handling methods:
- Prevention
- Avoidance
- Detection and Recovery
- Ignorance



