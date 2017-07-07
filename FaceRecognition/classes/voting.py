
class Voting:
    """
    Class the provides voting methods for the ensemble.
    """

    MAJORITY, WEIGHTED = range(2)

    def __init__(self, voting_scheme=MAJORITY, weights=[]):
        """
        Define the selected voting scheme (default is majoritary)
        Set the weights (default is an empty list)
        """
        self.voting_scheme = voting_scheme
        self.weights = weights

    def getVotingSchemeName(self):
        """
        Get the name of the selected voting scheme to be used in the report.
        """
        if self.voting_scheme == self.MAJORITY:
            return "Majority Voting"
        elif self.voting_scheme == self.WEIGHTED:
            return "Weighted Voting"
        return ""

    def vote(self, subjects, weights=[]):
        """
        Call the selected voting scheme
        """
        if self.voting_scheme == self.WEIGHTED:
            if not weights:
                weights = self.weights
            return self.weightedVoting(subjects, weights)
        else:
            return self.majorityVoting(subjects)

    def majorityVoting(self, subjects):
        """
        Majority voting.
        Return -1 for empty list
        """

        if len(subjects) == 0:
            return -1

        subject_voted = []
        number_of_votes = []

        # Count votes
        for i in range(0, len(subjects)):
            if subjects[i] in subject_voted:
                index = subject_voted.index(subjects[i])
                number_of_votes[index] = number_of_votes[index] + 1
            else:
                subject_voted.append(subjects[i])
                number_of_votes.append(1)

        index_max_voted = number_of_votes.index(max(number_of_votes))
        return subject_voted[index_max_voted]

    def weightedVoting(self, subjects, weights):
        """
        Weighted voting.
        """

        if len(subjects) == 0 or len(weights) == 0:
            return -1

        if len(subjects) != len(weights):
            return -1

        subject_voted = []
        value_of_votes = []

        # Count votes
        for i in range(0, len(subjects)):
            if subjects[i] in subject_voted:
                index = subject_voted.index(subjects[i])
                value_of_votes[index] = value_of_votes[index] + weights[i]
            else:
                subject_voted.append(subjects[i])
                value_of_votes.append(weights[i])

        max_value = max(value_of_votes)

        # If we have duplicate values then we have a tie
        if len(value_of_votes) != len(set(value_of_votes)):
            most_voted = []
            # Create a list of the subjects that have more votes
            for i in range(0, len(subject_voted)):
                if value_of_votes[i] == max_value:
                    most_voted.append(subject_voted[i])

            temp_subjects = []
            # Create a new list of the subjects
            for i in range(0, len(subjects)):
                if subjects[i] in most_voted:
                    temp_subjects.append(subjects[i])

            return self.majorityVoting(temp_subjects)
        else:
            index_max_voted = value_of_votes.index(max_value)
            return subject_voted[index_max_voted]
