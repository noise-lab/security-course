import argparse
import csv
import numpy
import os
import os.path
import re
import shutil
import subprocess
import sys
import StringIO
import tempfile
import traceback
import zipfile


class colors:
    RED     = '\033[31m'
    BLUE    = '\033[34m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    DEFAULT = '\033[0m'


class AutograderBase():
    def __init__(self, description, expected_files, optional_files,
                 submission_prefix, expected_dirs=[]):
        """
        Create AutograderBase object

        description - description of autograder
        expected_files - list of filenames expected in submission
        optional_files - list of filenames that are not required in submission
                         but can be included
        exptected_dirs - list of directories in submission that are required and
                         are include all children
        submission_prefix - prefix for submission_file
        """
        self.description = description
        self.expected_files = expected_files
        self.optional_files = optional_files
        self.expected_dirs = expected_dirs
        self.submission_prefix = submission_prefix

        self._have_init_csv = False
        self.csv_file_handle, self.csv_writer_handle = None, None

    def grade_filename(self, i):
        """Returns ith CSV grading file"""
        return os.path.join(os.path.abspath(os.path.curdir),
                            self.submission_prefix + '_grades%03d.csv' % i)

    def _init_csv(self):
        # Exit if have already initialized CSV members
        if self._have_init_csv:
            return

        # Select file to write grades
        csv_file_handle = None
        for i in range(1000):
            if not os.path.exists(self.grade_filename(i)):
                csv_file_handle = open(self.grade_filename(i), 'wb')
                csv_writer_handle = csv.writer(csv_file_handle)
                break

        self.csv_file_handle = csv_file_handle
        self.csv_writer_handle = csv_writer_handle
        self._have_init_csv = True

    def output_grades(self, name, grades):
        self._init_csv()
        grade_list = [os.path.normpath(name)] + [item for tup in grades for item in tup]
        self.csv_writer_handle.writerow(grade_list)
        self.csv_file_handle.flush()
        print grade_list

    def run(self):
        """Start grading and parsing arguments"""
        args = self.parse_arguments()

        if args.subcommand == 'init':
            # Do intial extracting and normalizing of submissions
            self.extract_and_normalize(os.path.normpath(args.ctools_dir),
                    os.path.normpath(args.untar_dir),
                    os.path.normpath(args.normalized_dir))
        elif args.subcommand == 'grade':
            # Grade projects
            assert os.path.isdir(args.proj_dir)
            if args.target is not None:
                # Grade one project
                assert not args.smart

                path = os.path.normpath(os.path.join(args.proj_dir, args.target))
                self.process(path)
            else:
                if args.smart:
                    assert args.resume is None
                    args.resume = self.get_resume_point()
                    if args.resume is None:
                        print 'No grading files found, starting from beginning'
                    else:
                        print 'Last graded was "%s"' % args.resume
                # Grade range of projects
                self.grade_projects(os.path.normpath(args.proj_dir),
                                    args.resume)
        elif args.subcommand == 'create-upload':
            # Create CTools upload ZIP
            download_zip = args.download_zip
            output_zip = args.output_zip
            grading_csv = args.grading_csv

            # Extract ZIP file
            tmp_dir = tempfile.mkdtemp(prefix='ctools-upload-')
            extracted_zip = extract_zip(download_zip, tmp_dir)

            # Read grading CSV
            grades = []
            with open(grading_csv, 'rb') as grading_csv_file:
                grading_reader = csv.reader(grading_csv_file)
                for row in grading_reader:
                    grades.extend(self.handle_grade_row(row))  # Get grades

            # Write grades to output CSV
            set_grades(extracted_zip, grades)

            # Write comments to coment files
            set_comments(extracted_zip, grades)

            # Create output ZIP
            zip_directory(extracted_zip, output_zip)

            # Delete tmp dir
            shutil.rmtree(tmp_dir)

            grades_list = [x.grade for x in grades]
            mean = round(numpy.mean(grades_list), 2)
            std_dev = round(numpy.std(grades_list), 2)
            median = round(numpy.median(grades_list), 2)

            print "== Upload to CTools and select 'Grade file' and 'Feedback comments' =="
            print 'Stats: mean=%.2f, std_dev=%.2f, median=%.2f' % (mean, std_dev, median)
        else:
            raise Exception('Unknown subcommand %s' % args.subcommand)

    def handle_grade_row(self, row):
        """Returns list of StudentGrade objects"""
        raise NotImplemented('Implement in child class')

    def get_resume_point(self):
        """
        Figure out the resume point (the last graded project) for grading
        based on the grades in csv
        """

        # Read in all csv files
        csv_file_contents = []
        for i in range(1000):
            if os.path.exists(self.grade_filename(i)):
                with open(self.grade_filename(i), 'r') as f:
                    csv_file_contents.append(f.read())

        # Check of no grade files found
        if len(csv_file_contents) == 0:
            return None

        csv_file_contents = ''.join(csv_file_contents)

        # Read combined CSV
        csv_buf = StringIO.StringIO(csv_file_contents)
        reader = csv.reader(csv_buf)

        # Get alphabetically last and return first column
        last_proj = sorted([row[0] for row in reader])[-1]
        csv_buf.close()
        return last_proj

    def parse_arguments(self):
        """Returns parsed program arguments"""
        parser = argparse.ArgumentParser(description=self.description)
        subparsers = parser.add_subparsers(dest='subcommand')
        init_parser = subparsers.add_parser('init', help='Extract and normalize tar files for this project')

        init_parser.add_argument('--ctools', dest='ctools_dir', required=True,
                                 help='Location of extracted "bulk_download.zip" folder')
        init_parser.add_argument('--untar', dest='untar_dir', required=True,
                                 help='Folder where extracted student tarballs will be stored')
        init_parser.add_argument('--normalized', dest='normalized_dir', required=True,
                                 help='Folder where normalized student submissions will be stored')

        grade_parser = subparsers.add_parser('grade', help='Grade the project')
        grade_parser.add_argument('-d', '--proj_dir',
                                  help="Directory of normalized submissions",
                                  required=True)
        group = grade_parser.add_mutually_exclusive_group()
        group.add_argument("-t", "--target", type=str, help='Grade this project only')
        group.add_argument("-r", "--resume", type=str,
                           help='Grade all projects after this project (alphabetically)')
        group.add_argument("-s", "--smart", action='store_true',
                           help='Try to figure out where to resume grading based on CSV grade files')

        create_upload_parser = subparsers.add_parser('create-upload',
                help='Create ZIP file to upload to CTOOLs')
        create_upload_parser.add_argument('--ctools-zip', dest='download_zip', required=True,
                help='location of CTools bulk download')
        create_upload_parser.add_argument('--output-zip', dest='output_zip', required=True,
                help='location output ZIP to upload')
        create_upload_parser.add_argument('--grading-csv', dest='grading_csv', required=True,
                help='Concatenated CSV with all grades')

        return parser.parse_args()

    def extract_and_normalize(self, ctools_dir, untar_dir, normalized_dir):
        extract(ctools_dir, untar_dir)
        normalize(untar_dir, normalized_dir, self.expected_files,
                          self.optional_files, self.expected_dirs)

    def project_dirs(self, proj_dir):
        """Returns list of project submissions (directory names)"""
        return sorted([x for x in os.listdir(proj_dir)
                       if x.startswith(self.submission_prefix) and
                       os.path.isdir(os.path.join(proj_dir, x))])

    def grade_projects(self, proj_dir, resume=None):
        """Grade all projects, optionally starting after resume"""
        proj_dirs = self.project_dirs(proj_dir)
        grade_projs = proj_dirs
        if resume is not None:
            resume = os.path.normpath(resume)
            assert(resume in proj_dirs)
            resume_idx = proj_dirs.index(resume)
            grade_projs = proj_dirs[resume_idx + 1:]
            print "Found %s; You have graded: %d / %d so far, keep going" %\
                  (resume, resume_idx + 1, len(proj_dirs))
            print "-----Commence grading-----"

        for i, p in enumerate(grade_projs):
            full = os.path.normpath(os.path.join(proj_dir, p))
            print '==== Grading "%s"' % p
            self.process(full)

    def process(self, project_path):
        raise NotImplemented('Implement this in children')


class SingleFileAutograder(AutograderBase):
    def __init__(self, expected_file, name, submission_prefix):
        self.grades = []
        self.names = []
        self.uname = ""

        assert isinstance(expected_file, str)
        self.expected_file = expected_file
        expected_files = [expected_file]

        AutograderBase.__init__(self, name, expected_files, [], submission_prefix)

    def extract_and_normalize(self, ctools_dir, untar_dir, normalized_dir,
                              expected_files, optional_files):
        extract_single_file_submissions(ctools_dir, untar_dir, self.submission_prefix)
        normalize_single_file_submissions(untar_dir, normalized_dir, self.expected_file)


def printc(c, message):
    print c + message + colors.DEFAULT

def manual_grade_file(filename, max_points):
    """
    This is a utility function that prints the entire contents of the file, and
    allows you to type  negative score/comment pairs until a 'q' is entered for
    the score. The total score (max points plus all the negative scores) and the
    joined comments are then returned.
    """
    if not os.path.exists(filename):
        return 0, 'no submission'

    # Regex magic to extract each answer
    with open(filename) as f:
        text = f.read()
        score = max_points
        comments = []
        printc(colors.GREEN, text)
        while True:
            subscore = raw_input("Subscore: ")
            if subscore == 'q':
                break

            subscore = float(subscore)
            # We only accept negative scores, because we only need to provide
            # score/comment pairs when the student does something wrong
            if subscore >= 0:
                printc(colors.YELLOW, "This function only accepts negative scores")
                continue

            comments.append(raw_input("Comments: "))
            score += subscore
        printc(colors.YELLOW, "score: " + str(score) + ',' + '. '.join(comments))

        return score, '. '.join(comments)

def manual_grade(filename, grading_funcs):
    """This is a utility function to help grade files where manual grading is required.

    The format of the input file should be:

        1. Student answer
           here
        answer continues until next answer or end of file, regardless of whitespace or newlines

        2. Second answer here

    This function will show you each answer one at a time, and allow you to enter a grade for that
    answer and optionally give a comment. it is still possible to use autograding for certain
    questions. Simply pass in a dictionary of question numbers (1-indexed) to grading functions,
    and those functions will be used to autograde those questions."""

    if not os.path.exists(filename):
        return 0, 'no submission'

    # Regex magic to extract each answer
    with open(filename) as f:
        text = f.read()
        answers = re.findall(r'^\d+\.[\S\s]*?(?=(?:^\d+\.)|(?:\Z))', text,
                             re.MULTILINE)

        results = []
        score = 0
        for i in range(1, len(answers) + 1):
            answer = answers[i - 1]
            printc(colors.BLUE, "Student answer:")
            printc(colors.GREEN, answer)
            subscore, comment = 0, ""
            if i in grading_funcs: # automatic grade
                subscore, comment = grading_funcs[i](answer)
                results.append((subscore, comment))
                score += subscore
            else: # Manual grade
                subscore = float(raw_input("Subscore: "))
                comment = raw_input("Comments: ")
                results.append((subscore, comment))
                score += subscore
            printc(colors.YELLOW, "score: " + str(subscore) + ", " + comment)

        printc(colors.YELLOW, str(results))
        printc(colors.YELLOW, "Total score: " + str(score))
        return results


# Globals used by grading gui functions

# TK modules
Tk = None
ttk = None
tkFont = None

# TK globals
grade = None
comment = None
multi_grades = None
text_font_size = 12
grade_input_width = 4
comment_input_width = 30
have_imported_TK = False
last_win_pos = (None, None)


def import_tkinter():
    """Eliminates file dependency on TKinter, only importing when needed"""
    global have_imported_TK, Tk, ttk, tkFont
    if not have_imported_TK:
        import Tkinter as Tk
        import ttk
        import tkFont
        have_imported_TK = True


def restore_win_pos(root):
    """If last_win_pos is set, set window to that location"""
    global last_win_pos
    last_x, last_y = last_win_pos
    if last_x is None or last_y is None:
        return
    root.geometry('+%d+%d' % last_win_pos)


def save_last_win_pos(root):
    """Save the current position of window to be restored with set_win_pos"""
    global last_win_pos
    geom = root.geometry()
    m = re.match("\d+x\d+\+(-?\d+)\+(-?\d+)", geom)
    if not m:
        print "Failed to parse geometry string %s" % repr(geom)
        print "Did not save window position"
        return
    last_win_pos = tuple(map(int, m.groups()))
    assert len(last_win_pos) == 2


def get_gui_check_grade(name, categories):
    """Display criteria for grade with checks"""
    import_tkinter()
    def onpress_cb(*args):
        global grade, comment
        grade = sum([var.get() for (cat, var, check) in fields])
        comment_fields = [cat for (cat, var, check) in fields if var.get() == 0]
        comment_fields.append(comment_entry.get())
        comment = '; '.join(comment_fields)
        print 'Grade (%d / %d); %s' % (grade, len(fields), comment)
        save_last_win_pos(root)
        root.destroy()

    def onenter_cb(*args):
        # Enter causes a check toggle, so undo the toggle
        if isinstance(root.focus_get(), Tk.Checkbutton):
            root.focus_get().toggle()
        onpress_cb(*args)

    global grade, comment
    grade = None
    comment = None
    root = Tk.Tk()
    restore_win_pos(root)
    root.title(name)
    text_font = tkFont.Font(size=text_font_size)

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(Tk.N, Tk.W, Tk.E, Tk.S))
    title = ttk.Label(mainframe, text=name, font=tkFont.Font(size=14), justify=Tk.CENTER)
    title.grid(column=0, row=0, sticky=Tk.W)
    note = ttk.Label(mainframe, text='Check criteria that are met:', font=text_font,
                     justify=Tk.CENTER)
    note.grid(column=0, row=1, sticky=Tk.W)
    fields = []
    for i,cat in enumerate(categories):
        var = Tk.IntVar()
        check = Tk.Checkbutton(mainframe, text=cat, variable=var, font=text_font)
        check.select()
        check.grid(column=0, row=i+2, sticky=Tk.W)
        fields.append((cat, var, check))

    # Comment
    comment_row = len(categories) + 2
    comment_subframe = ttk.Frame(mainframe, padding="3 3 12 12")
    comment_subframe.grid(column=0, row=comment_row, sticky=Tk.W)
    comment_label = ttk.Label(comment_subframe, text='Comment: ', font=text_font)
    comment_label.grid(column=0, row=0, sticky=Tk.W)
    comment_entry = ttk.Entry(comment_subframe, font=text_font, width=comment_input_width)
    comment_entry.grid(column=1, row=0, sticky=Tk.W)

    button_row = comment_row + 1
    button = Tk.Button(mainframe, text="OK", command=onpress_cb, font=text_font)
    button.grid(column=0, row=button_row)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    fields[0][2].focus()  # Focus on first checkbox
    root.bind('<Return>', onenter_cb)
    root.mainloop()

    if grade == None:
        print 'Closed window'
        sys.exit(1)

    return grade, comment


