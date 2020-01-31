## Goal: Submit to Canvas from Codio by clicking a button
### What skills do I need to be successful doing this?
If you're in 595, you have the skills. While the code uses python, you don't have to write any python.***

### Overall, the steps are
Task | Time to Complete
------------ | -------------
 get a key                  |     approx 3 minutes
 get this code              |     approx 3 minutes
 add key to code            |     approx 3 minutes
 install python3-venv       |     approx 1 minute
 check your Makefile        |     approx 1-10 minutes
 update your .codio file    |     approx 1-10 minutes
 Total                      |     approx 12-30 minutes


This document is populated with [\_] items. That means you have to do those things before moving on to the next step. If you see text and no [_], it means you don't have to do anything.

### [\_] Go get an API key from Canvas:
Click on Account, then Settings. Scroll down to "Approved Integrations" and click "+ New Access Token." Give the token a sensible name (this is just for your own benefit) and give it an expiration date of like, June. By then you'll be sipping MaiTais on a beach and won't need the token. I'll refer to the token as an API key. Copy it to use in the next step.

(Don't share your API key. It's like a username and pw all wrapped into one. Whatever you can do with your username/pw, you can do with your API key. If you ask me for help (and you're more than welcome to), don't include the key.)

### [\_] Make a folder in codio called `submitter`.
- Put 3 files from this repo into the submitter folder:
  - [\_] a config-sample.py file (where you can put your sensitive information like API key). Copy/rename the file config.py and paste in your API key info from the Canvas website.
  - [\_] canvas-submit.py (it has the code to submit your hw)
  - [\_] requirements.txt (python will use  this to download any necessary libraries. (I only required canvaspi, the _official_ python api of Canvas. All the other requirements are the ones that canvasapi then required.))

Cool. You're doing so well.

Alright.

### [\_] Get venv for python3
Give your codio environment the ability to do venv for python3 (this means the our python code will run in a local folder that won't interfere with other things). Type in terminal:

```sudo apt-get install python3-venv```

### [_] Have a submission recipe.
Your Makefile should include a submission recipe. If not, add one. It should zip the correct files into a submission.zip file. For part one, it might be:

```
submission: all
	tar -czvf submission.zip find_symbols.c find_symbols_test.c Makefile
```
For part 2 it might be:
```
submission: all
  tar -czvf submission.zip find_symbols.c symbol_table.c symbol_table_test.c populate_symbol_table_test.c Makefile
```
### [\_] Now paste this in terminal.

```
make submission; python3 -m venv python-lives-here; source python-lives-here/bin/activate; pip install -r submitter/requirements.txt; python submitter/canvas-submit.py
```

It runs the submission recipe from your makefile, then builds an environment to run the submitter code, and runs the submitter code. If it comes back and says kind things, you're good. In order to make it a one-click action, paste it into your .codio file as a command. For example, my commands in .codio file is like:
```
"commands": {
        "Lets Test!!" : "make all; ./test_find_symbols",
        "Valgrind, please~~" : "make all; valgrind ./test_find_symbols",
        "Submit Part 1" : "make submission; python3 -m venv python-lives-here; source python-lives-here/bin/activate; pip install -r submitter/requirements.txt; python submitter/canvas-submit.py"
    }
```

(This is happening in a folder called 'python-lives-here'. You can delete that folder. Or not. If you delete it, it'll regenerate the next time you run. If you leave it there, you'll save time on the next run.)  

  So in order to submit hw, click the toolbar!

  Did you hit a snag? Ask on piazza or DM on Slack. Is the documentation not perfect? Fix it and submit a pull request. It'd make my dang day.

  *** Going forward, you'll have to change the assignment_id. Uncomment/comment the lines in the canvas-submit.py file as necessary.
