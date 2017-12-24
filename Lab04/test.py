import sys
from pprint import pprint as pp
from projectAnalytics import *
if len(sys.argv) != 2:
    print("Usage: test.py <test case number>");
    sys.exit()
print(sys.argv[1])
if sys.argv[1] == '1':
    print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    print(getComponentCountByProject("96CC6F98-B44B-4FEB-A06B-390432C1F6EA"))
    print(getComponentCountByProject("invalid project id"))
if sys.argv[1] == '2':
    print(getComponentCountByStudent("Adams, Keith"))
    print(getComponentCountByStudent("Young, Frank"))
    print(getComponentCountByStudent("Non existent student"))
if sys.argv[1] == '3':
    pp(sorted(getParticipationByStudent("Young, Frank")))
    pp(sorted(getParticipationByStudent("Robinson, Pamela")))
    print(getParticipationByStudent("Non existent student"))
if sys.argv[1] == '4':
    print(sorted(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")))
    print(sorted(getParticipationByProject("6CCCA5F3-3008-46FF-A779-2D2F872DAF82")))
    print(getParticipationByProject("invalid project id"))
if sys.argv[1] == '5':
    pp(getProjectByComponent({'T71.386', 'C407.660', 'L760.824', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'}))
    pp(getProjectByComponent({'C108.908', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'}))
if sys.argv[1] == '6':
    pp(getStudentByComponent({'T71.386', 'C407.660', 'L760.824', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'}))
    pp(getStudentByComponent({'C108.908', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'}))
if sys.argv[1] == '7':
    pp(getComponentByStudent({'Young, Frank', 'Robinson, Pamela', 'White, Diana'}))
    pp(getComponentByStudent({'Thomas, Mark', 'Robinson, Pamela', 'White, Diana'}))
if sys.argv[1] == '8':
    print(getCommonByProject('082D6241-40EE-432E-A635-65EA8AA374B6', '90BE0D09-1438-414A-A38B-8309A49C02EF'))
    print(getCommonByProject('6CCCA5F3-3008-46FF-A779-2D2F872DAF82', '90BE0D09-1438-414A-A38B-8309A49C02EF'))
    print(getCommonByProject('6CCCA5F3-3008-46FF-A779-2D2F872DAF82', 'Invalid'))
if sys.argv[1] == '9':
    print(getCommonByStudent("Young, Frank", "White, Diana"))
    print(getCommonByStudent("Robinson, Pamela", "White, Diana"))
    print(getCommonByStudent("Robinson, Pamela", "Invalid"))
if sys.argv[1] == '10':
    pp(sorted(getProjectByCircuit()))
if sys.argv[1] == '11':
    pp(sorted(getCircuitByStudent()))
if sys.argv[1] == '12':
    print(sorted(getCircuitByStudentPartial("James")))
    print(getCircuitByStudentPartial("Invalid"))
    
