# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        #instantiate a set
        email_list = set()

        for email in emails:
            split_email = email.split("@")
            local_name = split_email[0].split("+")
            local = "".join(local_name[0].split("."))
            email_name = local + "@" + split_email[1]
            email_list.add(email_name)

        return len(email_list)
    
    def numUniqueEmails2(self, emails: list[str]) -> int:
        email_set = set()

        for email in emails:
            email_list = email.split("@")
            # email_list[0]
            local_list = email_list[0].split("+")
            # local_list[0]
            local_list_prefix = "".join(local_list[0].split("."))
            email_set.add(local_list_prefix + "@" + email_list[1])

        return len(email_set)