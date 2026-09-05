import random
import pytest

def compute_average(values):
    total =0
    for value in values:
        total+=value

    avg = total/len(values)    
    print(f'The average is: {avg}')
    return avg

# pytest executes functions/methods as tests that start with "test_"
def test_compute_average():
    values = [0, 1, 2, 3]
    print(values)
    assert compute_average(values) == 1.5


    random.seed() # for reproducibility
    values = [random.randint(0, 100) for _ in range(10)]
    print(values)
    compute_average(values)


def main():
    # TODO: write your own code to call compute_average()
    test_compute_average()
    pass

if __name__ == "__main__":
    main()