def get_gui_grade(name, max_score):
    """Show dialog box with comment and score input"""
    import_tkinter()
    def onpress_cb(*args):
        global grade, comment
        try:
            grade = float(grade_input.get())
        except:
            print 'Grade must be int or float'
            grade = None
            return
        if grade < 0:
            print 'Grade must be >= 0'
            grade = None
            return
        comment = comment_input.get()
        print 'Grade (%d / %d); %s' % (grade, max_score, comment)
        save_last_win_pos(root)
        root.destroy()

    global grade, comment
    grade = None
    comment = None
    root = Tk.Tk()
    restore_win_pos(root)
    root.title(name)
    text_font = tkFont.Font(size=text_font_size)

    # Title
    title = ttk.Label(root, text=name, font=tkFont.Font(size=14), justify=Tk.CENTER)
    title.pack()

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack()

    # Grade
    grade_label = ttk.Label(mainframe, text='grade', font=text_font)
    grade_label.grid(column=0, row=0, sticky=Tk.E)
    grade_subframe = ttk.Frame(mainframe, padding="3 3 12 12")
    grade_subframe.grid(column=1, row=0, sticky=Tk.W)
    grade_input = ttk.Entry(grade_subframe, font=text_font, width=grade_input_width)
    grade_input.insert(0, str(max_score))
    grade_input.grid(column=0, row=0, sticky=Tk.W)
    grade_label2 = ttk.Label(grade_subframe, text='/ %d' % max_score, font=text_font)
    grade_label2.grid(column=1, row=0, sticky=Tk.W)

    # Comment
    comment_label = ttk.Label(mainframe, text='comment', font=text_font)
    comment_label.grid(column=0, row=1, sticky=Tk.W)
    comment_input = ttk.Entry(mainframe, font=text_font, width=comment_input_width)
    comment_input.grid(column=1, row=1, sticky=Tk.W)

    # Button
    button = Tk.Button(root, text="OK", command=onpress_cb, font=text_font)
    button.pack()

    root.bind('<Return>', onpress_cb)
    grade_input.focus()
    grade_input.select_range(0, Tk.END)
    root.mainloop()

    if grade is None or comment is None:
        print 'Closed window'
        sys.exit(1)

    return grade, comment


