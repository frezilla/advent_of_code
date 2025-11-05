#==============================================================================
# --- Day 4: The Ideal Stocking Stuffer ---
#==============================================================================


import hashlib


def run():
    print("--- Day 4: The Ideal Stocking Stuffer ---")
    fhand = open("puzzle.txt", "r")
    secret_key = ''
    for line in fhand:
        secret_key += line.rstrip()
    nb_zeros = 5
    answer = 0
    n = '0'
    while 1:
        str_value = str(answer)
        test_value = f"{secret_key}{str_value}"
        md5_value = hashlib.md5(test_value.encode()).hexdigest()
        if md5_value.startswith(n.zfill(nb_zeros)):
            break
        answer += 1
    print(f"Réponse : {answer}")


if __name__ == '__main__':
    run()