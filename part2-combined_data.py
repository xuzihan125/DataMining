count_rating = 0  # total rating number
count_user = {}  # user and their rating user_id:{movie_id: rating, ....]
earliest_date = 3000  # date of rating : earliest one
latest_date = 0  # date of rating : latest one
movie_map = {}
movie_name_map = {}


def read_rating_file(file_name, size=None):
    print(file_name)
    global count_rating, earliest_date, latest_date
    file_source = open(file_name, "r")
    last_index = -1
    while True:
        line = file_source.readline()
        if size is not None and size <= count_rating:
            break
        if not line:
            break
        elif line.find(",") == -1:
            last_index = int(line.split(":")[0])
        else:
            count_rating = count_rating + 1
            user_id, rate, year = line.split(",")
            user_id = int(user_id.strip())
            rate = int(rate.strip())
            year = int(year.split("-")[0].strip())
            if count_user.get(user_id) and count_user.get(user_id).get(last_index):
                print(line)
            if not count_user.get(user_id):
                count_user[user_id] = {}
            count_user[user_id][last_index] = rate
            earliest_date = min(earliest_date, year)
            latest_date = max(latest_date, year)


def read_movie_file(file_name):
    print(file_name)
    file_source = open(file_name, "r")
    while True:
        line = file_source.readline()
        if not line:
            break
        movie_id, _, name = line.split(",", maxsplit=2)
        name = name.strip()
        movie_map[int(movie_id.strip())] = name
        movie_name_map[name] = movie_name_map.get(name) + 1 if movie_name_map.get(name) else 1


def display_result(question=[True, True, True]):
    if question[0]:
        question_1()

    if question[1]:
        question_2()

    if question[2]:
        question_3()


def question_1():
    print("3.a: total number of records:{0}".format(count_rating))
    # 480189 user
    print("3.b: total number of unique user:{0}".format(len(count_user)))
    #
    print("3.c: range of date: from {0} to {1}".format(earliest_date, latest_date))


def question_2():
    count_one = 0
    count_four = 0
    for key in movie_name_map:
        if movie_name_map[key] == 1:
            count_one += 1
        elif movie_name_map[key] == 4:
            count_four += 4
    print("4.a: number of movie with unique name:{0}".format(count_one))
    print("4.b: number of movie names refer to four movie:{0}".format(count_four))


def question_3(special_num=200, rate=5):
    spec_user_count = 0
    minimal_id = 2649429
    for user_id in count_user:
        if (len(count_user[user_id]) == special_num):
            spec_user_count += 1
            if (minimal_id > user_id):
                minimal_id = user_id

    print("5.a: number of user that rated exactly {0} movies:{1}".format(special_num, spec_user_count))
    print("5.b: lowest user ID:{0}".format(minimal_id))
    movie_list = []
    for movie_id in count_user[minimal_id]:
        if int(count_user[minimal_id][movie_id]) == rate:
            movie_list.append(movie_map[movie_id])
    print("name of movies rated {0}:".format(rate) + str(movie_list))


read_rating_file("data/archive/combined_data_1.txt")
read_rating_file("data/archive/combined_data_2.txt")
read_rating_file("data/archive/combined_data_3.txt")
read_rating_file("data/archive/combined_data_4.txt")
read_movie_file("data/archive/movie_titles.csv")

display_result()
