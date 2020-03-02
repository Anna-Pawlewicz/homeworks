from name_plus_surname_generators import surname_generator, save_result, name_generator


def name_plus_surname_generator():
    name = name_generator.name_generator()
    surname = surname_generator.surname_generator()
    result = name, surname
    return result



