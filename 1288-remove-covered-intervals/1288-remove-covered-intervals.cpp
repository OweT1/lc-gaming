class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const vector<int> a, const vector<int> b){
            if (a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });

        int res = 0, r = 0;
        for (vector<int> x: intervals) {
            res += x[1] > r;
            r = max(r, x[1]);
            for (int k: x) std::cout << k << " ";
            std::cout << "\n";
        }

        return res;
    }
};