def get_gui_multi_grades(name, questions):
    """
    Show dialog box with comment and score input for multiple parts
    Takes list of the form [('Part1', 5), ('Part2', 2), ...]
    """
    import_tkinter()
    assert len(questions) >= 1

    def onpress_cb(*args):
        global multi_grades
        tmp_multi_grades = []
        for (grade_entry, comment_entry), (quest, max_score) in zip(widgets, questions):
            try:
                grade = float(grade_entry.get())
            except:
                print 'Grade must be int or float'
                return
            if grade < 0:
                print 'Grade must be >= 0'
                return
            comment = comment_entry.get()
            tmp_multi_grades.append((grade, comment))
        multi_grades = tmp_multi_grades
        total_score = sum([x[0] for x in multi_grades])
        max_total_score = sum([x[1] for x in questions])
        print 'Grade (%.2f / %.2f)' % (total_score, max_total_score)
        save_last_win_pos(root)
        root.destroy()

    global multi_grades
    multi_grades = None

    root = Tk.Tk()
    restore_win_pos(root)
    root.title(name)
    text_font = tkFont.Font(size=text_font_size)


    # Title
    title = ttk.Label(root, text=name, font=tkFont.Font(size=14), justify=Tk.CENTER)
    title.pack()

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack()

    grade_subframe = ttk.Frame(mainframe, padding="3 3 12 12")
    grade_subframe.pack()

    ttk.Label(grade_subframe, text='Comment', font=text_font).grid(column=3, row=0)
    widgets = []
    for (i, (quest, max_score)) in enumerate(questions):
        i += 1
        # Label
        grade_label = ttk.Label(grade_subframe, text=quest, font=text_font)
        grade_label.grid(column=0, row=i, sticky=Tk.E, ipadx=20)

        # Entry
        grade_input = ttk.Entry(grade_subframe, font=text_font, width=grade_input_width)
        grade_input.insert(0, str(max_score))
        grade_input.grid(column=1, row=i, sticky=Tk.W)
        grade_label2 = ttk.Label(grade_subframe, text='/ %d' % max_score, font=text_font)
        grade_label2.grid(column=2, row=i, sticky=Tk.W, ipadx=20)

        # Comment
        comment_input = ttk.Entry(grade_subframe, font=text_font, width=comment_input_width)
        comment_input.grid(column=3, row=i, sticky=Tk.W)

        widgets.append((grade_input, comment_input))

    widgets[0][0].focus()
    widgets[0][0].select_range(0, Tk.END)

    # Button
    button = Tk.Button(root, text="OK", command=onpress_cb, font=text_font)
    button.pack()

    root.bind('<Return>', onpress_cb)
    root.mainloop()

    if multi_grades is None:
        print 'Closed window'
        sys.exit(1)

    return multi_grades


