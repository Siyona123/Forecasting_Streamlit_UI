from exc import input_number

def test_index(index,list):
    try:
        val = list[index]
        return val
    except IndexError:
        return f"There is only {len(list)} elements"


list=[1,2,3,4,5,6,7,8,9]
index=input_number("Enter index:")
print(test_index(index,list))

