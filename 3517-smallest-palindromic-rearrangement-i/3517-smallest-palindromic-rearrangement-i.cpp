class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> freq(26, 0);

        for (char c: s.substr(0, s.length()/2)) {
            freq[c-'a']++;
        }

        std::string result;
        for (int i=0; i<freq.size(); i++) {
            int count = freq.at(i);
            if (count > 0) result += string(count, char(static_cast<int>('a')+i));
        }
        std::string reversed_result(result.rbegin(), result.rend());
        return result + (s.length() % 2 == 1 ? string(1, s[s.length()/2]) : "") + reversed_result;
    }
};