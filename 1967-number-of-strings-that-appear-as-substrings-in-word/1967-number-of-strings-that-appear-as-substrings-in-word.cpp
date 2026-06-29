class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int result = 0;
        for (int i = 0; i < patterns.size(); i++) {
            result += word.contains(patterns[i]) ? 1 : 0;
        }
        return result;
    }
};