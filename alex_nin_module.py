import pandas as pd

def get_statistics(data_frame, *args):
    '''
    Reads in a data frame and returns the statistical information
    provided by pandas
    
    Params: 
        data_frame: an object containing information in tabular format
        *args: a list of columns to get statistics from
    
    Returns:
    stats_list: a list of statistical information
    '''
    if len(args) < 1:
        return "Please provide at least one column"
    else:
        stats_list = []
        for arg in args:
            if arg not in data_frame.columns:
                continue
            stats_list.append(data_frame[arg].describe())
        return stats_list
    
def main():
    # To test functionality
    data_f = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    data_frame = pd.DataFrame(data_f)
    print(get_statistics(data_frame, 'A', 'B', 'C'))
    
if __name__ == '__main__':
    main()