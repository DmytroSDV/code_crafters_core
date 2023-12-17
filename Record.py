from datetime import datetime

def days_to_birthday(self):
    try:
        current_date = datetime.now().date()
        record_nearest_birthday = self.birthday.value.replace(year=current_date.year)
        if record_nearest_birthday < current_date:
            record_nearest_birthday = self.birthday.value.replace(year=current_date.year + 1)
            days_until_birthday = (record_nearest_birthday - current_date).days
            # print(f"Record: {self.name.value}, Nearest Birthday: {record_nearest_birthday}, Days until Birthday: {days_until_birthday}")
        return days_until_birthday
                
    except AttributeError:
            print(f"Contact name do not have birthday record")