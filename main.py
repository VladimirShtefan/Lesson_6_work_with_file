from random import sample
File_with_words = 'words.txt'
File_leaders = 'history.txt'


def get_rand_word_and_points(file_for_read):
    """Moving letters in a word.

        Keyword arguments:
        file_for_read -- file with word for questions

    """
    points = 0
    try:
        with open(file_for_read) as file_for_read:
            list_ = list(file_for_read.readlines())
    except FileNotFoundError:
        return 'Не найден фаил'
    for word in list_:
        word = word.split()[0]
        rand_word = ''.join(sample(word, len(word)))
        print(f"Угадайте слово: {rand_word}")
        user_answer = input('Введите ответ: ')
        if user_answer.lower() == word.lower():
            print(f'Верно! Вы получаете 10 очков.')
            points += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')
    return str(points)


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
        point = int(word.split()[1])
        count += 1
        if point > max_points:
            max_points = point
    print(f'Всего игр сыграно: {count}')
    print(f'Максимальный рекорд: {max_points}')


if __name__ == '__main__':
    user_name = input('Введите Ваше имя: ')
    write_history(File_leaders, user_name, get_rand_word_and_points(File_with_words))
    get_stats(File_leaders)
