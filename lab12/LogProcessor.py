import re


if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[(?:24\/Mar\/2009:14:39:35|24\/Mar\/2009:14:[4-5][0-9]:[0-5][0-9]|24\/Mar\/2009:1[5-9]:[" \
              r"4-5][0-9]:[0-5][0-9]|24\/Mar\/2009:2[0-3]:[4-5][0-9]:[0-5][" \
              r"0-9]|25\/Mar\/2009:11:43:29)\s\S+\s\S+\s\S+(?:TH)(?:\s+|\S+) "
    number_of_matched_requests = 0
    read_lines = 0

    with open("acess_log_Jul95") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nNumber of all words successful requests with TH: %d" % number_of_matched_requests)