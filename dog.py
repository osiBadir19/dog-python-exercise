from datetime import date


class Dog:
    """
    create a dog class
    """
    def __init__(self, name: str, size: int,
                 breed_default='unknown', date_of_birth='unknown'):
        self.name = name
        self.size = size
        self.breed = breed_default
        self.birth = date_of_birth

    def bark(self):
        """get the dog to bark, by printing word woof!"""
        print("woof!")

    def dog_id(self):
        """ return a detailed id information of the dog object"""
        return "dog name:\n\t{0}\n------\ndog size in kg:\n\t{1}\n------\n" \
               "dog breed:\n\t{2}\n------\ndog birth date:\n\t{3}\n------\n".format(
                    self.name, self.size, self.breed, self.birth)

    def get_name(self):
        """ return the dog name """
        return "the dog name is : {0}".format(self.name)

    def set_name(self, new_name: str):
        """allow the user to set an alphapitical name between
        2 and 30 characters     """
        if 2 >= len(new_name) <= 30:
            self.name = new_name.title()

    def dog_years(self):
        """ return the dog age in dog years (1 year = 7 dog years) """
        int_birth = self.birth.split("/")
        d1 = str(date.today().strftime("%d/%m/%Y")).split("/")
        d3 = [int(d1[1]) - int(int_birth[1]),
                int(d1[2]) - int(int_birth[2])]
        if d3[1] < 0:
            return d3[2] - 1
        else:
            return d3[2]//7