class Quest:
    """
    Represents a question.

    Optionally takes a list of common answers of the form:
    [('Name1', 1, 'Comment1'), ('Name2', 2, 'Comment2'), ...]
    """
    def __init__(self, name, max_score, common_answers=[]):
        self.name = name
        self.max_score = max_score
        self.common_answers = common_answers


def get_gui_multi_grades_fancy(name, parts):
    """
    Show dialog box with comment and score input for multiple parts
    Takes list of parts of the form:
      [('Part1', [quest1, quest2, ...]), ...]
    """
    import_tkinter()
    assert len(parts) >= 1

    def onpress_cb(*args):
        global multi_grades
        tmp_multi_grades = []
        question_lists = [quests for _, quests in parts]
        questions = []
        for ql in question_lists:
            questions.extend([(q.name, q.max_score) for q in ql])
        for (grade_entry, comment_entry), (quest, max_score) in zip(widgets, questions):
            try:
                grade = float(grade_entry.get())
            except:
                print 'Grade must be int or float'
                return
            if grade < 0:
                print 'Grade must be >= 0'
                return
            comment = comment_entry.get()
            tmp_multi_grades.append((grade, comment))
        multi_grades = tmp_multi_grades
        total_score = sum([x[0] for x in multi_grades])
        max_total_score = sum([x[1] for x in questions])
        print 'Grade (%.2f / %.2f)' % (total_score, max_total_score)
        save_last_win_pos(root)
        root.destroy()

    global multi_grades
    multi_grades = None

    root = Tk.Tk()
    restore_win_pos(root)
    root.title(name)
    text_font = tkFont.Font(size=text_font_size)

    # Title
    title = ttk.Label(root, text=name, font=tkFont.Font(size=14), justify=Tk.CENTER)
    title.pack()

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack()

    grade_subframe = ttk.Frame(mainframe, padding="3 3 12 12")
    grade_subframe.pack()

    row = 0
    ttk.Label(grade_subframe, text='Comment', font=text_font).grid(column=3, row=row)
    row += 1
    widgets = []
    for part_name, part_questions in parts:
        # Part label
        part_label = ttk.Label(grade_subframe, text=part_name, font=text_font)
        part_label.grid(column=0, row=row, columnspan=3, sticky=Tk.W)
        row += 1
        for quest in part_questions:
            # Label
            grade_label = ttk.Label(grade_subframe, text=quest.name, font=text_font)
            grade_label.grid(column=0, row=row, sticky=Tk.W, ipadx=20)

            # Entry
            grade_input = ttk.Entry(grade_subframe, font=text_font, width=grade_input_width)
            grade_input.insert(0, str(quest.max_score))
            grade_input.grid(column=1, row=row, sticky=Tk.W)
            grade_label2 = ttk.Label(grade_subframe, text='/ %d' % quest.max_score, font=text_font)
            grade_label2.grid(column=2, row=row, sticky=Tk.W, ipadx=20)

            # Comment
            if len(quest.common_answers) == 0:
                # Just normal entry field
                comment_input = ttk.Entry(grade_subframe, font=text_font, width=comment_input_width)
                comment_input.grid(column=3, row=row, sticky=Tk.W)
                widgets.append((grade_input, comment_input))

            else:
                # Add combobox
                values = [ans_name for ans_name, ans_score, ans_comment in quest.common_answers]
                comment_input = ttk.Combobox(grade_subframe, font=text_font, values=values, width=comment_input_width)
                comment_input._extra_store = (grade_input, quest)
                def combo_cb(event):
                    comment_input = event.widget
                    current = comment_input.current()
                    if current != -1:
                        (grade_input, quest) = comment_input._extra_store
                        (ans_name, ans_score, ans_comment) = quest.common_answers[current]
                        grade_input.delete(0, Tk.END)
                        grade_input.insert(0, ans_score)
                        comment_input.set(ans_comment)

                comment_input.bind('<<ComboboxSelected>>', combo_cb)
                comment_input.grid(column=3, row=row, sticky=Tk.W)
                widgets.append((grade_input, comment_input))

            row += 1

    widgets[0][0].focus()
    widgets[0][0].select_range(0, Tk.END)

    # Button
    button = Tk.Button(root, text="OK", command=onpress_cb, font=text_font)
    button.pack()

    root.bind('<Return>', onpress_cb)
    root.mainloop()

    if multi_grades is None:
        print 'Closed window'
        sys.exit(1)

    return multi_grades


