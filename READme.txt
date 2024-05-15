Pomodoro App Documentation
_____________________________________________________________________________________________________________________________
Overview:
The Pomodoro App is a simple implementation of the Pomodoro Technique, a time management method developed by Francesco Cirillo in the late 1980s. This technique involves breaking work into intervals, typically 25 minutes in length, separated by short breaks. After a certain number of work intervals, a longer break is taken. The Pomodoro App provides a user-friendly interface for users to track and manage their work intervals and breaks.
-----------------------------------------------------------------------------------------------------------------------------
Features:

Timer Mechanism:

The application allows users to start timers for work intervals, short breaks, and long breaks.
The duration of each interval is configurable through constants defined in the code.
Countdown Mechanism:

The countdown mechanism is implemented using the countdown() function, which updates the displayed time on the canvas every second until the countdown reaches zero.
Reset Timer:

Users can reset the timer at any time using the reset_timer() function.
This function cancels any ongoing countdown and resets the displayed time to "00:00".
User Interface (UI) Setup:

The UI is built using Tkinter widgets for a simple and intuitive user experience.
It includes a title label, a canvas for displaying the timer image and text, buttons for starting and resetting the timer, and a label for displaying check marks as a visual indication of completed work intervals.
Functionality:

When the "START" button is clicked, the timer starts counting down from the configured work duration.
After each work interval, a short break is taken, except after every 8th work interval, when a longer break is taken.
During breaks, the title label changes to indicate the break type (short or long).
Check marks are displayed to track completed work intervals.
------------------------------------------------------------------------------------------------------------------------------
Usage:
Run the Pomodoro App by executing the Python script pomodoro_app.py.
Use the "START" button to begin the timer for work intervals.
After each work interval, take a short break by allowing the timer to run.
After every 8th work interval, a longer break will be automatically taken.
Use the "RESET" button to reset the timer at any time.
------------------------------------------------------------------------------------------------------------------------------
Dependencies:
Python 3.x
Tkinter (Python's standard GUI library)
------------------------------------------------------------------------------------------------------------------------------
