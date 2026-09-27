import pandas as pd

df=pd.read_csv("student_data.csv")
df["Avg Marks"]=df[["Maths","Science","English"]].mean(axis=1)
df["Total Marks"]=df[["Maths","Science","English"]].sum(axis=1)
df["Grade"]=df["Avg Marks"].apply(
        lambda x:"A+" if x>90 else
             "A" if x>80 else
             "B+" if x>70 else
             "B" if x>60 else
             "C" if x>35 else
             "Fail")

print("---Student Performance Analysis System---")
print("1.Load Dataset")
print("2.Student Analysis")
print("3.Marks Analysis")
print("4.Student Performance")
print("5.Subject Analysis")
print("6.Attendance Analysis")
print("7.Department Gender Analysis")
print("8.Data Operation")
print("\n")

choice=input("Enter the Choice:")
def load_dataset(df):
    print("First Few Records:\n",df.head())
    print("Last Few Records:\n",df.tail())
    print("\n")
    print("Number of Rows and columns:",df.shape)
    print("All Columns Name:\n",df.columns)
    print("data Types of each column:\n",df.dtypes)
    print("Null values in each column:",df.isnull())
    print("\n")
# load_dataset(df)

def student_analysis(df):
    print("Number of Students:",df["Name"].count())

    subjects=["Maths","Science","English"]
    print("Number of Subjects:",len(subjects))

    avg_attendance=df["Attendance"].mean()
    high_attendance=df["Attendance"].max()
    low_attendance=df["Attendance"].min()
    print("Average Attendance of the Class:",avg_attendance)
    print("Higest attendance of the class:",high_attendance)
    print("Lowest attendance of the class:",low_attendance)
    print("\n")
# student_analysis(df)

def marks_analysis(df):
    print("Total Marks of Each Student\n")
    # df["Total Marks"]=df[["Maths","Science","English"]].sum(axis=1)
    print(df[["USN","Name","Department","Maths","Science","English","Total Marks"]])
    print("\n")

    print("Avg Marks of Each Student\n")
    # df["Avg Marks"]=df[["Maths","Science","English"]].mean(axis=1)
    print(df[["USN","Name","Department","Maths","Science","English","Total Marks","Avg Marks"]])
    print("\n")

    print("Grade of Each Student\n")
    # df["Grade"]=df["Avg Marks"].apply(
    #     lambda x:"A" if x>85 else
    #          "B" if x>65 else
    #          "C" if x>45 else
    #          "Fail")
    print(df[["USN","Name","Department","Maths","Science","English","Total Marks","Avg Marks","Grade"]])
    print("\n")

    class_avg=df["Avg Marks"].mean()
    high_total_marks=df["Total Marks"].max()
    low_total_marks=df["Total Marks"].min()
    print("The total class average is:",class_avg)
    print("The higest total marks in a class:", high_total_marks)
    print("The lowest total marks in a class:",low_total_marks)
#marks_analysis(df)

def student_performance(df):
   # marks_analysis(df)
    highest=df["Avg Marks"].max()
    topper=df[df["Avg Marks"]==highest]
    print("Top performer of the class:",topper["Name"].iloc[0])

    lowest=df["Avg Marks"].min()
    low=df[df["Avg Marks"]==lowest]
    print("Low performer of the class:",low["Name"].iloc[0])

    Top=df[df["Avg Marks"]>85]
    print("---Students Scoring Above 85---")
    for name in Top["Name"]:
        print(name)

    low=df[df["Avg Marks"]<85]
    print("---students scoring below 85---")
    for name in low["Name"]:
        print(name)

    rank=df.sort_values(
        by="Avg Marks",
        ascending=False
    )
    rank=rank.reset_index(drop=True)
    print("---Rank students from highest to lowest---\n",rank[["Name","Avg Marks"]])
#student_performance(df)

