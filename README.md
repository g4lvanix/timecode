## Timecode - Morse code time announcement

This project allows you to output your system time in Morse code through your
computer speakers.

**generate.py** - used to generate the needed audio files for the numbers 0 to 9. Code speed is adjustable via the *wpm* variable.

**timecode.sh** - bash script that gets current system time and uses aplay to play the corresponding WAV files.

In order to have the system time automatically announced via Morse code, you can
set up a cron job.

Before the timecode.sh script can output the time, you need to generate the wave files
fist using `python3 generate.py`. You need to rerun this script every time you change the
settings like WPM or tone frequency.

To announce the system time every 15 minutes assuming you cloned the repo to `/home/username/timecode` you can setup a cron job using `crontab -e`:
```
*/15 * * * * bash /home/username/timecode/timecode.sh
```
