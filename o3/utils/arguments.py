import argparse

class Arguments:

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Run Yaana script")

        parser.add_argument("--ide", type=str, help="Preferred IDE")
        parser.add_argument("--pr", type=str, help="Preferred project--either 'Backend(be)' or 'Frontend(fe)'")
        args = parser.parse_args()

        preferred_ide, preferred_pr = args.ide, args.pr
        return [preferred_ide, preferred_pr]