def discover(path, regex, applyRegex=True, caseSensitive=True):
    """
    Returns generator of all files that match regex in path
    regex - pattern to match; interpretation depends on applyRegex
    applyRegex - if true, treat regex as regex object, else a string
    caseSensitive - if false, compares with lowercase version of all found files
        assumes that regex is lowercase for case insensitive searches
    """
    if not os.path.exists(path):
        printc(colors.RED, "ERROR: Path doesn't exist")
        sys.exit(1)

    for dirpath, _, files in os.walk(path):
        for file in files:
            filecmp = file if caseSensitive else file.lower()
            if ((applyRegex and regex.match(filecmp)) or
                    (not applyRegex and regex == filecmp)):
                yield os.path.join(dirpath, file)


def discover_dir(path, regex, applyRegex=True, caseSensitive=True):
    """
    Returns generator of all directories that match regex in path
    regex - pattern to match; interpretation depends on applyRegex
    applyRegex - if true, treat regex as regex object, else a string
    caseSensitive - if false, compares with lowercase version of all found directories
        assumes that regex is lowercase for case insensitive searches
    """
    if not os.path.exists(path):
        printc(colors.RED, "ERROR: Path doesn't exist")
        sys.exit(1)

    for dirpath, dirs, files in os.walk(path):
        for d in dirs:
            dcmp = d if caseSensitive else d.lower()
            if ((applyRegex and regex.match(dcmp)) or
                    (not applyRegex and regex == dcmp)):
                yield os.path.join(dirpath, d)


