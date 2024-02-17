from tarologist_ai.datasets.tarot_dataset import get_dataset

def main():
    dataset = get_dataset()
    print(dataset.head(5).to_numpy())

if __name__ == "__main__":
    main()