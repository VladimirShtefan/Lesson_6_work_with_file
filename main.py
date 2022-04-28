from random import sample
file_with_words = 'words.txt'
file_leaders = 'history.txt'
points = 0
step = 0


def input_user_name():
    """Function to get username."""
    name = input('Введите Ваше имя: ')
    return name


def get_all_words(file_for_read):
    """Reading from a file list with words.

        Keyword arguments:
        file_for_read -- name file

    """
    list_words = []
    with open(file_for_read, 'r') as file_for_read:
        for line in file_for_read:
            list_words.append(line.replace('\n', ''))
    return list_words


def get_word_with_rand_symbols(list_, count):
    """Moving letters in a word.

        Keyword arguments:
        list_ -- list with words
        count -- word number in the list

    """
    rand_word = ''.join(sample(list_[count],  len(list_[count])))
    print(f'Угадайте слово: {rand_word}')
    return list_[count]


def input_user_answer():
    """Function to get unswer."""
    answer = input('Введите ответ: ')
    return answer


def check_the_correct_answer(random_word, user_answer):
    """Function to check the correct answer.

        Keyword arguments:
        random_word -- jumbled word
        user_answer -- user answer

    """
    if random_word.lower() == user_answer.lower():
        print(f'Верно! Вы получаете 10 очков.')
        return 10
    print(f'Неверно! Верный ответ – {random_word}.')
    return 0


def write_history(file_for_write, name_leader, sum_points):
    """Write in a file user name and points.

        Keyword arguments:
        file_for_write -- name file for write
        name_leader -- user name
        sum_points -- summary points

    """
    with open(file_for_write, 'a') as file_for_write:
        file_for_write.write(f'{name_leader} {sum_points}\n')


def get_stats(file_for_stats):
    """Displaying information about the number of games and the record.

        Keyword arguments:
        file_for_stats -- name file with information about games and the record

    """
    with open(file_for_stats, 'r') as file:
        max_points = 0
        count = 0
        for line in file:
            count += 1
            if int(line.replace('\n', '').split(' ')[1]) > max_points:
                max_points = int(line.replace('\n', '').split(' ')[1])
    print(f'Всего игр сыграно: {count}')
    print(f'Максимальный рекорд: {max_points}')


if __name__ == '__main__':
    user_name = input_user_name()
    while step < len(get_all_words(file_with_words)):
        points += check_the_correct_answer(get_word_with_rand_symbols(get_all_words(file_with_words), step),
                                           input_user_answer())
        step += 1
    write_history(file_leaders, user_name, points)
    get_stats(file_leaders)
