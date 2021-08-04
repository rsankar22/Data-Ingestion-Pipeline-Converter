import fileInScan
from validationSchema import excel_valid
import fileInScan as f

user = input('Input path here:')
print(excel_valid(fileInScan.pullFile(user)))