def discover_tarballs(path):
    "recursively walk a directory to find all tarballs"
    # Should add support for .tgz and .tar
    for f in discover(path, re.compile("^.*\.tar\.gz$")):
        yield f


def normalize_submission(path, normalized_dir, expected_files, optional_files, expected_dirs=[]):
    newpath = os.path.join(normalized_dir, path.split('/')[-1])
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    print 'Normalizing path "%s" into "%s"' % (path, newpath)

    expected_dirs_set = set(expected_dirs + ['.git'])
    for dirpath, dirnames, files in os.walk(path):
        # Exclude directories inside expected_dirs
        split_path_set = set([x.lower() for x in os.path.relpath(dirpath, path).split('/')])
        if not split_path_set.isdisjoint(expected_dirs_set):
            continue

        for f in files:
            # Only allow expected files and optional files, excluding hidden files
            if f.lower() not in expected_files and f.lower() not in optional_files and f[0] != '.':
                unexpected_file = os.path.relpath(os.path.join(dirpath, f), path)
                printc(colors.YELLOW, "INFO: File '%s' is not an expected file or optional file. Consider removing "
                                      "'points for format." % unexpected_file)

    copy_files(path, newpath, expected_files, False)
    copy_files(path, newpath, optional_files, True)
    copy_dirs(path, newpath, expected_dirs, False)


def copy_files(path, newpath, files, is_optional):
    for f in files:
        candidates = list(discover(path, f, applyRegex=False, caseSensitive=False))

        # Catch errors
        if len(candidates) > 1:
            printc(colors.RED, "ERROR: MULTIPLE CANDIDATES FOR file '%s' found. Delete all but one copy." % f)
            sys.exit(1)

        if len(candidates) == 0:
            if not is_optional:
                printc(colors.YELLOW, "INFO: could not find file '%s' in '%s'" % (f, newpath))
            continue

        if os.path.exists(os.path.join(newpath, f)):
            print "File already copied"
            continue

        # Copy file to newpath
        assert len(candidates) == 1
        shutil.copyfile(candidates[0], os.path.join(newpath, f))


def copy_dirs(path, newpath, dirs, is_optional):
    for expect_dir in dirs:
        candidates = list(discover_dir(path, expect_dir, applyRegex=False, caseSensitive=False))

        # Catch errors
        if len(candidates) > 1:
            printc(colors.RED, "ERROR: MULTIPLE CANDIDATES FOR folder '%s' found. Delete all but one copy." % expect_dir)
            sys.exit(1)

        if len(candidates) == 0:
            if not is_optional:
                printc(colors.YELLOW, "INFO: could not find folder '%s' in '%s'" % (expect_dir, newpath))
            continue

        if os.path.exists(os.path.join(newpath, expect_dir)):
            print "File already copied"
            continue

        # Copy file to newpath
        assert len(candidates) == 1
        shutil.copytree(candidates[0], os.path.join(newpath, expect_dir))


