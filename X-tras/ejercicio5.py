def get_student_data(student_dict, key_list):
    print('')
    for key in key_list:
        student_dict[key] = input(f'Please enter the {key} ')
    return student_dict
        
def assign_trimester(student_dict):
    acum = 0
    promedio = 0
    for key, value in student_dict.items():
        if key == 'Middle School Grades' or key == 'High School Grades':
            acum += int(value)
            average = acum / 2
    student_dict['Average'] = average
    if average >= 18:
        student_dict['Trimester'] = 2
    elif average >= 12:
        student_dict['Trimester'] = 1
    else:
        student_dict['Trimester'] = 'Rechazado'
    return student_dict, average        

def print_student_report(student_dict):
    print('\n**********STUDENT REPORT**********\n')
    for key, value in student_dict.items():
        print(f'{key}: {value}')
    print('')

def get_totals(student_dict, trimesters, average):
    trimesters[student_dict['Trimester']]['students'] += 1
    trimesters[student_dict['Trimester']]['averages'] += average
    return trimesters

def print_university_report(students_count, trimesters):
    print('\n**********FINAL REPORT**********\n')
    print(f'Total Students: {students_count}')
    print('Average of Students per Trimester: ', end='')
    print(round(students_count/2, 2))
    print('Number of Students per Trimester: ')
    for key, value in trimesters.items():
        print(f' - {key}º Trimester: ', end = '')
        print(trimesters[key]['students'])
    print('General Average Grade: ')
    for key, value in trimesters.items():
        print(f' - {key}º Trimester: ', end = '')
        try:
            print(round(trimesters[key]['averages']/trimesters[key]['students'], 2))
        except:
            print('0')
    print('')


def main():
    student_count = 0
    trimesters = {
        1:{
            'students': 0,
            'averages': 0,

        },
        2:{
            'students': 0,
            'averages': 0,

        }
    }
    student_dict = {}
    students = []
    key_list = ['ID', 'Middle School Grades','High School Grades']
    student_count = 0
    while True:
        student_count += 1
        student_dict = get_student_data(student_dict, key_list)
        student_dict, average = assign_trimester(student_dict)
        print_student_report(student_dict)
        trimesters = get_totals(student_dict, trimesters, average)
        if input('Do you want to continue Y or N: ').upper() == 'N':
            break
    print_university_report(student_count, trimesters)
main()