def subject_analysis(df):
    subjects=["Maths","Science","English"]
    print("---Subjectwise Average Marks---")
    for subject in subjects:
        print(f"{subject}:{df[subject].mean():.2f}")

    print("---Highest Score in each Subject---")
    for subject in subjects:
        print(f"{subject}:{df[subject].max()}")

    print("---Lowest Score in each Subject---")
    for subject in subjects:
        print(f"{subject}:{df[subject].min()}")

    print("---Easiest Subject---")
    m=df["Maths"].mean()
    s=df["Science"].mean()
    e=df["English"].mean()

    max_avg=max(m,s,e)
    if max_avg==m:
        print("Maths:",m)
    elif max_avg==s:
        print("Science:",s)
    else:
        print("English:",e)

    print("---most difficult subject (lowest class average)---")
    min_avg=min(m,s,e)
    if min_avg==m:
        print("Maths:",m)
    elif min_avg==s:
        print("Science:",s)
    else:
        print("English:",e)

#subject_analysis(df)

def attendance_analysis(df):
    print("---students with attendance analysis---")
    excellent=df[df["Attendance"]>95]
    good=df[(df["Attendance"]>85) & (df["Attendance"]<95)]
    average=df[(df["Attendance"]>65) & (df["Attendance"]<85)]
    poor=df[df["Attendance"]<65]

    print("\nThe students Excellent in attendance")
    for name in excellent["Name"]:
        print(name)

    print("\nThe students good in attendance")
    for name in good["Name"]:
        print(name)

    print("The students average in attendance")
    for name in average["Name"]:
        print(name)

    print("The students poor in attendance")
    for name in poor["Name"]:
        print(name,name)

    print("---Average attendance department-wise---")
    avg_dep=df.groupby("Department")["Attendance"].mean()
    print(avg_dep)
#attendance_analysis(df)

def department_gender_analysis(df):
    print("---Count Of Students in each Department---")
    dep_stu_count=df.groupby("Department")["Name"].count()
    print(dep_stu_count)

    print("---Count Of Male And Female Students---")
    gender_count=df.groupby("Gender")["Name"].count()
    print(gender_count)

    print("---Department-wise Average Marks---")
    dep_avg=df.groupby("Department")["Avg Marks"].mean()
    print(dep_avg)

    print("---Gender-wise Average Marks---")
    gender_avg=df.groupby("Gender")["Avg Marks"].mean()
    print(gender_avg)

    print("---Top performing department---")
    top_avg=dep_avg.max()
    top_dep=dep_avg.idxmax()
    print(top_dep,top_avg)

#department_gender_analysis(df)

def data_operation(df):
    print("---sort students by marks---")
    result=df.sort_values(by="Avg Marks",ascending=False)
    result["Rank"]=range(1,len(result)+1)
    result=result[["Rank","Name","Avg Marks"]]
    print(result)

    print("---sort students by attendance---")
    attendance=df.sort_values(by="Attendance",ascending=False)
    attendance=attendance[["USN","Name","Gender","Department","Attendance"]]
    print(attendance)
    print("\n")
    print("---filtering students based on the department---\n")
    department=["CSE","ECE","ISE","EEE","ME"]
    for dep in department:
        print(f"\n----{dep} department----")
        print(df[df["Department"]==dep])
    print("\n")

    print("---filtering students based on grade----")
    grade=["A","B","C"]
    for g in grade:
        print(f"\n----{g} Grade students---")
        print(df[df["Grade"]==g])

    print("---Search for a student using their USN---")

    usn=int(input("Enter student usn(101-115) to get data:"))
    print(usn)
    result=df[df["USN"]==usn]
    if result.empty:
        print("Invalid Usn")
    else:
        print(result)

# data_operation(df)
if choice=="1":
    print(load_dataset(df))
elif choice=="2":
    print(student_analysis(df))
elif choice=="3":
    print(marks_analysis(df))
elif choice=="4":
    print(student_performance(df))
elif choice=="5":
    print(subject_analysis(df))
elif choice=="6":
    print(attendance_analysis(df))
elif choice=="7":
    print(department_gender_analysis(df))
else:
    print(data_operation(df))
