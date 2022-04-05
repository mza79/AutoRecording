Auto stream recording script using face detection developed using pycharm

having the recording program installed: Using EV record screen program

ie. ctrl+f1 : start record
    ctrl+f2: end record
    
    
program's initial state monitors the screen for face detections.

and will press "ctrl+f1" to record screen when detecting faces.


Program will continously perform face detections to check the stream is still going

After 5 minutes of lost face detection, program will persume the stream has ended

and will send "ctrl+f2" to stop recording, then return to detection state



Direct to the webpage of desired stream channels and start the program

you can go to sleep, eat, ect. and not missing out your favourite stream channel.


Build directory is project build using pyinstaller:
pyinstaller main.py --console

source code: main.py


