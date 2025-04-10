def get_top_students(data):
    sorted_data = sorted(data, key=lambda x: (x["avg score"], x["name"]))
    output = [[i["name"] + " - " + str(i["avg score"])] for i in sorted_data[::-1]]
    return output
def get_average_age(data):
    avg_age_list = [i["age"] for i in data]
    return round(sum(avg_age_list) / len(avg_age_list),1)
def filter_by_grade(data,grade):
    return len(list(filter(lambda x: x["avg score"] > grade, data)))
