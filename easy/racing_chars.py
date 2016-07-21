import sys

def parse_track():
    track = []
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            track.append(test.strip())
    return track

def checkpoint(line):
    if 'C' in line:
        return True
    else:
        return False

def find_passage(line, curr_pos):
    if 'C' in line:
        if abs(line.index('C') - curr_pos) > 1:
            return line.index('_')
        else:
            return line.index('C')
    else:
        return line.index('_')

def find_move(curr_pos, next_pos):
    if next_pos == curr_pos:
        return '|'
    elif next_pos == curr_pos + 1:
        return '\\'
    elif next_pos == curr_pos - 1:
        return '/'

def main():
    curr_pos = None
    track = parse_track()
    for line in track:
        if checkpoint(line):
            to_replace = 'C'
        else:
            to_replace = '_'
        if curr_pos is None:
            curr_pos = find_passage(line, curr_pos)
            print(line.replace(to_replace, '|'))
        else:
            next_pos = find_passage(line, curr_pos)
            print(line.replace(to_replace, find_move(curr_pos, next_pos)))
            curr_pos = next_pos
    
if __name__ == '__main__':
    main()
