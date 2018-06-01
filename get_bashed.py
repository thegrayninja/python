## Saves current user's CodeBashing Status.
## If user is not 100% complete in primary course, the user data is
## appended to "Data", which then is currently printed to the screen
## using the ShowData() function.
## Email template stored in file, but not currently in use. Simply return
## "EmailMessage" within the Class UserStatus-def EmailTemplate to use

import json



def main():
    Data = GetData()
    ShowData(Data)


class UserStatus:
    Email = ""
    PrimaryCourse = ""
    CompletedPercentage = ""
    LastActive = ""


    def EmailTemplate(self):
        Name = self.Email.split('.')
        FirstName = Name[0].capitalize()

        ##currently disabled, but didn't want to lose my work :)
        EmailMessage = """
Hello {}!

  Information Security is here to give you a quick update on your CodeBashing Status.
  
        Primary Course: {}
        Percentage Completed: {}
        Last Active: {}
  
Thank you and have a nice day!
BHN InfoSec
""".format(FirstName, self.PrimaryCourse, self.CompletedPercentage, self.LastActive)

        return("{},{},{},{},{}".format(FirstName, self.Email, self.PrimaryCourse, self.CompletedPercentage, self.LastActive))


def GetData():
    APIKey = "<key>"
    AuthToken = "<token>"
    CurlCommand = "curl 'https://<domain>.codebashing.com/api/v1/users/sign_in_and_course_info' -H \"X-API-KEY: {}\" -H 'Authorization: Token token=\"{}\"' > codebash.json".format(APIKey, AuthToken)
    #subprocess.Popen(CurlCommand, shell=True, stdout=subprocess.PIPE).stdout.read()

    with open('codebash.json') as JsonData:
        CodeData = json.load(JsonData)


    #print(CodeData[0])

    AllUsers = []
    Counter = 0

    for i in CodeData:
        Email = (CodeData[Counter]["email"])
        PrimaryCourseName = CodeData[Counter]["primary_course_name"]
        if PrimaryCourseName != None:
            Percentage = CodeData[Counter][PrimaryCourseName + ".completed_percentage"]
            LastActive = CodeData[Counter]["last_active_at"]
        else:
            PrimaryCourseName = "No Active Courses"
            Percentage = "0"

        i = UserStatus()
        i.Email = Email
        i.PrimaryCourse = PrimaryCourseName
        Percentage = "{}%".format(str(Percentage).split('.')[0])
        i.CompletedPercentage = Percentage
        LastActive = LastActive.split('T')
        LastActive = LastActive[0]
        i.LastActive = LastActive
        if Percentage != "100%":
            #print(i.EmailTemplate())
            AllUsers.append(i.EmailTemplate())

        Counter += 1
    return(AllUsers)


def ShowData(Data):
    for i in Data:
        print(i)


if __name__ == main():
    main()
