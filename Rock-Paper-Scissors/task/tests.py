from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class RPSTest(StageTest):
    def generate(self) -> List[TestCase]:
        cases = ["rock",
                 "paper",
                 "scissors"]
        return [TestCase(stdin=cases[case],
                         attach=(cases + cases)[case + 1])
                for case in range(len(cases))]

    def check(self, reply: str, attach) -> CheckResult:
        correct_output = "Sorry, but the computer chose {}".format(attach.strip())
        return CheckResult("Sorry, but the computer chose {}".format(attach.strip()) == reply.strip(),
                           "Your answer on \"{}\" was \"{}\". This is a wrong output. The correct output is \"{}\"".format(attach, reply.strip(),
                                                                                                                           correct_output))


if __name__ == '__main__':
    RPSTest("rps.game").run_tests()
