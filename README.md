# journal-logger

A logger object that enables logging to systemd journal (`journalctl`)

### Installation with Poetry
```bash
git clone https://github.com/kirisakow/journal-logger.git

cd your-project

poetry install --editable ../rel/path/to/journal-logger/
```

### Usage examples:
```py
import logging
from journal_logger.journal_logger import JournalLogger

logging.basicConfig(level=logging.DEBUG)
jl = JournalLogger(program_name='myProgram') # whatever string to represent your program logs in journalctl

def my_function():
    jl.print("both program name and function name will be logged at the beginning of this record")

if __name__ == '__main__':
    jl.print("program name you've set will be logged at the beginning of this record")
    my_function()
```
The output you'll see in systemd journal:
```log
...
Jun 04 13:19:10 hostname python[75310]: myProgram: program name you've set will be logged at the beginning of this record
Jun 04 13:19:10 hostname python[75310]: myProgram: my_function: both program name and function name will be logged at the beginning of this record
...
```