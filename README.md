# Python Quiz App

A simple, interactive quiz application built with Python. Test your knowledge on various topics with multiple-choice questions!

## Features

- Multiple-choice questions on various topics
- Randomized question order for each playthrough
- Immediate feedback on answers
- Score tracking
- Option to play multiple rounds

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-quiz-app.git
   ```
2. Navigate to the project directory:
   ```
   cd python-quiz-app
   ```

## Usage

Run the quiz app by executing the following command in your terminal:

```
python quiz_app.py
```

Follow the on-screen prompts to answer questions and see your score.

## Customizing the Quiz

To add or modify questions, edit the `questions` list in the `quiz_app.py` file. Each question is a dictionary with the following structure:

```python
{
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer": "Correct option here"
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please open an issue on GitHub.

Happy quizzing!
