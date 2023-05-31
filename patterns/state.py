# не работает у меня. непонятно

from abc import ABC, abstractmethod

class StudentState(ABC):
    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def study(self):
        pass


class EatingStudentState(StudentState):
    def eat():
        return 'already eating'
    
    def sleep():
        return 'cannot sleep rn, but surely will after.'
    
    def study():
        return 'watching some educational videos'
    

class SleepingStudentState(StudentState):
    def eat():
        return 'cannot eat rn, but will surely wake up hungry'

    def sleep():
        return 'already sleeping'

    def study():
        return 'our students are studying even while they are dreaming'
    

class StudyingStudentState(StudentState):
    def eat():
        return 'should not be distracted with food while studying'

    def sleep():
        return 'should not fall asleep while studying'

    def study():
        return 'now studying twice as hard'


class Student:
    def __init__(self, name, state):
        self.name, self.state = name, state

    def get_state(self):
        return self.state
    
    def set_state(self, new_state: StudentState):
        if isinstance(new_state, StudentState):
            self.state = new_state

    state = property(get_state, set_state)

    def sleep(self):
        self._execute('sleep')

    def eat(self):
        self._execute('eat')

    def study(self):
        self._execute('study')

    def _execute(self, action):
        print(f'{self.name}: {getattr(self.state, action)()}')

kirill = Student('Kirill', StudyingStudentState)
kirill.study()
kirill.eat()
kirill.sleep()
kirill.state = EatingStudentState()
kirill.study()
kirill.eat()
