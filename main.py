from envparse import env
from checker import PlagiarismChecker

if __name__ == "__main__":
    user_key = env.str("USER_KEY")
    files = env.list("FILES")
    public = env.bool("PUBLIC")
    min_uniq = env.float("MIN_UNIQ")

    checker = PlagiarismChecker(user_key, public)

    uids = {}

    for file in files:
        if file.endswith('.md'):
            with open(file) as f:
                try:
                    uid = checker.add_text(f.read())
                    uids[file] = uid
                except Exception as e:
                    print("::error ::{message}".format(message=e))

    results = {}

    for file in uids:
        try:
            uid = uids[file]
            uniq = checker.get_result(uid)
            results[file] = {
                "uniq": uniq,
                "url": "https://text.ru/antiplagiat/{uid}".format(uid=uid)
            }
        except Exception as e:
            print("::error ::{message}".format(message=e))

    print("::set-output name=results::{results}".format(results=results))

    exit_code = 0

    for file in results:
        if results[file]["uniq"] < min_uniq:
            print("::error ::Text uniq in file {file} is {uniq} < {min}".format(file=file,
                                                                                uniq=results[file]["uniq"],
                                                                                min=min_uniq))
            exit_code = 1

    exit(exit_code)
