Implementing an Autograder
--------------------------

To implement an autograder, extend the `AutograderBase` class. In the constructor, make sure you call the constructor for the base class. After instantiating your autograder, call the `run()` method, which calls a function called `process`, which you must implement. `process` is passed the full path to a single project, and called by the base class for all of the projects. In this function, grade the files, and then call `output_grades` with the project name and a list of tuples contain the grade and comments for each part of the project. For example:

```
output_grades(project3_jsmith_jdoe, [(3, ''), (1, 'not enough detail')])
```

In order to be able to upload grades to CTools, you will need to implement the `handle_grade_row()` method in your class. It takes in a list of elements in a row of the grading CSV and returns a list StudentGrade objects.

After that, you simply need to make an instance of your autograder in the `main()` function and call `run()`. Then, you're good to go. You can also incorporate the `manual_grade` function into your autograder as described below.

Using an Autograder
-------------------

After downloading and unzipping the bulk_download.zip from CTools, run the grading script with the `init` subcommand. This will extract all of the tars from the folder, place them in a different directory, and then normalize the submissions and place them in a new directory. For example,

```
./grade_p3.py init --ctools /path/to/download/folder --untar /path/to/untar/folder -n-normalized /path/to/normalized/folder
```

The names of the directories in the normalized folder should be of the form `project2_name1_name2` (if they are not, they will either not be graded, or there may be issues extracting uniqnames). To grade these projects, run the following command:

```
./grade_p3.py grade -d /path/to/normalized/folder
```

If you were already part way through grading, you can do a "smart" resume grading by running:
```
./grade_p3.py grade -d /path/to/normalized/folder -s
```

If you were already part way through grading, you can manually resume from AFTER a given project by running:
```
./grade_p3.py grade -d /path/to/normalized/folder -r project3_jsmith_jdoe
```

To grade only one project, you can run:
```
./grade_p3.py grade -d /path/to/normalized/folder -t project3_jsmith_jdoe
```

Note that there may be some minor tweaking of constants in the scripts, but we've tried to reduce that to a minimum. After grading, you'll have several CSV files. Concatenate these together using the `cat` command into a combined grade CSV. However, this CSV file won't be in the correct format to upload to CTools.

Uploading to CTools
-------------------

This way should be used for autograders that extend the AutograderBase class.

Once the grading is done and you have your final CSV, you need to convert this into a format CTools can understand using the `create-upload` subcommand. First modify your grader define your handler in the `handle_grade_row()` method. Look at the existing handlers for an example of how to implement a handler. Each handler is passed a row of the CSV, with which you first extract the uniqnames, then grade each part of the project, then normalize the grades to 10 points, and then return a list of grades. Note that the names passed to the `extract_grade_part` function are used to generate the comments file. Once you've defined your handler, run a command similar to this:

```
./grade_hw4.py create-upload --ctools-zip bulk_download.zip --output-zip hw4_grades_upload.zip --grading-csv ./hw4_grades_final.csv
```
where `bulk_download.zip` is the zip downloaded from CTools, `hw4_grades_upload.zip` is the zip you'll upload to CTools, and `hw4_grades_final.csv` is the final grades for the project. Examine the output zip file to make sure it has grades and comments, then upload to CTools.

Uploading to CTools (old way)
-----------------------------

The following method is outdated and should only be used for autograders that have not been upgraded to use the AutograderBase class.

Once the grading is done and you have your final CSV, you need to convert this into a format CTools can understand using the `create_ctools_csv.py` script (which should eventually be merged into the base class, see the TODO section). First modify the `project_handlers` variable in the main function and define your handler. Look at the existing handlers for an example of how to implement a handler. Each handler is passed a row of the CSV, with which you first extract the uniqnames, then grade each part of the project, then normalize the grades to 10 points, and then return a list of grades. Note that the names passed to the `extract_grade_part` function are used to generate the comments file. Once you've defined your handler, run a command similar to this:

```
./create_ctools_csv.py --ctools-zip ~/Downloads/bulk_download.zip --output-zip p3_graded.zip --grading-csv project3_grades_final.csv --project p3
```

where `bulk_download.zip` is the zip downloaded from CTools, `p3_graded.zip` is the zip you'll upload to CTools, and `project3_grades_final.csv` is the final grades for the project. Examine the output zip file to make sure it has grades and comments, then upload to CTools.

Grading Homework
----------------

Because homeworks only have a single text file as a submission, homework autograders should inherit from `SingleFileAutograder`. Then, in the `process` function, you can do something simple like display the file so you can read the answers and type in a score and comments. Alternatively, you can use the `manual_grade` function in the `common_grading` module. This function parses out each answer in the given text file and displays it to you one by one, so you can grade each answer one at a time. Furthermore, if certain questions can be autograded, you can supply a dictionary of functions to autograde those questions, but let you manually grade the rest. For more details, see the docstring for the function.

You should generally try to use `manual_grade`, because this function produces a score/comment pair for each question, which makes it easy for the student to see where they lost points. However, sometimes we don't specify a format to use and students choose to use their own formatting, i.e. numbering with "(1)" instead of "1." (tip: make sure the file formats are specified in the project and homework specs before releasing the specs). You should do a quick grep to before grading to find any students who didn't follow the format, as their format might break the autograder, and if there are only a few cases, manually fix them. If for some reason you can't do this, you can use the `manual_grade_file` function, which will output the entire file, and allow you to continuously entire score/comment pairs until you type the letter 'q' for the score. The only problem with this is that it adds all the scores and comments you typed together, so it's hard for the student to see where they lost points. It's still useful if you can't get `manual_grade` to work.

TODO
----

Here are some things we still need to do:
- Write format checking and upload creater for students. This way, students will upload in a consistent format.
- The extracting functionality only searches for files with the extension .tar.gz. We should expand this to detect other files and at least log them, so we know they're there and can take points off for format, but not forget to grade them.
- Add functionality to the base class to only grade one problem at a time, and to merge individual problems from different CSV files. For example, project 3 has a coding question which takes a long time to grade, and is usually not graded with the other questions. It would be nice to tell the autograder which question to grade, and then with a CSV file for each question, easily merge them into one final CSV file (I actually wrote some starter code for this in `merge_questions.py`, but it needs to be fleshed out and put in the base class).
- Make `manual_grade` not screw up when the first word in a line is an IP address.
- Remove the normalizing step. This can be merged into the extract step, and is just a leftover from the old autograders.
- Make the project1 and project2 autograders implement the base class
- Automatically log all warning and error messages from the extraction into a log. This way, if there are some issues that effect grading (i.e. someone included files they shouldn't have in their tar file, or they submitted a zip file), they'll be output to a log and you can account for after you've finished the rest of the grading.
- Move grades to a better format (such as SQLite) that are just a single file. Could have schema that would mark problems as graded/ungraded. Also reduces the number of files.
