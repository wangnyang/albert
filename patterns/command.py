# анин рабочий
# Есть абстрактный класс команды, в котором что-то общее для всех команд, и все остальные классы команд от него наследуются.
from abc import ABC, abstractmethod


class Computer:
    def __init__(self, model: str):
        self.model = model

    def run_code(self, language: str):
        print(f'PC {self.model} is running code in {language} programming language')
    
    def stop(self):
        print('PC stopped running program')


class Command(ABC):

    def __init__(self, pc: Computer):
        self.pc = pc
    
    @abstractmethod
    def execute(self):
        pass

    def unexecute(self):
        self.pc.stop()


class PythonCommand(Command):

    def execute(self):
        self.pc.run_code('Python')


class OcamlCommand(Command):

    def execute(self):
        self.pc.run_code('Ocaml')


class ComputerInterface:
    def __init__(self, python_cmd: PythonCommand, ocaml_cmd: OcamlCommand):
        self.ocaml_cmd = ocaml_cmd
        self.python_cmd = python_cmd
        self.current_cmd = None

    def run(self, cmd):
        if self.current_cmd:
            self.current_cmd.unexecute()
        self.current_cmd = cmd
        cmd.execute()

    def run_python(self):
        self.run(self.python_cmd)
    
    def run_ocaml(self):
        self.run(self.ocaml_cmd)

    def stop(self):
        if self.current_cmd:
            self.current_cmd.unexecute()
            self.current_cmd = None
        else:
            print('PC is idle now')


pc = Computer('Acer')
interface = ComputerInterface(PythonCommand(pc), OcamlCommand(pc))
interface.run_ocaml()
interface.run_python()
interface.stop()
interface.stop()
