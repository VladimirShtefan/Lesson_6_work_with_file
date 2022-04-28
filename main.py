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
    with open(file_for_read) as file_for_read:
        return list(file_for_read.readlines())


def get_word_with_rand_symbols(list_, count):
    """Moving letters in a word.

        Keyword arguments:
        list_ -- list with words
        count -- word number in the list

    """
    word = list_[count].replace('\n', '')
    rand_word = ''.join(sample(word, len(word)))
    print(f"Угадайте слово: {rand_word}")
    return word


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
    with open(file_for_stats) as file:
        stats_file = list(file.readlines())
    max_points = 0
    count = 0
    for word in stats_file:
        point = int(word.replace('\n', '').split(' ')[1])
        count += 1
        if point > max_points:
            max_points = point
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
