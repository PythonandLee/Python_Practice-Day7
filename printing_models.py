# Devide two parts for 'print designs' and 'reveal final results'.
# Use 'while' to determine if 'unprinted_designs' is empty or not.
# Store unprinted models in the list. It is convenient when recall the function
# if the list is including lots elements.

def print_models(unprinted_designs, completed_models):
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['flyerA', 'businesscard', 'invitaiton', 'poster']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)