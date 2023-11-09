from dado import Dice

def main():
    dice1 = Dice()
    dice2 = Dice()

    for _ in range(5):
        results1 = []
        results2 = []
        for _ in range(2):
            roll1 = dice1.roll()
            roll2 = dice2.roll()
            results1.append(roll1)
            results2.append(roll2)

        print(f"Roll 1: {results1[0]}, Roll 2: {results2[0]}")
        print(f"Roll 1: {results1[1]}, Roll 2: {results2[1]}")
        print(f"Roll 1: {results1[2]}, Roll 2: {results2[2]}")
        print(f"Roll 1: {results1[3]}, Roll 2: {results2[3]}")
        print(f"Roll 1: {results1[4]}, Roll 2: {results2[4]}")

if __name__ == "__main__":
    main()
