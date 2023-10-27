questions = [
    '1. The language of Lakshadweep, a Union Territory of India, is',
    '2. September 27 is celebrated every year as',
    '3. Which of the following is observed as Sports Day every year?',
    '4. Pongal is a popular festival of which state?',
    '5. Ghototkach in Mahabharat was the son of',
    '6. The first month of the Indian national calendar is',
    '7. Which of the following is a folk dance of India?',
    '8. Who painted the Mona Lisa?',
    '9. Which famous physicist developed the theory of relativity?',
    '10. Which country is known as the "Land of the Rising Sun"?',
    '11. Which animal is known for its ability to change its color?',
    '12. Who is the author of the Harry Potter book series?'
]

answers = [
    ('A. Tamil', 'B. Hindi', 'C. Malayalam', 'D. Telugu', 'C'),
    ('A. Teacher\'s Day', 'B. National Integration Day', 'C. World Tourism Day', 'D. International Literacy Day', 'C'),
    ('A. 22nd April', 'B. 26th July', 'C. 29th August', 'D. 2nd October', 'D'),
    ('A. Karnataka', 'B. Kerala', 'C. Tamil Nadu', 'D. Andhra Pradesh', 'B'),
    ('A. Duryodhan', 'B. Arjuna', 'C. Yudhishthir', 'D. Bhima', 'A'),
    ('A. Magha', 'B. Chaitra', 'C. Ashadha', 'D. Vaishakha', 'B'),
    ('A. Kathakali', 'B. Mohiniattam', 'C. Garba', 'D. Manipuri', 'A'),
    ('A. Vincent van Gogh', 'B. Leonardo da Vinci', 'C. Pablo Picasso', 'D. Michelangelo', 'B'),
    ('A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Marie Curie', 'B'),
    ('A. China', 'B. India', 'C. Japan', 'D. South Korea', 'C'),
    ('A. Tiger', 'B. Elephant', 'C. Chameleon', 'D. Caterpiee', 'C'),
    ('A. J.R.R. Tolkien', 'B. J.K. Rowling', 'C. George R.R. Martin', 'D. Stephenie Meyer', 'B')
]

levels = [1000, 2500, 5000, 8000, 10000, 25000, 50000, 100000, 250000, 500000, 800000, 1000000]

for i in range(len(questions)):
    print(f'(Question for Rs:{levels[i]})')
    print(questions[i])
    print(f'{answers[i][0]}, {answers[i][1]}, {answers[i][2]}, {answers[i][3]}')
    reply = input('Enter your answer: ')
    if reply.upper() == answers[i][4].upper():
        print(f'The answer is correct! Congratulations, you have won Rs: {levels[i]}')
    else:
        print('Oops! Better luck next time.')
        break
