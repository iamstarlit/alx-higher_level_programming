#!/usr/bin/python3

"""A module of the algorithm to solve N queens puzzle."""


def is_safe(m_queen, nqueen):
    """checks if the queens can or cannot kill each other.

    Args:
        m_queen (list): a list of the queens positions
        nqueen (int): queen number

    Returns:
        bool: True when queens can't kill each other,
            False otherwise

    """

    for index in range(nqueen):

        # check if queens are in the same column
        if m_queen[index] == m_queen[nqueen]:
            return False

        # check if queens are in the same diagonal
        if abs(m_queen[index] - m_queen[nqueen]) == abs(index - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """prints the list of queens positions.

    Args:
        m_queen (list): list of queens position
        nqueen (int): number of queens

    """

    result = []

    # store result in a list 'result'
    for i in range(nqueen):
        result.append([i, m_queen[i]])

    print(result)


def Queen(m_queen, nqueen):
    """Recursively executes Backtracking algorithm.

    Args:
        m_queen (list): list of queens positions
        nqueen (int): number of queens

    """

    # check if 'nqueen' value is equal to length of 'm_queen'
    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    # set value of current queen to -1
    m_queen[nqueen] = -1

    # loop until value of current queen is less
    # than the length of 'm_queen' minus 1
    while m_queen[nqueen] < (len(m_queen) - 1):
        m_queen[nqueen] += 1

        # check if queen is in safe position
        if is_safe(m_queen, nqueen) is True:
            # check if nqueen is not equal to length of 'm_queen'
            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def NQueen(size):
    """Invokes the Backtracking algorithm.

    Args:
       size (int): size of the chessboard

    """

    m_queen = [-1 for i in range(size)]

    Queen(m_queen, 0)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    NQueen(size)
