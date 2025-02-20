class University:
    def __init__(self, universityname):
        self.universityname = universityname

    def getUniversityName(self):
        return self.universityname

class Location:  # Fixed the missing `class` keyword
    def __init__(self, locationname):
        self.locationname = locationname

    def getLocationName(self):
        return self.locationname

class College(University, Location):
    def __init__(self, collegename, universityname, locationname):
        self.collegename = collegename
        University.__init__(self, universityname)
        Location.__init__(self, locationname)

    def getCollegeName(self):
        return self.collegename

coll = College("ABC Engineering College", "Anna University", "Chennai")
print(coll.getUniversityName())  # Returns "Anna University"
print(coll.getLocationName())   # Returns "Chennai"
print(coll.getCollegeName())    # Returns "ABC Engineering College"
