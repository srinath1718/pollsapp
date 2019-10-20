from restapi.models import EmployeeModel

class Employee:

    def findEmployeeById(self,empID):

        return EmployeeModel.objects.filter(id=empID)

    def getEmployeById(self, id):

        return EmployeeModel.objects.get(id=id)

    def setEmployeeModelObject(self,postData, empModel=None):

        print(empModel)
        if empModel is None:
            empModel = EmployeeModel()

        empModel.emp_name = postData['emp_name']
        empModel.emp_email = postData['emp_email']
        empModel.emp_address = postData['emp_address']
        empModel.emp_city = postData['emp_city']

        return empModel

    def findEmployeeByEmail(self,empEmail):

        return EmployeeModel.objects.get(emp_email=empEmail)

    def findAll(self):

        return EmployeeModel.objects.values()



