import numpy as np
from part1 import *

input_data = prepare_data('input.txt')
# print(input_data)
in_dots, in_max_x, in_max_y, in_start =  get_dots(input_data)
# print(in_max_x, in_max_y)
input_folds = get_folds(input_data, in_start)
input_paper = init_paper(in_max_x, in_max_y)
updated_paper = update_paper(input_paper, in_dots)
folded_paper = fold_paper(updated_paper, input_folds)
print(folded_paper)
print(np.count_nonzero(folded_paper == '#'))