THE POMODORO APP USING PYTHON AND TKINDER
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project is a simple implementation of the Pomodoro Technique using the Tkinter library in Python. 
The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. 
It involves breaking work into intervals, traditionally 25 minutes in length, separated by short breaks.
After a certain number of work intervals, a longer break is taken.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
->Timer Mechanism: The application allows users to start a timer for work intervals, short breaks, and long breaks. Each interval duration is configurable through constants defined at the beginning of the code.

->Countdown Mechanism: The countdown mechanism is implemented using the countdown() function, which updates the displayed time on the canvas every second until the countdown reaches zero.

->Reset Timer: The reset_timer() function allows users to reset the timer, cancelling any ongoing countdown and resetting the displayed time to "00:00".

->UI Setup: The user interface (UI) is built using Tkinter widgets. It includes a title label, a canvas for displaying the timer image and text, buttons for starting and resetting the timer, and a label for displaying check marks as a visual indication of completed work intervals.

->Functionality: When the "START" button is clicked, the timer starts counting down from the configured work duration. After each work interval, a short break is taken, except after every 8th work interval, when a longer break is taken. During breaks, the title label changes to indicate the break type (short or long). Check marks are displayed to track completed work intervals.
