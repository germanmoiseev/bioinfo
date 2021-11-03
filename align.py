x_seq = " INSURANCE" # MUST ADD SPACE BEFORE THE SEQ
y_seq = " SURFACE" # MUST ADD SPACE BEFORE THE SEQ

P = 1
M = -1
G = -1


scores = [[None]*len(y_seq) for i in range(len(x_seq))]

def get_score(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return scores[0][y-1] + G
    elif y == 0:
        return scores[x-1][0] + G
    else:
        if x_seq[x] == y_seq[y]:
            xy_move = scores[x-1][y-1] + P
        else:
            xy_move = scores[x-1][y-1] + M
        y_move = scores[x][y-1] + G
        x_move = scores[x-1][y] + G
    best_move = max(xy_move, x_move, y_move)
    return best_move

def get_max_index():
    max_score = scores[0][0]
    max_id = (0, 0)
    all_max_ids = [max_id]
    for i in range(len(x_seq)):
        for j in range(len(y_seq)):
            if scores[i][j] >= max_score: #maybe better use >, it depends
                prevmax = max_score
                max_score = scores[i][j]
                max_id = (i, j)
                if scores[i][j] == prevmax:
                    all_max_ids.append(max_id)
                else:
                    all_max_ids = [max_id]

    return max_id, max_score, all_max_ids
    
def result(fromend=True):
    if fromend:
        x, y = len(x_seq)-1, len(y_seq)-1
        return get_sequence(x, y)
    else:
        ids, _,  allids = get_max_index()
        x, y = ids
        results = []
        for idea in allids:
            results.append(get_sequence(idea[0], idea[1]))
        return results
    
def get_sequence(x, y):
    reversed_seq_x = ""
    reversed_seq_y = ""
    while x > 0 or y > 0:
        if x > 0 and y > 0:
            xy_move = scores[x-1][y-1]
            x_move = scores[x-1][y]
            y_move = scores[x][y-1]
            best = max(xy_move, x_move, y_move)
        elif x > 0:
            best = scores[x-1][y]
        else:
            best = scores[x][y-1]
        if xy_move == best:
            reversed_seq_x += x_seq[x]
            reversed_seq_y += y_seq[y]
            x -= 1
            y -= 1
        elif x_move == best or y == 0:
            reversed_seq_x += x_seq[x]
            reversed_seq_y += "_"
            x -= 1
        else:
            reversed_seq_x += "_"
            reversed_seq_y += y_seq[y]
            y -= 1
    return reversed_seq_x[::-1], reversed_seq_y[::-1]

for i in range(len(x_seq)):
    for j in range(len(y_seq)):
        scores[i][j] = get_score(i, j)
for line in scores:
    print(line)

result = result() # result(False) if need all results from max values, not from the corner

print()
print(*result, sep="\n")
print(f"Score: {scores[len(x_seq)-1][len(y_seq)-1]}")
