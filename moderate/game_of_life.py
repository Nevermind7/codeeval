import sys

def setup():
    """Read initial state from file.
       Return state plus additional dummy edge lines/columns."""
    with open(sys.argv[1], 'r') as test_case:
        width = None
        for line in test_case:
            if not width:
                width = len(line.strip())
                initial =  ['E'*(width+2)]
            initial.append('E{}E'.format(line.strip()))
        initial.append('E'*(width+2))
    return initial

def next_gen(state):
    """Apply rules to state to determine which cells die and live when 
       moving to next generation."""
    new_state = []
    for line_index, line in enumerate(state):
        new_line = ''
        for cell_index, cell in enumerate(line):
            alive_neighbors = live_neighbors(line_index, cell_index, state)
            if cell == '*':
                if alive_neighbors in [2,3]:
                    new_line += '*'
                elif alive_neighbors in [0, 1]:
                    new_line += '.'
                elif alive_neighbors > 3:
                    new_line += '.'
            elif cell == 'E':
                new_line += 'E'
            else:
                if alive_neighbors == 3:
                    new_line += '*'
                else:
                    new_line += '.'
        new_state.append(new_line)
    return new_state

def live_neighbors(line, cell, state):
    """Ignore edge cells because they are not actually part of the state.
       For every other cell, return the number of alive neighbors."""
    is_edge = state[line][cell] == 'E'
    if not is_edge:
        n = [state[line-1][cell-1],state[line-1][cell],state[line-1][cell+1],
             state[line][cell-1],                      state[line][cell+1],
             state[line+1][cell-1],state[line+1][cell],state[line+1][cell+1]]
        return len([x for x in n if x == '*'])

def output(state):
    state = [x.replace('E', '') for x in state[1:-1]]
    for line in state:
        print(line)

def main():
    state = setup()
    for i in range(10):
        state = next_gen(state)
    output(state)
        
if __name__ == '__main__':
    main()
