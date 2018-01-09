# The Employee class holds employee information.

class Employee:
    # The __init__ method initializes the attributes.
    def __init__(self, name, idno, dept, job):
        self.__name = name
        self.__idno = idno
        self.__dept = dept
        self.__job = job

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_idno method sets the ID No. attribute.
    def set_idno(self, idno):
        self.__idno = idno
        
    # The set_dept method sets the department attribute.
    def set_dept(self, dept):
        self.__dept = dept

    # The set_job method sets the Job title attribute.
    def set_job(self, job):
        self.__job = job

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_idno method returns the ID No. attribute.
    def get_idno(self):
        return self.__idno

    # The get_dept method returns the department attribute.
    def get_dept(self):
        return self.__dept

    # The get_job method returns the Job Title attribute.
    def get_job(self):
        return self.__job

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID No.: " + self.__idno + \
               "\nDepartment: " + self.__dept + \
               "\nJob Title: " + self.__job
    