def extract(ctools_dir, untar_dir):
    print '========= Extracting submissions ============'
    orig_dir = os.getcwd()
    # extract tarballs into a rationally named directory structucture
    for f in discover_tarballs(ctools_dir):
        os.chdir(orig_dir)
        new_path = os.path.join(untar_dir,
                                '_'.join(f.split('/')[-1].split('.')[:-2]))
        if os.path.exists(new_path):
            printc(colors.YELLOW, "INFO: redundant submission: %s"
                   % f.split('/')[-1].split('.')[:-2])
        else:
            os.makedirs(new_path)
            try:
                subprocess.check_output(['tar', '-xf', f, '-C', new_path])
            except:
                print "TAR extract failed"
                print traceback.format_exc()
                try:
                    print "Attempting ZIP extract"
                    subprocess.check_output(['unzip', f, '-d', new_path])
                    printc(colors.YELLOW,
                           "INFO: Student submitted a zip file: %s" % f)
                except:
                    print "Unable to extract file '%s' to '%s'" % (f, new_path)
                    print traceback.format_exc()
                    sys.exit(-1)

    os.chdir(orig_dir)

def normalize(untar_dir, normalized_dir, expected_files, optional_files, expected_dirs=[]):
    print '========= Normalizing submissions ============'
    for f in sorted(os.listdir(untar_dir)):
        fullpath = os.path.join(untar_dir, f)
        normalize_submission(fullpath, normalized_dir, expected_files,
                             optional_files, expected_dirs)


def child_folders(path):
    """Returns list of full path of child folders of path (not recursive)"""
    for child in os.listdir(path):
        p = os.path.join(path, child)
        if os.path.isdir(p):
            yield p


def child_files(path):
    """Returns list of full path of child file of path (not recursive)"""
    for child in os.listdir(path):
        p = os.path.join(path, child)
        if os.path.isfile(p):
            yield p


def extract_single_file_submissions(ctools_dir, untar_dir, folder_prefix):
    """Extracts submission when submisison is single (non-archive) file"""
    print '========= Extracting submissions ============'
    orig_dir = os.getcwd()

    #print [x for x in child_folders(ctools_dir)]
    for f in list(child_folders(ctools_dir)):
        os.chdir(orig_dir)
        folder_name = os.path.basename(f)
        uniqname_matches = re.findall('\((.+)\)', folder_name)
        assert len(uniqname_matches) == 1
        uniqname = uniqname_matches[0]

        # Make directory
        dst_dir = os.path.join(untar_dir, folder_prefix + '_' + uniqname)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        sub_folder = os.path.join(f, 'Submission attachment(s)')
        children = os.listdir(sub_folder)
        if len(children) == 0:
            # No submission
            continue
        elif len(children) > 1:
            print 'Too many submissions in "%s"' % f
            printc(colors.YELLOW, '--> Copy submission manually to extract folder')
            raw_input('Hit Enter to continue... ')
            continue

        # Copy file
        sub_file = os.path.join(sub_folder, children[0])
        shutil.copy(sub_file, dst_dir)

    os.chdir(orig_dir)


def normalize_single_file_submissions(untar_dir, normalized_dir, dst_filename):
    """Normalizes submission when submisison is single (non-archive) file"""
    print '========= Normalizing submissions ============'
    for p in child_folders(untar_dir):
        sub_file_cands = list(child_files(p))
        if len(sub_file_cands) > 1:
            print 'Should only be one child file of "%s"' % p
            print 'Got %s' % repr(sub_file_cands)
            sys.exit(1)
        elif len(sub_file_cands) == 0:
            continue
        subfile = sub_file_cands[0]
        submit_dir = os.path.join(normalized_dir, os.path.basename(p))
        os.makedirs(submit_dir)
        dst_path = os.path.join(submit_dir, dst_filename)
        shutil.copyfile(subfile, dst_path)


def txt_submission_contents(text_file):
    """Returns contents of file as a string, correcting newlines"""
    with open(text_file, 'r') as f:
        # Correct newlines
        answer = f.read().replace('\r\n', '\n').replace('\r', '\n')
        return answer.rstrip() + '\n'


class StudentGrade(object):
    """Represents grade and comment for a given student"""
    def __init__(self, uniqname, grade, comment):
        self.uniqname = str(uniqname)
        self.grade = float(grade)
        self.comment = str(comment)

    def __repr__(self):
        return '<StudentGrade: uniqname=%s, grade=%.2f>' %\
               (self.uniqname, self.grade)


