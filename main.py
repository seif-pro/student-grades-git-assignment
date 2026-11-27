"""Simple student grade calculator."""

def average(grades):
    return sum(grades) / len(grades) if grades else 0

if __name__ == '__main__':
    grades = [85, 90, 78, 92, 88]
    print(f'Grades entered: {len(grades)}')
    print(f'Average grade: {average(grades):.1f}')
    print('Status: Pass' if average(grades) >= 50 else 'Status: Fail')
