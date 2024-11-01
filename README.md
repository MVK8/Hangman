# A simple Hangman game but with themes!

**Video Demo:** [Watch here](https://www.youtube.com/oops)


Hello, world! This is my project and from the title you can already tell what it is. But before we go any further make sure you
installed the required modules:

##### Pyfiglet: [read more](https://pypi.org/project/pyfiglet/)

this gets used to display ASCII text art,
you can install it with the following command:

```pip install pyfiglet```

##### Pytest: [read more](https://docs.pytest.org/en/stable/)

this gets used for **"test_project.py"** to make sure every function works properly,
you can install it with:

```pip install pytest```

After you have installed the modules and already know how Hangman works you can give the game a try with the following command: ```python project.py```
but if you are unsure on how the game works here is a brief explanation:

### Objective of the game:

The objective is to guess a random word from  a .csv file in a certain amount of attempts, in this case, you get 6 attemps before you lose.
The way you can guess is by typing a single character and seeing if that character is in the word.
If the character is in the word, you get to see where it is located and how often it comes up in the word but
If you guess incorrectly, you lose an attempt and this gets visualized by drawing a part of a character on a gallow.


#### Example:

Let’s try it with an example if the word is **"test"**
and if you guess: **"T"** you will see:
```bash

  +---+
  |   |
      |
      |
      |
      |
==========
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
word:  t _ _ t
```
But if you guess: **"R"** which is incorrect:
```bash

  +---+
  |   |
  O   |
      |
      |
      |
==========
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
word:  t _ _ t
 ```

As you can see you see a piece of the character (The head) appeared because you guessed incorrecly.
The game will continue until you guess the entire word in this case it will be **"test"** or your entire
character gets drawn, a.k.a you run out of attempts.

### Themes:

The game comes with 3 built in themes:

 ```bash
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
please choose a Theme:
(1) History
(2) Countries
(3) Elements
(4) Custom
(5) Exit
 ```
Here you can see all the built in themes in the game. You can select one by typing the number before the name of the theme you want to select.
 As you can see there is also a fourth option called "Custom" this is meant for themes that you add on your own, more on that here:


### Reading / making custom themes:

#### Making themes:

Before selecting any custom themes you have to make one first this can be done by selecting number **"2"**
 ```bash
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
please choose what you would like to do:
(1) Begin the game
(2) Add custom theme
(3) Exit
 ```
After selecting it you will end up at this screen:
 ```bash
Please enter the name of your file (exclude .csv): test
 ```
Here you will be promted to enter the name of the file (**make sure to exclude the .csv**). For this example we will use the name **"test"** after that
you will be promted to enter the words you want in the theme:
 ```bash
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use /exit to save and exit the file
Word: test2
```
After you have entered all your desired words you want in the theme (in this case we will only add one word **"test2"** for this example) you
 can use "/exit" to save it. Now our file is saved and we can use the theme.

#### Reading Themes:

Now to read the file we go back to this screen and select number **"4"**:
```bash
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
please choose a Theme:
(1) History
(2) Countries
(3) Elements
(4) Custom
(5) Exit
```
You will be promted this:

```bash
Available files:
test.csv
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enter the name of an .csv file: test.csv
```
Here we select a file from the available files and enter the name (**include the .csv**).For the example we enter **"test.csv"**
```bash
  +---+
  |   |
      |
      |
      |
      |
==========
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
word:  te_ t2
```

And as you can see after a few correct attempts the word was indeed  **"test2"**

#### Customization / Safeguards:

I have chosen to use the.csv file format txt to make it easier for future customization, like adding multiple difficulties. Along with each part of the
program is put in their own function to make it more user friendly to read and customize the code. As far as it goes for safeguards I have
multiple basic filters installed, like inputting the wrong number or receiving blank input, but keep in mind I have performed multiple tests to
Make sure the program doesn't crash, but that doesn't mean it's bulletproof (reporting bugs is appreciated).

#### What each file does:


##### Project Structure:

- `1.csv`
- `2.csv`
- `3.csv`
- `project.py`
- `README.md`
- `requirements.txt`
- `test_project.py`

From the project structure you may have noticed that there are multiple .csv files called "1.csv","2.csv and "3.csv" these files are for the inbuilt themes
which link back to which number you enter on the theme selector. Along with "project.py" which is the main file there is also "test_project.py" which
is for testing each function if they fully work, you can test it with the following command: ```pytest test_project.py```. In "requirements.txt" all the
 required modules are noted.

### The role of each function in the program:


####  main():
Main() function has 0 parameters. And is mainly responsible for reciving and redirecting information to and from functions. The main() function also captures the name of the user and redirects it to other other functions.


#### menu(name):

The Menu() function has 1 parameter, this is for the username. The menu() function is mainly responsible for
 detecting the users input and filtering any wrong input and forwardng it to the main() function.

#### game_mode(n, name):

The game_mode() function has 2 parameters which is for the output from menu() and the username. The game_mode() function is responsible to determining
 what the user wants to do and determining the right .csv file for the game. The game_mode() function is also responsible for handeling the custom
 theme option and redirecting the right .csv file  to the word_maker() function.

 #### word_maker(n)
 The word_maker function has 1 paramater which is the .csv file name recived from game_mode((). The word_maker() function is responsible for reading the csv
 file and selecting a random word and redirecting this to the game_maker() function.

#### game_maker(n, name)
The game_maker() function has 2 paramaters, which is the word recieved from the word maker and the username.
 The game_make() function is responsible for generating the game environment like the gallow and keeping count on how many wrong attempts were made. The game_maker() function is also responsible for showing the users' statistics on the end screen.

#### theme_maker()
The theme_maker() has 0 parameters. This function is responsible for everything related for creating and saving .csv files.

#### game_exit(name)
The game_exit() function has 1 parameter, which is for the username. The game_exit() function is responsible for exiting the program and giving the user a goodbye.





 ###### *If you find any bugs or grammatical mistakes, it please report them, as I'm not a native speaker or the best programmer. Haha*
