from l1_8_module import *

def get_list_from_file(filename):
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def main():
    working_sample = get_list_from_file("dataset_1.txt")
    print(f'The Mean is: {get_sample_mean(working_sample)}')
    print(f'The Std. Dev is: {get_sample_standard_dev(working_sample)}')
    print(f'The Median is: {get_sample_median(working_sample)}')
    print(f'The Low Quartil is: {get_n_quartil(Quartil.LOW, working_sample)}')
    print(f'The Mid Quartil is: {get_n_quartil(Quartil.MID, working_sample)}')
    print(f'The High Quartil is: {get_n_quartil(Quartil.HIGH, working_sample)}')
    print(f'The 50th Percentil is: {get_n_percentil(0.5, working_sample)}')
    
if __name__ == "__main__":
    # execute only if run as a script
    main()