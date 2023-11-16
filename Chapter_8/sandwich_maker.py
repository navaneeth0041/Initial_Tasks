import pyinputplus as pyip
prices={
    'wheat' : 5, 'white' : 3, 'sourdough':2, 'chicken':10, 'turkey':20, 'ham':15, 'tofu':5, 'cheddar':2,'swiss':5,'mozzarella':5,'mayo':1,'mustard':1,'lettuce':2,'tomato':2
    
    }
bread_type=pyip.inputMenu(['wheat','white','sourdough'],prompt='Select your bread type: ')
protein_type=pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='Select you protein type:')
cheese=pyip.inputYesNo('Cheese?(yes,no)')

if cheese=='yes':
    cheese_type=pyip.inputMenu(['cheddar','Swiss','mozzarella'],prompt='Select the desired type: ')

additionals=pyip.inputMenu(['mayo','mustad','lettuce','tomato'],prompt='Select the toppings: ')

cost=prices[bread_type]+prices[protein_type]+prices[cheese_type]+prices[additionals]
n_sand=pyip.inputInt('How many sandwiches do you need?',min=1)

t_cost=cost*n_sand
print(t_cost)