def extract_grading_uniqnames(s):
    """
    Extracts uniqnames of partners given string of the form:
    'project2_doe_smith'
    """

    names = s.split('_')[1:]
    return names


def pop_n(mylist, n):
    """Pop first n items from list and return as a tuple"""
    return tuple((mylist.pop(0) for _ in xrange(n)))


def extract_grade_part(row, section, parts, curr_state=None):
    """
    Get comment and grade for part of list of the form
    [grade1, comment1, grade2, comment2, ...]

    Returns tuple (grade, max_grade, comment)
    """
    if curr_state is None:
        curr_state = (0, 0, '')
    comment_lines = []
    curr_grade, curr_max_grade, curr_comment = curr_state
    part_grade = 0
    part_max_grade = 0
    for p_name, p_max_grade in parts:
        (grade, comment) = pop_n(row, 2)
        grade = float(grade)
        part_grade += grade
        part_max_grade += p_max_grade
        comment_lines.append('  %s: (%.2f/%.2f)  %s\n' % (p_name, grade, p_max_grade, comment))

    first_line = '%s (%.2f/%.2f):\n' % (section, part_grade, part_max_grade)
    comment_lines.insert(0, first_line)
    total_grade = curr_grade + part_grade
    total_comment = curr_comment + ''.join(comment_lines)
    total_max_grade = curr_max_grade + part_max_grade

    return total_grade, total_max_grade, total_comment


def extract_final_grade(curr_state, max_normalized_grade):
    """
    Add final line to comment that states final grade.
    Takes in grade to which to normalize grade.
    Also wraps comment in HTML pre tags
    """
    grade, max_grade, comment = curr_state
    comment += '\nGrade: %.2f / %.2f\n' % (grade, max_grade)
    normalized_grade = round((float(grade) / float(max_grade)) * float(max_normalized_grade), 1)
    comment += 'Normalized Grade: %.1f / %.1f\n' % (normalized_grade, max_normalized_grade)
    comment = '<pre>\n' + comment + '</pre>\n'
    return normalized_grade, max_normalized_grade, comment


def apply_late_penalty(row, max_normalized_grade, curr_state):
    """
    Applies late penalty percentage

    0: do nothing
    10: -10% max grade
    20: -20% max grade
    """
    grade, max_grade, comment = curr_state
    penalty_percent, penalty_comment = pop_n(row, 2)
    penalty_pts = (float(penalty_percent) / 100.0) * max_normalized_grade

    if penalty_pts > 1e-5:
        grade = max(round(grade - penalty_pts, 1), 0)
        comment += 'Penalty: %.1f%%  %s\n' % (float(penalty_percent), penalty_comment)
        comment += 'After Penalty: (%.1f / %.1f)\n' % (grade, max_normalized_grade)

    return grade, max_grade, comment


def set_grades(extracted_zip, grades):
    """Write grades to main grades.csv"""

    grade_csv = os.path.join(extracted_zip, 'grades.csv')

    # Read in CSV
    with open(grade_csv, 'rb') as f:
        reader = csv.reader(f)
        grade_rows = [row for row in reader]

    # Modify CSV data
    for gr in grades:
        row_cands = [r for r in grade_rows
                     if len(r) >= 2 and
                     r[0] == gr.uniqname and r[1] == gr.uniqname]
        assert len(row_cands) == 1
        row = row_cands[0]
        row[4] = '%.1f' % gr.grade  # Can only have 1 decimal place

    # Write data back to CSV
    with open(grade_csv, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(grade_rows)


def get_uniqname_dir(extracted_zip, uniqname):
    """Returns full path to directory with '(uniqname)'"""
    cands = []
    for f in sorted(os.listdir(extracted_zip)):
        full = os.path.join(extracted_zip, f)
        if os.path.isdir(full) and ('(%s)' % uniqname) in f:
            cands.append(full)

    assert len(cands) == 1
    return cands[0]


def set_comments(extracted_zip, grades):
    """Walk into extracted zip director and set comment.txt files"""
    for gr in grades:
        student_dir = get_uniqname_dir(extracted_zip, gr.uniqname)
        comment_file = os.path.join(student_dir, 'comments.txt')
        with open(comment_file, 'wb') as f:
            f.write(gr.comment)


def extract_zip(download_zip, output_dir):
    """Extracts zip to output dir and returns absolute path of child folder"""
    with zipfile.ZipFile(download_zip) as z:
        z.extractall(output_dir)

    children = os.listdir(output_dir)
    assert len(children) == 1
    return os.path.join(output_dir, children[0])


def zip_directory(directory, zip_loc):
    """Create ZIP archive of directory and place it in zip_loc"""
    with zipfile.ZipFile(zip_loc, 'w') as z:
        for root, dirs, files in os.walk(directory):
            for f in files:
                full = os.path.join(root, f)
                arc_path = os.path.relpath(full, os.path.dirname(directory))
                z.write(full, arc_path)
