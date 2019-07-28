# Stanford Scheduler

The goal of this project was to create a Stanford version of MIT's Firehose Course Scheduler(https://firehose.guide/).

This program will launch a GUI that will allow you to get a live view of the course that you might be considering
and allow you to quickly spot any scheduling conflicts and such. The same view is available in Carta (https://carta.stanford.edu), however I personally thought it was a bit ugly and you can't see it in full screen.


Currently, this only supports lecture times and excludes sections. If there is more than one lecture time available during
any given quarter, than you will be prompted to pick one before it is added to your schedule.

## Requirements:

- `Python 3.X` (Not by Python2, not sure and not willing to try it. Its a dying language. Move on.)
    - If you do not already have Python installed, I would highly recommend doing so using Ananconda as it comes with all sorts of features ( `conda` CLI, package manager, etc.) (https://www.anaconda.com/distribution/)
- `PyQt5` (If you have `pip` installed, I have included a bash script that should be able to install PyQt5 easily)

## Instructions:

- Open the terminal
