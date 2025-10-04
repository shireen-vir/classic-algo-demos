def step_function(x):
    """Activation function: step function"""
    return 1 if x >= 0 else 0

def main():
    print("=== Perceptron Learning Rule Demo ===")

    n = int(input("Enter number of inputs: "))

    m = int(input("Enter number of training examples: "))
    training_data = []
    print("\nEnter training data (inputs followed by target output):")
    for i in range(m):
        example = input(f"Example {i+1}: ").split()
        inputs = list(map(float, example[:n]))
        target = int(example[n])
        training_data.append((inputs, target))

    lr = float(input("\nEnter learning rate (e.g., 0.1): "))

    weights = [0.0] * n
    bias = 0.0

    print("\nStarting training...")

    # Training loop
    epochs = 0
    while True:
        error_count = 0
        for inputs, target in training_data:

            y_in = sum(w * x for w, x in zip(weights, inputs)) + bias
            output = step_function(y_in)

            error = target - output
            if error != 0:
                error_count += 1
                for i in range(n):
                    weights[i] += lr * error * inputs[i]
                bias += lr * error

        epochs += 1
        if error_count == 0:
            break  # training complete

    print("\nTraining complete!")
    print(f"Number of epochs: {epochs}")
    print("Final Weights:", weights)
    print("Final Bias:", bias)

    print("\nTesting trained perceptron:")
    for i, (inputs, target) in enumerate(training_data):
        y_in = sum(w * x for w, x in zip(weights, inputs)) + bias
        output = step_function(y_in)
        print(f"Example {i+1}: Input={inputs}, Target={target}, Output={output}")


if __name__ == "__main__":
    main()
