# Replace the "ANSWER HERE" with your answer
#28/04/2025
#Rozas Miguel Agustin - TP6 - Introduccion a la programacion
#Ejercicio 1 - List

#sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#sample_list2 = []
#sample_list3 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
#sample_list4 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
#sample_list5 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 5:
        del list_to_remove_elements[5]

    if len(list_to_remove_elements) > 4:
        del list_to_remove_elements[4]

    if len(list_to_remove_elements) > 1: 
        del list_to_remove_elements[0]

    return list_to_remove_elements  # Remove this line and implement
#removed_elements = remove_elements(sample_list)
#print("Remove Elements:")
#print(removed_elements)  # Expected output: ['Green', 'White', 'Black']

#5/05/2025
def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements  # Remove this line and implement
#elements_added = add_elements(sample_list)
#print("Add Elements:") #Input = remove_elements(sample_list) = ['Green', 'White', 'Black']
#print(elements_added) # Expected output: ['Pink', 'Green', 'White', 'Black, 'Yellow']

def is_empty(list_to_check):
    if len(list_to_check) > 0:
        return False
    else:
        return True
     # Remove this line and implement
#print("Is Empty:")
#print(is_empty(sample_list)) #Expected Output: False
#print(is_empty(sample_list2)) #Expected Output: True

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    elif list_to_compare1[2] == list_to_compare2[2]:
        return True
    else:
        return False
    # Remove this line and implement
#print("Checklist:")
#print(check_lists(sample_list,sample_list3)) #Expected output: False
#print(check_lists(sample_list3,sample_list4))# Expected output: True

def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify = [list_of_lists_to_modify [0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
    return list_of_lists_to_modify
    
#print("List_of_lists")
#print(list_of_lists(sample_list5)) #Expected output: [[1, 2], [5, 6, 7], [11, 12]]
